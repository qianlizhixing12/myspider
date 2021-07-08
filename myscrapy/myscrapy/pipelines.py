# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface
from scrapy.utils.project import get_project_settings
import sqlite3
import datetime


class GaokaoSchoolPipeline:

    def process_item(self, item, spider):
        self.items.append(item)
        return item

    def open_spider(self, spider):
        self.items = []
        # , 字符编码报错
        config = get_project_settings().get('SQLITE_CONFIG')
        self.conn = sqlite3.connect(**config)
        self.insert = self.conn.cursor()

    def close_spider(self, spider):
        try:
            updatedt = str(datetime.datetime.now().date())
            datas = ((item['name'], item['city'], item['dep'], item['style'], item['level'], item['star'], updatedt) for item in self.items)
            data = ('gaokao', 'school', updatedt)
            # 执行批量插入
            # sqlite使用?占位符，mysql使用%s占位符
            self.insert.executemany('insert into gaokao_school (name, city, dep, style, level, star, updatedt) values (?, ?, ?, ?, ?, ?, ?)', datas)
            self.insert.execute('insert into scrapy_update_info (web, item, updatedt) values (?, ?, ?)', data)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        finally:
            self.insert.close()
            self.conn.close()
