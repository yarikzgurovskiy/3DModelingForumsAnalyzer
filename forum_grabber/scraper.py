from scrapy.crawler import CrawlerProcess
from forum_grabber.forum_grabber.spiders.message_spider import MessageSpider
from forum_grabber.forum_grabber.spiders.topic_spider import TopicSpider
from scrapy.utils.project import get_project_settings


class Scraper:
    def __init__(self):
        self.__process = CrawlerProcess(get_project_settings())

    def scrap_messages(self):
        self.__process.crawl(MessageSpider)

    def scrap_topics(self):
        self.__process.crawl(TopicSpider)

    def run(self):
        self.__process.start()

