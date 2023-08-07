import datetime


def format_date(date: str) -> datetime.date:
    today = datetime.date.today()
    list_date = date.split('-')
    return datetime.date.fromisoformat(f"{today.year}-{list_date[1]}-{list_date[0]}")


def get_weekday(date: datetime.datetime) -> str:
    day_of_week = date.weekday()
    dict_week = {0: "Luni", 1: "Marti", 2: "Miercuri", 3: "Joi", 4: "Vineri", 5: "Sambata", 6:"Duminica"}
    return dict_week[day_of_week]


def time_delta(date1: datetime.date, date2: datetime.date) -> datetime.timedelta:
    diff = date1 - date2
    return diff


if __name__ == '__main__':
    bday = input('Enter your b-day [day-month; 03-08]: ')
    bday = format_date(bday)
    weekday = get_weekday(bday)
    print(weekday)
    date_1 = datetime.date.today()
    data = time_delta(date_1, bday)
    if data.days < 0:
        print(f"Ziua ta va fi peste {data.days} zile! Intr-o zi de{weekday} ")
    else:
        print(f"Ziua ta a fost acum {data.days} zile! Intr-o zi de {weekday}")
    print(data)
