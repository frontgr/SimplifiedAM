from datetime import datetime
import pytz


def am_time_now():
    fmt = "%Y-%m-%d %H:%M:%S"
    now_utc = datetime.now(pytz.timezone('UTC'))
    now_am = now_utc.astimezone(pytz.timezone('Asia/Yerevan'))
    return str(now_am.strftime(fmt))


def user_time_compare(user_date):

    now_time = datetime.now()
    now_local = user_date
    ny = pytz.timezone('America/New_York')
    now_ny = ny.localize(now_time)

    localVsUtc = now_local.strftime('%z')
    utcVsNY = now_ny.strftime('%z')

    if localVsUtc[0:1] and utcVsNY[0:1] == '+':
        return '+' + str(abs(int(localVsUtc[1:3]) - int(utcVsNY[1:3])))
    else:
        return str(int(localVsUtc[0:3]) + int(utcVsNY[0:3]))
