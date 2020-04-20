# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class DsSpider(CrawlSpider):
    name = 'ds'
    allowed_domains = ['www.dushu.com']
    start_urls = ['https://www.dushu.com/book/1163_1.html']
    rules = (
        Rule(LinkExtractor(allow=r'/book/1163_\d+.html'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        div_list = response.xpath('//div[@class="bookslist"]/ul/li/div')
        for div in div_list:
            item['src'] = div.xpath('./div/a/img/@data-original').extract_first()
            item['alt'] = div.xpath('./div/a/img/@alt').extract_first()
            item['author'] = div.xpath('./p[1]/a[1]/text()|./p[1]/text()').extract_first()
            yield item
