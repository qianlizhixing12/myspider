import scrapy
from myscrapy.items import GaokaoSchoolItem


class GaokaoschoolSpider(scrapy.Spider):
    name = 'gaokaoschool'
    allowed_domains = ['gaokao.chsi.com.cn']
    custom_settings = {
        'ITEM_PIPELINES': {
            'myscrapy.pipelines.GaokaoSchoolPipeline': 300
        },
    }
    start_urls = ['https://gaokao.chsi.com.cn/sch/search--ss-on,searchType-1,option-qg,start-0.dhtml']

    def parse(self, response):
        select = scrapy.Selector(response=response)
        # pages = select.xpath('//ul[@class="ch-page clearfix"]/li/a/text()')[-1].extract()
        pages = select.css('ul.ch-page li.lip a::text')[-1].extract()
        for page in range(int(pages)):
            url = f'https://gaokao.chsi.com.cn/sch/search--ss-on,searchType-1,option-qg,start-{20*page}.dhtml'
            yield scrapy.Request(url=url, callback=self.parse_item, dont_filter=True)

    def parse_item(self, response):
        select = scrapy.Selector(response=response)
        for info in select.css('table.ch-table tr'):
            if info.css('td'):
                item = GaokaoSchoolItem()
                # name = info.xpath('td[1]/a/text()').get()
                name = info.css('td:nth-child(1) a::text').get()
                city = info.css('td:nth-child(2)::text').get()
                dep = info.css('td:nth-child(3)::text').get()
                style = info.css('td:nth-child(4)::text').get()
                level = info.css('td:nth-child(5)::text').get()
                star = info.css('td:nth-child(9) a::text').get()
                item['name'] = name.strip() if name else '*'
                item['city'] = city.strip() if city else '*'
                item['dep'] = dep.strip() if dep else '*'
                item['style'] = style.strip() if style else '*'
                item['level'] = level.strip() if level else '*'
                item['star'] = star.strip() if star else '*'
                yield item
