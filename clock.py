#Python scheduler on Heroku https://devcenter.heroku.com/articles/clock-processes-python

#Spider scheduler https://stackoverflow.com/questions/61040267/unable-to-run-scrapy-spider-with-apscheduler

from apscheduler.schedulers.blocking import BlockingScheduler
from scrapy_job_it.spiders.bdcrawler import BDcrawlerSpider
from scrapy_job_it.spiders.jjcrawler import JjcrawlerSpider
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess
from apscheduler.schedulers.twisted import TwistedScheduler
#working version for BDcrawlerSpider
process = CrawlerProcess(get_project_settings())
process.crawl(BDcrawlerSpider)
process.start()
scheduler = TwistedScheduler()
scheduler.add_job(process.crawl, 'cron', args=[BDcrawlerSpider], hour=20, minute=50)
scheduler.start()
process.start(False)

#version for 2 spiders scheduled in different houres
# def run_spider(spider, hour):
#     process = CrawlerProcess(get_project_settings())
#     process.crawl(spider)
#     process.start()
#     scheduler = TwistedScheduler()
#     scheduler.add_job(process.crawl, 'cron', args=[spider], hour=hour, minute=50)
#     scheduler.start()
#     process.start(False)
#
#
# run_spider(BDcrawlerSpider, 20)
# run_spider(JjcrawlerSpider, 10)

#run scheduler - tutorial
# sched = BlockingScheduler()
#
# @sched.scheduled_job('interval', minutes=3)
# def timed_job():
#     print('This job is run every three minutes.')
#
# @sched.scheduled_job('cron', day_of_week='mon-fri', hour=19)
# def scheduled_job():
#     print('This job is run every weekday at 5pm.')
#
# sched.start()