import sys
import os
from apscheduler.schedulers.twisted import TwistedScheduler
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess
from myscrapy.spiders.gaokaoschool import GaokaoSchoolSpider

# 获取当前脚本路径
dirpath = os.path.dirname(os.path.abspath(__file__))
#运行文件绝对路径
print(os.path.abspath(__file__))
#运行文件父路径
print(dirpath)
# 添加环境变量
sys.path.append(dirpath)
#切换工作目录
os.chdir(dirpath)

process = CrawlerProcess(get_project_settings())
# 创建schedulers
sched = TwistedScheduler()
# 每天三点准时启动
sched.add_job(process.crawl,
              'cron',
              hour=18,
              minute=19,
              args=[GaokaoSchoolSpider])
sched.start()
process.start(False)  # Do not stop reactor after spider closes
