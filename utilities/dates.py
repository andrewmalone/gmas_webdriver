from datetime import datetime, timedelta
import random


def random_date(start="1/1/08", end="1/1/14", fmt="%m/%d/%y"):
    sd = datetime.strptime(start, fmt)
    ed = datetime.strptime(end, fmt)
    dt = sd + timedelta(days=random.randint(0, (ed - sd).days))
    return datetime.strftime(dt, fmt)


def budget_period_dates(start, end, fmt="%m-%d-%Y"):
    """
    For any project start/end dates, returns a list of tuples representing the dates of each budget period.
    Assumes year long budget periods
    Returns the start/end dates if end - start is less than 1 year
    """
    sd = datetime.strptime(start, fmt)
    ed = datetime.strptime(end, fmt)
    diff = (ed + timedelta(days=1)) - sd
    # http://stackoverflow.com/questions/4436957/pythonic-difference-between-two-dates-in-years
    diff_years = (diff.days + diff.seconds/86400.0)/365.2425
    if diff_years < .95:
        return (start, end)
    periods = int(round(diff_years))
    period_dates = []
    for i in range(periods):
        start = datetime.strftime(datetime(sd.year + i, sd.month, sd.day), fmt)
        end = datetime.strftime(datetime(sd.year + (i + 1), sd.month, sd.day) - timedelta(days=1), fmt)
        period_dates.append((start, end))
    return period_dates


if __name__ == "__main__":
    pass
