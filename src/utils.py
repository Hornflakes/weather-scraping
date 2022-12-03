import datetime as dt


def formatDateForReq(date):
    dateStr = "01." + "{:%m.%Y}".format(date)
    return dt.datetime.strptime(dateStr, "%d.%m.%Y")


def dateToDict(date):
    dateDictKeys = ["day", "month", "year"]

    dateList = (date.strftime("%d.%m.%Y")).split(".")
    return {key: dateList[i] for i, key in enumerate(dateDictKeys)}
