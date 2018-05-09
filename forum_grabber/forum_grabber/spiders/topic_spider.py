import scrapy

from ..items import ForumTopicItem


class TopicSpider(scrapy.Spider):
    name = "topics"

    def start_requests(self):
        urls = [
            'http://polycount.com/categories/general-discussion/p' + str(i) for i in range(2, 3)
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for topic in response.css("tr.Item"):
            item = ForumTopicItem()
            item['name'] = str(topic.css("a.EntryLink > h3::text").extract()[1]).strip()
            item['url'] = str(topic.css("a.EntryLink::attr(href)").extract_first()).strip()
            yield item

        next_page_url = response.css("a.ext::attr(href)").extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))
