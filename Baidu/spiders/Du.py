import scrapy
import configparser
import sys
import os

# Get the absolute path of the current script
script_path = os.path.abspath(__file__)
# Get the directory of the script
script_dir = os.path.split(script_path)[0]
# Get the root directory of the project
root_dir = os.path.split(script_dir)[0]

# Add the root directory of the project to sys.path
sys.path.append(root_dir)

# Now Python can find items.py, so you can import it
from items import BaiduItem


def get_baidu_search_url(keyword, page):
    urltmp = "https://www.baidu.com/s?wd=%s&tn=news&pn=%d"
    start = 10*(page - 1)
    url = urltmp % (keyword, start)
    return url
    pass

class GafBaiduSpider(scrapy.Spider):
    name = 'Du'
    
    config = configparser.ConfigParser()
    def __init__(self, name=None, **kwargs):
        super().__init__(name=name, **kwargs)
        self.config.read('config_baidu.ini', encoding='utf-8')
        self.keywords = []
        for i in range(int(self.config['set']['maxnum'])):
            keywordid = 'keyword%d' % (i+1)
            ckeyword = self.config[keywordid]
            self.keywords.append({
                'id': keywordid,
                'keyword': ckeyword['keyword'],
                'pages': int(ckeyword['pages']),
                'page': int(ckeyword['page']),
            })

    def start_requests(self):
        for kws in self.keywords:
            if kws['page'] <= kws['pages']:
                url = get_baidu_search_url(kws['keyword'], kws['page'])
                yield scrapy.Request(url= url, callback= self.parse, meta= kws)


    def parse(self, response):
        kws = response.meta
        keyword = kws['keyword']
        urls = response.xpath('//div[@id="content_left"]//div[contains(@class,"result-op")]')

        for i in range(len(urls)):
            url = urls[i]
            item = BaiduItem()
            item['subject'] = keyword
            item['url'] = url.xpath("@mu")[0].extract()
            item['title'] = "".join(url.xpath('.//a[@href="%s"]//text()' % item['url']).extract())
            # 来源和日期
            item['source'] = ""
            item['publish_time'] = ""
            source_date = url.xpath(".//div[@class='news-source_Xj4Dv']/span/text()").extract()
            if len(source_date) == 1:
                date = source_date[0]
                if date.find("月") >0 and date.find("日") > 0: # "月" means "month", "日" means "day"
                    item['publish_time'] = date
                else:
                    item['source'] = date
            elif len(source_date) == 2:
                item['publish_time'] = source_date[1]
                item['source'] = source_date[0]
            item['brief'] = "".join(url.xpath('.//span[contains(@class,"c-font-normal") and contains(@class,"c-color-text")]//text()').extract())

            yield item

        # 查找下一页
        page = kws['page']
        pages = kws['pages']
        if page < pages:
            page += 1
            url = get_baidu_search_url(keyword, page)
            print("Keyword: [%s], currently crawling page %d, total pages: %d" % (keyword, page, pages))


            self.config[kws['id']]['page'] = str(page)
            with open('config_baidu.ini', 'w', encoding='utf-8') as c:
                self.config.write(c)

            kws['page'] = page
            yield scrapy.Request(url, meta=kws, callback=self.parse)
        pass
