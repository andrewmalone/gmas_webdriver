from datetime import datetime, timedelta
import random


def random_date(start="1/1/08", end="1/1/14", fmt="%m/%d/%y"):
    sd = datetime.strptime(start, fmt)
    ed = datetime.strptime(end, fmt)
    dt = sd + timedelta(days=random.randint(0, (ed - sd).days))
    return datetime.strftime(dt, fmt)
