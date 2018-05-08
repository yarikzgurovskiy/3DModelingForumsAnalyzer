# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from .items import ForumMessageItem, ForumTopicItem
from .database import Database


class ForumGrabberPipeline(object):

    def process_item(self, item, spider):
        if isinstance(item, ForumTopicItem):
            self.db.save_topic(item.__dict__['_values'])
        elif isinstance(item, ForumMessageItem):
            self.db.save_message(item.__dict__['_values'])
        return item

    def open_spider(self, spider):
        self.db = Database()

    def close_spider(self, spider):
        self.db.close()
