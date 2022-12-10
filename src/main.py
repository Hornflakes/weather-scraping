from conf import *
from utils import *
import requests
import bs4
import pandas as pd
import datetime as dt
from dateutil.relativedelta import relativedelta


existingDf = pd.read_excel(io=EXCEL_FILE_NAME, sheet_name=EXCEL_SHEET_NAME)

dateCol = existingDf.columns[DATE_COL_EXCEL_INDEX]
lastDayRow = existingDf[dateCol].last_valid_index()

lastDayStr = existingDf[dateCol][lastDayRow]
firstDayDate = dt.datetime.strptime(lastDayStr, "%d.%m.%Y") + dt.timedelta(days=1)
todayDate = dt.date.today()

firstMonthDate = formatDateForReq(firstDayDate)
presentMonthDate = formatDateForReq(todayDate)
firstDayDict = dateToDict(firstDayDate)

dataPointKeys = [
    "date",
    "minTemperature",
    "maxTemperature",
    "maxSustainedWind",
    "maxGustWind",
    "rainfall",
    "snowDepth",
    "description",
]
data = {key: [] for key in dataPointKeys}

monthDate = firstMonthDate
while monthDate <= presentMonthDate:
    monthDict = dateToDict(monthDate)
    url = "https://freemeteo.ro/vremea/bucuroaia/istoric/istoric-lunar/?gid=683499&station=4621&month={}&year={}&language=romanian&country=romania".format(
        monthDict["month"], monthDict["year"]
    )
    response = requests.get(url)

    soup = bs4.BeautifulSoup(response.text, "lxml")
    if monthDate is firstMonthDate:
        dailySoup = soup.find_all(
            lambda tag: tag.name == "tr"
            and "data-day" in tag.attrs
            and int(tag["data-day"]) > int(firstDayDict["day"]) - 1
        )
    else:
        dailySoup = soup.find_all("tr", attrs={"data-day": True})

    for daySoup in dailySoup:
        data["date"].append(daySoup.find_all("td")[0].string)
        data["maxSustainedWind"].append(daySoup.find_all("td")[3].string)
        data["maxGustWind"].append(daySoup.find_all("td")[4].string)
        data["rainfall"].append(daySoup.find_all("td")[5].string)
        data["snowDepth"].append(daySoup.find_all("td")[6].string)
        data["description"].append(daySoup.find_all("td")[9].contents[0])

        minTemperature = daySoup.find_all("td")[1].string
        if minTemperature[0] == "-":
            data["minTemperature"].append(minTemperature + "'")
        else:
            data["minTemperature"].append(minTemperature)

        maxTemperature = daySoup.find_all("td")[2].string
        if maxTemperature[0] == "-":
            data["maxTemperature"].append(maxTemperature + "'")
        else:
            data["maxTemperature"].append(maxTemperature)

    monthDate = monthDate + relativedelta(months=+1)

with pd.ExcelWriter(
    EXCEL_FILE_NAME, engine="openpyxl", mode="a", if_sheet_exists="overlay"
) as xlWriter:
    df = pd.DataFrame(data)
    df.to_excel(
        excel_writer=xlWriter,
        sheet_name=EXCEL_SHEET_NAME,
        index=False,
        header=False,
        startcol=DATE_COL_EXCEL_INDEX,
        startrow=lastDayRow + 2,
    )
