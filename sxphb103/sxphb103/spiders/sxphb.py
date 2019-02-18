# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urlencode
from sxphb103.items import Sxphb103Item,ProvinceItem
import json
import sys
import time
class SxphbSpider(scrapy.Spider):


    name = 'sxphb'
    # allowed_domains = ['103.42.76.240']


    # print(full_urls)
    # start_urls = [full_urls+str[1]]
    #请求省份数据
    #urls = ['http://103.42.76.240/phb/data/province_data.php']

    def start_requests(self):
        # baseurl = 'http://103.42.76.240/phb/data/'
        baseurl = 'http://103.42.76.240/phb/data/province_data.php'

        print('模式1：全国数据')
        print('模式2：省份数据')
        b = int(input('请输入'))
        if b == 1:
            print('正在解析全国省份,请稍后')
            yield scrapy.Request(baseurl,self.parse)
        elif b == 2:
            print('只能获取一个省份的数据!')
            sys.exit('功能完善中......................................')
        else:
            sys.exit('退出')
    #解析出省份
    def parse(self,response):
        #判断要自然人还是法人还是全都要
        print('1.自然人')
        print('2.法人')
        print('3.全都要')
        baseurl = 'http://103.42.76.240/phb/data/'
        d = {
            '自然人': 'country_person_money.php?',
            '法人': 'country_unit_money.php?'
        }
        full_urls = []
        full_urls.append(baseurl + d['自然人'])
        full_urls.append(baseurl + d['法人'])
        c = int(input('请按数字:\n'))

        #逻辑判断,可优化.
        if c == 1:
            print('进入自然人模式')
            result = json.loads(response.text)
        #请求自然人
            for provincename in result.keys():
                data = {'order': 'desc', 'province': provincename}
                for page in range(0, 11):
                    data['page'] = page
                    params = urlencode(data)
                    url1 = full_urls[0] + params
                    print(url1)
                    #回调处理明文json
                    yield scrapy.Request(url1, self.parse_page, dont_filter=True)
        elif c == 2:
            print('进入法人模式')
        #请求法人
            result = json.loads(response.text)
            for provincename in result.keys():
                data = {'order': 'desc', 'province': provincename}
                for page in range(0, 11):
                    data['page'] = page
                    params = urlencode(data)
                    url1 = full_urls[1] + params
                    print(url1)
                    # input('111')
                    #         yield scrapy.Request(url,self.parse2)
                    yield scrapy.Request(url1, self.parse_page, dont_filter=True)
        elif c == 3:
            print('进入贪婪模式')
            print('程序准备中,异步32线程即将开启')
            time.sleep(5)
        # 请求全国
            result = json.loads(response.text)
            for provincename in result.keys():
                data = {'order': 'desc', 'province': provincename}
                for page in range(0, 11):
                    data['page'] = page
                    params = urlencode(data)
                    url1 = full_urls[0] + params
                    url2 = full_urls[1] + params
                    print('自然人url 200 success')
                    print(url1)
                    print('==============')
                    print('法人url 200 success')
                    print(url2)
                    yield scrapy.Request(url1, self.parse_page, dont_filter=True)
                    yield scrapy.Request(url2, self.parse_page, dont_filter=True)
        else:
            sys.exit('输入有误,退出')
    #解析明文json数据
    def parse_page(self, response):
        result = json.loads(response.text)
        for i in result:
            item = Sxphb103Item()
            item['name'] = i.get('iname')
            item['money'] = i.get('money')
            item['province'] = i.get('provinceName')
            yield item
