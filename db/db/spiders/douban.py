# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from db.items import DbItem
import time
import re

class DoubanSpider(CrawlSpider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/']
    rules = (
        Rule(LinkExtractor(allow=r'/subject/[0-9]+/*$'or r'/subject/[0-9]+/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = DbItem()

        item['url'] = response.url

        item['name'] = response.xpath('//*[@id="content"]/h1/span[1]/text()').extract()

        item['kind'] = self.get_kind(response)

        item['grade'] = response.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()').extract()

        item['describe'] = self.describe_handle(response)

        # item['comments'] = self.comments_item(response)

        return item


    # def comments_item(self, response):
    #     comments = response.xpath('//div[@class="review-list"]/div/div/div[@class="main-bd"]/div[1]/div[@class="short-content"]text()[1]')
    #     return comments

    def get_kind(self, response):
        kinds = response.xpath('//*[@id="info"]/span[@property="v:genre"]/text()').extract()
        kind = ""
        for i in kinds:
            kind += i
            kind += " "
        return kind

    def describe_handle(self, response):
        des = response.xpath('//*[@id="link-report"]/span/text()').extract()
        esp = "".join(des)
        asp = re.sub('\s', "", esp)
        return asp
