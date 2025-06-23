import pytz
from datetime import datetime, time as dtime
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from plugins.auto_redeem_codes import post_daily_redeem_codes

scheduler = AsyncIOScheduler()


def start_auto_redeem_scheduler(bot, time_of_post):
    hour, minute = map(int, time_of_post.split(":"))
    ist = pytz.timezone("Asia/Kolkata")
    now = datetime.now(ist)
    target_time = datetime.combine(now.date(), dtime(hour, minute))
    utc_time = ist.localize(target_time).astimezone(pytz.utc)

    scheduler.add_job(post_daily_redeem_codes, trigger='cron', hour=utc_time.hour, minute=utc_time.minute, args=[bot])
    scheduler.start()
  
