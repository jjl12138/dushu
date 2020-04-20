# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DushuItem(scrapy.Item):

    # define the fields for your item here like:
    src = scrapy.Field()  # 发布作者
    alt = scrapy.Field()  # 作者博客主页链接
    author = scrapy.Field()  # 发布时间
