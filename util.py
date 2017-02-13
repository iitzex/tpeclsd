from datetime import date, timedelta

def getday():
    fmt = "%y%m%d"
    today = date.today().strftime(fmt)

    return today

def getnextday():
    fmt = "%y%m%d"
    _today = date.today()
    _tomorrow = _today + timedelta(days=1)
    tomorrow = _tomorrow.strftime(fmt)

    return tomorrow


if __name__ == "__main__":
    print getnextday()