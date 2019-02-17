# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv
from scrapy import cmdline

class TutorialPipeline(object):
    def process_item(self, item, spider):
        return item


class DetailPipeline(object):
    path = "C:\\Users\\Yuriko\\Desktop\\origin.csv"

    def __init__(self):
        self.file = open(self.path, 'a', newline='')
        self.writer = csv.writer(self.file)

    def process_item(self, item, spider):
        line = [item['location_depart'], item['location_area'], item['district'],
                item['price_total'], item['price_each'], item['deal_period'], item['date'],
                item['room_style'], item['cons_area'], item['inside_area'], item['room_vers'],
                item['desc_situation'], item['room_etage'], item['room_cate'],
                item['cons_year'], item['etage_room_rate'],  item['warm_style']]
        self.writer.writerow(line)

    def spider_closed(self, spider):
        self.file.close()
        cmdline.execute("scrapy crawl lianjia".split())
