#Python scheduler on Heroku https://devcenter.heroku.com/articles/clock-processes-python

#Spider scheduler https://stackoverflow.com/questions/61040267/unable-to-run-scrapy-spider-with-apscheduler

from apscheduler.schedulers.blocking import BlockingScheduler
from scrapy_job_it.spiders.bdcrawler import BDcrawlerSpider
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess
from apscheduler.schedulers.twisted import TwistedScheduler

process = CrawlerProcess(get_project_settings())
process.crawl(BDcrawlerSpider)
process.start()
scheduler = TwistedScheduler()
scheduler.add_job(process.crawl, 'cron', args=[BDcrawlerSpider], hour=20, minute=50)
scheduler.start()
process.start(False)

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