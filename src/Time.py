from datetime import datetime
import pytz


def am_time_now():
    fmt = "%Y-%m-%d %H:%M:%S"
    now_utc = datetime.now(pytz.timezone('UTC'))
    now_am = now_utc.astimezone(pytz.timezone('Asia/Yerevan'))
    return str(now_am.strftime(fmt))


def user_time_compare(user_date):

    now_time = datetime.now()
    now_local = pytz.timezone(str(user_date))
    ny = pytz.timezone('America/New_York')
    now_ny = ny.localize(now_time)
    now_l = now_local.localize(now_time)

    return int(now_ny.strftime('%z')[:3]) - int(now_l.strftime('%z')[:3])
