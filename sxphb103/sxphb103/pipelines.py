# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class Sxphb103Pipeline(object):
    def process_item(self, item, spider):
        # print("================")
        # print(item)
        print('已完成写入1条数据')
        # print(item['title'])
        # print(item['time'])
        # print(item['number'])
        # print("================")
        return item
