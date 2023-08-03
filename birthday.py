import datetime


def format_date(date: str) -> datetime.datetime:
    pass


def get_weekday(date: datetime.datetime) -> str:
    pass


def time_delta(date1: datetime.datetime, date2: datetime.datetime) -> datetime.timedelta:
    pass


if __name__ == '__main__':
    bday = input('Enter your b-day [day-month; 03-08]: ')
    bday = format_date(bday)