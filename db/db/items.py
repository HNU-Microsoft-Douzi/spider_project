# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DbItem(scrapy.Item):

    #links
    url = scrapy.Field()

    id = scrapy.Field()
    #电影名称
    name = scrapy.Field()
    #电影的种类
    kind = scrapy.Field()
    #电影的评分
    grade = scrapy.Field()
    #电影的描述
    describe = scrapy.Field()
    #电影的评论
    # comments = scrapy.Field()