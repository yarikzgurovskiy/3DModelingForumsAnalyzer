import scrapy

from ..database import Database
from ..items import ForumMessageItem


class MessageSpider(scrapy.Spider):
    name = "messages"
    custom_settings = {
        'ITEM_PIPELINES': {
            'forum_grabber.forum_grabber.pipelines.ForumGrabberPipeline': 400
        }
    }

    def start_requests(self):
        db = Database()
        urls = [topic['url'] for topic in db.get_topics()]
        db.close()
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for message in response.css("div.Item-Inner"):
            item = ForumMessageItem()
            item['text'] = message.css("div.Message::text").extract_first()
            item['author'] = message.css("a.Username::text").extract_first()
            item['date'] = message.css("time::attr(datetime)").extract_first()
            item['topic_url'] = str(response)[5:len(str(response)) - 1]

            yield item

        next_page_url = response.css("a.Next::attr(href)").extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))
