# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from openpyxl import Workbook
import json
import xlwt
import pandas as pd
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BaiduPipeline:

    def __init__(self):
        self.wb = Workbook()
        self.ws = self.wb.active
        self.ws.append(['Search Request', 'Detailed url', 'Title', 'Source', 'Publish Time', 'Introduction'])
 
    def process_item(self, item, spider):
        # line = [item['subject'], item['url'], item['title'], item['source'], item['publish_time'], item['brief']]
        if ("京东" in item['brief'] or "品牌" in item['brief'] or "发货" in item['brief'] or "图片" in item['brief']):
        # if those Chinese keywords are in the brief, then the data will not be saved ("京东" is the name for something like "Chinese Amazon", "品牌" means "brand", "发货" means "delivery", "图片" means "picture)
            line = []
            self.ws.append(line)
            self.wb.save('BaiduResult.xlsx')
        else:
            line = [item['subject'], item['url'], item['title'], item['source'], item['publish_time'], item['brief']]
            self.ws.append(line)
            self.wb.save('BaiduResult.xlsx')
        




    # Save data as .json format

    # def __init__(self):
    #     self.f = open("tencent.json", "w")

    # def process_item(self, item, spider):
    #     content = json.dumps(dict(item), ensure_ascii = False) + ",\n"
    #     self.f.write(content)
        




    # Save data as .xlsx format (bad attempt)

    # def close_spider(self, spider):
    #     self.f.close()

    # def __init__(self):
        
    #     self.f = open("百度查询.xlsx", "w")

    # def process_item(self, item, spider):
    #     print(list(item))
    #     pf = pd.DataFrame(list(item))
    #     order = ['subject','url','title','source','publish_time', 'brief']
    #     pf = pf[order]
    #     columns_map = {
    #         'subject':'Search Request',
    #         'url':'Detailed url',
    #         'title':'Title',
    #         'source':'Source',
    #         'publish_time':'Publish Time',
    #         'brief':'Introduction'
    #     }
    #     pf.rename(columns = columns_map,inplace = True)
    #     file_path = pd.ExcelWriter('name.xlsx')
    #     pf.fillna(' ',inplace = True)
    #     pf.to_excel(file_path,encoding = 'utf-8',index = False)
    #     file_path.save()
    
    # def close_spider(self, spider):
    #     self.f.close()
    


    # def Excel(self):

    #     with open(r'/Users/alexyang/爬虫/Baidu/百度查询.json','r',encoding='UTF-8')as j:
    #         json_data = json.load(j)
    #         js = pd.DataFrame(json_data)
    #     js.to_excel(r'/Users/alexyang/爬虫/Baidu/百度查询结果.xlsx', index=False)