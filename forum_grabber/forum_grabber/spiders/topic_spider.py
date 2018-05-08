import scrapy


class TopicSpider(scrapy.Spider):
    name = "topics"
    start_urls = ["http://polycount.com/categories/general-discussion"]

    def parse(self, response):
        for topic in response.css("tr.Item"):
            yield {
                'id': str(topic.css("tr.Item::attr(id)").extract_first()).split('_')[-1],
                'name': str(topic.css("a.EntryLink > h3::text").extract()[1]).strip(),
                'url': topic.css("a.EntryLink::attr(href)").extract_first()
            }

        next_page_url = response.css("a.ext::attr(href)").extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))
