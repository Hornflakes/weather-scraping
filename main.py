import requests
import bs4
import pandas as pd
import datetime
from dateutil.relativedelta import relativedelta

dt = datetime


existingDf = pd.read_excel(io="weather-data.xlsx", sheet_name="Sheet1")
lastDayStr = existingDf["date"].iloc[-1]

firstDayDate = dt.datetime.strptime(lastDayStr, "%d.%m.%Y") + dt.timedelta(days=1)
todayDate = dt.date.today()

firstMonthStr = "01." + "{:%m.%Y}".format(firstDayDate)
presentMonthStr = "01." + "{:%m.%Y}".format(todayDate)
firstMonthDate = dt.datetime.strptime(firstMonthStr, "%d.%m.%Y")
presentMonthDate = dt.datetime.strptime(presentMonthStr, "%d.%m.%Y")

dateDictKeys = ["day", "month", "year"]
firstDayToAdd = (firstDayDate.strftime("%d.%m.%Y")).split(".")
firstDayToAdd = {key: firstDayToAdd[i] for i, key in enumerate(dateDictKeys)}

dataPointKeys = [
    "date",
    "minTemperature",
    "maxTemperature",
    "maxSustainedWind",
    "maxGustWind",
    "rainfall",
    "snowDepth",
    "barometricPressure",
    "description",
]
data = {key: [] for key in dataPointKeys}

monthDate = firstMonthDate
while monthDate <= presentMonthDate:
    monthToAdd = (monthDate.strftime("%d.%m.%Y")).split(".")
    monthToAdd = {key: monthToAdd[i] for i, key in enumerate(dateDictKeys)}

    url = "https://freemeteo.ro/vremea/bucuroaia/istoric/istoric-lunar/?gid=683499&station=4621&month={}&year={}&language=romanian&country=romania".format(
        monthToAdd["month"], monthToAdd["year"]
    )
    response = requests.get(url)

    soup = bs4.BeautifulSoup(response.text, "lxml")
    if monthDate is firstMonthDate:
        dailySoup = soup.find_all(
            lambda tag: tag.name == "tr"
            and "data-day" in tag.attrs
            and int(tag["data-day"]) > int(firstDayToAdd["day"]) - 1
        )
    else:
        dailySoup = soup.find_all("tr", attrs={"data-day": True})

    for daySoup in dailySoup:
        data["date"].append(daySoup.find_all("td")[0].string)
        data["minTemperature"].append(daySoup.find_all("td")[1].string)
        data["maxTemperature"].append(daySoup.find_all("td")[2].string)
        data["maxSustainedWind"].append(daySoup.find_all("td")[3].string)
        data["maxGustWind"].append(daySoup.find_all("td")[4].string)
        data["rainfall"].append(daySoup.find_all("td")[5].string)
        data["snowDepth"].append(daySoup.find_all("td")[6].string)
        data["barometricPressure"].append(daySoup.find_all("td")[7].string)
        data["description"].append(daySoup.find_all("td")[9].contents[0])

    monthDate = monthDate + relativedelta(months=+1)

with pd.ExcelWriter(
    "weather-data.xlsx", engine="openpyxl", mode="a", if_sheet_exists="overlay"
) as xlWriter:
    df = pd.DataFrame(data)
    df.to_excel(
        excel_writer=xlWriter,
        sheet_name="Sheet1",
        index=False,
        header=False,
        startrow=len(existingDf.index) + 1,
    )
