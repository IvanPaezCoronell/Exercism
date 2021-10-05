import datetime


def add(moment):
    gigasecund = datetime.timedelta(seconds=10**9)
    return moment + gigasecund
