# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from .items import ForumMessageItem, ForumTopicItem
from .database import Database


class ForumGrabberPipeline(object):
    def __init__(self):
        self.__db = Database()

    def process_item(self, item, spider):
        if isinstance(item, ForumTopicItem):
            self.__db.save_topic(item.__dict__['_values'])
        elif isinstance(item, ForumMessageItem):
            self.__db.save_message(item.__dict__['_values'])
        return item

    def close_spider(self, spider):
        self.__db.close()
