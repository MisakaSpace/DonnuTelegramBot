import datetime

from bot.config import DAYS_NAME, PAIR_TIME


def get_start_week(date):
    start = date - datetime.timedelta(days=date.isoweekday() - 1)
    return start


def get_day_name(date):
    return DAYS_NAME[date.isoweekday() - 1]


def get_pair_time(number):
    return '{} - {}'.format(*PAIR_TIME[number - 1])


def get_pair_status(number):
    start, end = PAIR_TIME[number - 1]
    start = datetime.datetime.strptime(start, '%H:%M').time()
    end = datetime.datetime.strptime(end, '%H:%M').time()

    now = datetime.datetime.now().time()

    if end < now:
        return '✔️'
    if start < now < end:
        return "➖"
    return '✖️'


def get_next_day_by_number(day_number):
    today = datetime.date.today()
    delta = datetime.timedelta(days=7)
    week_start = get_start_week(today) if today.isoweekday() <= day_number else get_start_week(today + delta)
    return week_start + datetime.timedelta(days=day_number-1)


def find_day(text: str):
    text = text.lower()
    today = datetime.date.today()
    if "понеділок" in text:
        return get_next_day_by_number(1)
    elif "вівторок" in text:
        return get_next_day_by_number(2)
    elif "середа" in text or "середу" in text:
        return get_next_day_by_number(3)
    elif "четвер" in text:
        return get_next_day_by_number(4)
    elif "п'ятниця" in text or "п'ятницю" in text:
        return get_next_day_by_number(5)
    elif "субота" in text or "суботу" in text:
        return get_next_day_by_number(6)
    elif "субота" in text or "суботу" in text:
        return get_next_day_by_number(7)
    elif "сьогодні" in text:
        return today
    elif "завтра" in text:
        return today + datetime.timedelta(days=1)
    elif "післязавтра" in text:
        return today + datetime.timedelta(days=2)