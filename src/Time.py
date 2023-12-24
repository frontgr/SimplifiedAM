from datetime import datetime
import pytz


def am_time_now():
    fmt = "%Y-%m-%d %H:%M:%S"
    now_utc = datetime.now(pytz.timezone('UTC'))
    now_am = now_utc.astimezone(pytz.timezone('Asia/Yerevan'))
    return str(now_am.strftime(fmt))


def user_time_compare():

    now_time = datetime.now()
    now_local = now_time.astimezone()
    ny = pytz.timezone('America/New_York')
    now_ny = ny.localize(now_time)

    localVsUtc = now_local.strftime('%z')
    utcVsNY = now_ny.strftime('%z')

    output = {'local time': str(now_local), 'NY time': str(now_ny), 'difference': ''}

    if localVsUtc[0:1] and utcVsNY[0:1] == '+':
        if int(localVsUtc[1:3]) > int(utcVsNY[1:3]):
            output['difference'] = "Local time is ahead of New York one on " + str(int(localVsUtc[1:3]) - int(utcVsNY[1:3]))
            return output
        else:
            output['difference'] = "New York time is ahead of local one on " + str(int(localVsUtc[1:3]) - int(utcVsNY[1:3]))
            return output
    else:
        if int(localVsUtc[1:3]) < int(utcVsNY[1:3]):
             output['difference'] = "Local time is ahead of New York one on " + str(int(localVsUtc[1:3]) + int(utcVsNY[1:3]))
             return output
        else:
             output['difference'] = "New York time is ahead of local one on " + str(int(localVsUtc[1:3]) + int(utcVsNY[1:3]))
             return output







