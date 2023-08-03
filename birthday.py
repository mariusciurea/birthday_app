import datetime


def format_date(date: str) -> datetime.datetime:
    today = datetime.date.today()
    list_date = date.split('-')
    return datetime.datetime.fromisoformat(f"{today.year}-{list_date[1]}-{list_date[0]}")

def get_weekday(date: datetime.datetime) -> str:
    pass


def time_delta(date1: datetime.datetime, date2: datetime.datetime) -> datetime.timedelta:
    pass


if __name__ == '__main__':
    bday = input('Enter your b-day [day-month; 03-08]: ')
    bday = format_date(bday)
    print(bday)
