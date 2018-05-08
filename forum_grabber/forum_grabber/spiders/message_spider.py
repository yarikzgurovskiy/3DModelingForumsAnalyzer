import scrapy


class MessageSpider(scrapy.Spider):
    name = "messages"
    start_urls = [
        'http://polycount.com/discussion/199203/shadow-of-the-tomb-raider',
        'http://polycount.com/discussion/200381/choosing-gift-for-3d-artist'
    ]

    def parse(self, response):
        for message in response.css("div.Item-Inner"):
            yield {
                'text': message.css("div.Message::text").extract_first(),
                'author': message.css("a.Username::text").extract_first(),
                'date': message.css("time::attr(datetime)").extract_first()
            }

        next_page_url = response.css("a.Next::attr(href)").extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))
