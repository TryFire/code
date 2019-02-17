import scrapy
from scrapy.http import Request
import time


class LJSpider(scrapy.Spider):
    project_name = "LianjiaSpider for ZYL"
    name = "lianjia"
    base_url = "https://bj.lianjia.com"
    origin_url = "https://bj.lianjia.com/chengjiao/"
    start_urls = []
    total_num = 0
    #page = 105

    def start_requests(self):
        url = "https://bj.lianjia.com/chengjiao/dongcheng/"
        print(url)
        yield Request(url, callback=self.parse)

    def parse(self, response):
        #/html/body/div[3]/div[1]/dl[2]/dd/div/div[2]
        res = response.xpath('//div[@data-role=\'ershoufang\']/div[2]//a')[11:22:1]
        res = [res[0], res[2], res[10]]
        print(res)
        #del res[6]
        for sel in res:
            area_url = self.base_url + sel.xpath('@href').extract()[0]
            print(area_url)
            for i in range(1, 100):
                next_url = area_url + "pg" + str(i) + "/"
                yield scrapy.Request(next_url, callback=self.parse_detail_lien)

    def parse_detail_lien(self, response):
        for sel in response.xpath('//ul/li/div[@class=\'info\']/div[@class=\'title\']'):
            detail_url = sel.xpath('a/@href').extract()[0]
            print("try", detail_url)
            yield scrapy.Request(detail_url, callback=self.parse_detail)


            # print(self.project_name, "out")
            # for sel in response.xpath('//ul/li/div[@class=\'info\']/div[@class=\'title\']'):
            #     detail_url = sel.xpath('a/@href').extract()[0]
            #     print("try", detail_url)
            #     yield scrapy.Request(detail_url, callback=self.parse_detail)
            # /html/body/div[3]/div[1]/dl[2]/dd/div/div/a[1]
            # /html/body/div[3]/div[1]/dl[2]/dd/div/div/a[2]
            # /html/body/div[3]/div[1]/dl[2]/dd/div/div
            # //div[@data-role=\'ershoufang\']/div/a
            # print(self.project_name, "get page:", self.page)
            # time.sleep(1)
            # if self.page < 10:
            #     self.page = self.page + 1
            #     next_url = self.origin_url + "pg" + str(self.page) + "/"
            #     yield scrapy.Request(next_url, callback=self.parse)

            # print(self.project_name, "end------------------------------------")

    def parse_detail(self, response):
        self.total_num += 1
        print(self.project_name, "正在获取第", self.total_num, "条数据", "  get url:", response.url)
        wrapper = response.xpath('/html/body/div[4]')
        # 小区
        district = wrapper.xpath('div/text()').extract()[0].split(' ')[0]

        # 成交日期
        date = wrapper.xpath('div/span/text()').extract()[0][0:11]

        location = response.xpath('/html/body/section[1]/div[1]')

        # department 朝阳
        location_depart = location.xpath('a[3]/text()').extract()[0]

        # 大望路
        location_area = location.xpath('a[4]/text()').extract()[0]

        price = response.xpath('/html/body/section[1]/div[2]/div[2]')

        price_len = len(price.xpath('div[1]/span/i/text()').extract())
        if (price_len == 0):
            price_total = "no data"
            price_each = "no data"
            deal_period = "no data"
        else:
            price_total = price.xpath('div[1]/span/i/text()').extract()[0]

            price_each = price.xpath('div[1]/b/text()').extract()[0]

            deal_period = price.xpath('div[3]/span[2]/label/text()').extract()[0]

        base_attrs = response.xpath('//*[@id="introduction"]/div/div[1]/div[2]/ul')

        # 房屋户型
        room_style = base_attrs.xpath('li[1]/text()').extract()[0]

        # 所在楼层
        room_etage = base_attrs.xpath('li[2]/text()').extract()[0]

        # 建筑面积
        #
        cons_area = base_attrs.xpath('li[3]/text()').extract()[0]

        # 户型结构
        room_cate = base_attrs.xpath('li[4]/text()').extract()[0]
        #

        # 屋内面积
        inside_area = base_attrs.xpath('li[5]/text()').extract()[0]
        # //*[@id="introduction"]/div/div[1]/div[2]/ul/li[5]/text()

        # 房屋朝向
        room_vers = base_attrs.xpath('li[7]/text()').extract()[0]
        #

        # 建成年代
        cons_year = base_attrs.xpath('li[8]/text()').extract()[0]
        #

        # 装修情况
        desc_situation = base_attrs.xpath('li[9]/text()').extract()[0]
        #

        # 供暖方式
        warm_style = base_attrs.xpath('li[11]/text()').extract()[0]
        #

        # 梯户比例
        etage_room_rate = base_attrs.xpath('li[12]/text()').extract()[0]

        print(self.project_name, "获取第", self.total_num, "条数据success", "  get url:", response.url)

        item = DetailItem()
        item['district'] = district
        item['date'] = date
        item['location_depart'] = location_depart
        item['location_area'] = location_area
        item['price_total'] = price_total
        item['price_each'] = price_each
        item['deal_period'] = deal_period
        item['room_style'] = room_style
        item['room_etage'] = room_etage
        item['cons_area'] = cons_area
        item['room_cate'] = room_cate
        item['inside_area'] = inside_area
        item['room_vers'] = room_vers
        item['cons_year'] = cons_year
        item['desc_situation'] = desc_situation
        item['warm_style'] = warm_style
        item['etage_room_rate'] = etage_room_rate

        yield item


class DetailItem(scrapy.Item):
    district = scrapy.Field()
    date = scrapy.Field()
    location_depart = scrapy.Field()
    location_area = scrapy.Field()
    price_total = scrapy.Field()
    price_each = scrapy.Field()
    deal_period = scrapy.Field()
    room_style = scrapy.Field()
    room_etage = scrapy.Field()
    cons_area = scrapy.Field()
    room_cate = scrapy.Field()
    inside_area = scrapy.Field()
    room_vers = scrapy.Field()
    cons_year = scrapy.Field()
    desc_situation = scrapy.Field()
    warm_style = scrapy.Field()
    etage_room_rate = scrapy.Field()
