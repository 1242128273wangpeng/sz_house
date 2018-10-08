# -*- coding: utf-8 -*-
import scrapy
import io
import requests
from urllib import urlretrieve
import json
from lxml import etree
import chardet
import sys

class SzhouseSpider(scrapy.Spider):
    name = 'SzHouse'
    allowed_domains = ['sz.lianjia.com']
    start_urls = ['https://sz.lianjia.com/ershoufang/guangmingxinqu/']

    def parse(self, response):
        title = response.css("title::text").extract()
        print title[0].encode('utf-8')
        content = response.body
        html = etree.HTML(content)
        result = html.xpath('/html/body//div[@class="info clear"]')
        with open("./house.txt","a+") as f:
            for i in result:
                title = i.xpath('./div[@class="title"]/a/text()')[0]
                desc = i.xpath('./div[@class="address"]/div/text()')[0]
                address = i.xpath('./div[@class="address"]/div/a/text()')[0]
                flood = i.xpath('./div[@class="flood"]/div/a/text()')[0]
                position = i.xpath('./div[@class="flood"]/div/text()')[0]
                follow = i.xpath('./div[@class="followInfo"]/text()')[0]
                tags = ""
                listTags = i.xpath('./div[@class="tag"]/span/text()')
                for j in listTags:
                    tags+=(j+",")
                total = i.xpath('./div[@class="priceInfo"]/div[@class="totalPrice"]/span/text()')[0]
                unit = i.xpath('./div[@class="priceInfo"]/div[@class="unitPrice"]/span/text()')[0]
                log = ((flood.encode('utf-8'))+" "+(address.encode('utf-8'))+" "+(position.encode('utf-8'))+" 总价:"+(total.encode('utf-8'))+" "+(unit.encode('utf-8'))+" "+(tags.encode('utf-8'))+" "+(desc.encode('utf-8'))+" "+(title.encode('utf-8'))+"\n")
                print log
                f.write(log)
        
    
