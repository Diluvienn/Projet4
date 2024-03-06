import datetime


def validate_date_format(date_string: str) -> bool:
    try:
        datetime.datetime.strptime(date_string, '%d-%m-%Y')
        return True
    except ValueError:
        return False