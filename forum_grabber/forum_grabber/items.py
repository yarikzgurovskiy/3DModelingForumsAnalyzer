# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item


class ForumTopicItem(Item):
    name = Field()
    url = Field()


class ForumMessageItem(Item):
    text = Field()
    author = Field()
    date = Field()
    topic_url = Field()
