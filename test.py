# import scrapy
# from scrapy.crawler import CrawlerProcess
#


# from forum_grabber.forum_grabber.spiders.message_spider import MessageSpider
# from .topic_spider import TopicSpider
#
# process = CrawlerProcess({
#     'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0;)'
# })
# process.crawl(TopicSpider)
# process.start()



# from twisted.internet import reactor
# import scrapy
# from scrapy.crawler import CrawlerRunner
# from scrapy.utils.log import configure_logging
#
#
# configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
# runner = CrawlerRunner()
#
# d = runner.crawl(TopicSpider)
# d.addBoth(lambda _: reactor.stop())
# reactor.run()  # the script will block here until the crawling is finished


# from scrapy.crawler import CrawlerProcess
# from scrapy.utils.project import get_project_settings
#
# process = CrawlerProcess(get_project_settings())
#
# # 'followall' is the name of one of the spiders of the project.
# process.crawl('followall', domain='scrapinghub.com')
# process.start() # the script will block here until the crawling is finished

#
# class Command(ScrapyCommand):
#
#     requires_project = True
#     excludes = ['TopicSpider']
#
#     def syntax(self):
#         return '[options]'
#
#     def short_desc(self):
#         return 'Runs all of the spiders'
#
#     def run(self, args, opts):
#         settings = get_project_settings()
#         crawler_process = CrawlerProcess(settings)
#         for spider_name in crawler_process.spider_loader.list():
#             if spider_name in self.excludes:
#                 continue
#             spider_cls = crawler_process.spider_loader.load(spider_name)
#             crawler_process.crawl(spider_cls)
#         crawler_process.start()
#
#
# cm = Command()
# cm.run()
