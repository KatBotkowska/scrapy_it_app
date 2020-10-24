#Python scheduler on Heroku https://devcenter.heroku.com/articles/clock-processes-python

from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=3)
def timed_job():
    print('This job is run every three minutes.')

@sched.scheduled_job('cron', day_of_week='mon-fri', hour=19:15)
def scheduled_job():
    print('This job is run every weekday at 5pm.')

sched.start()