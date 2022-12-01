import requests
import bs4
import pandas as pd


def dataToExcel():
    url = "https://freemeteo.ro/vremea/bucuroaia/istoric/istoric-lunar/?gid=683499&station=4621&month=10&year=2022&language=romanian&country=romania"
    response = requests.get(url)

    soup = bs4.BeautifulSoup(response.text, "lxml")
    dailySoup = soup.find_all("tr", attrs={"data-day": True})

    dataPointKeys = [
        "minTemperature",
        "maxTemperature",
        "maxSustainedWind",
        "maxGustWind",
        "rainfall",
        "snowDepth",
        "barometricPressure",
        "description",
    ]
    data = {dataPointKey: [] for dataPointKey in dataPointKeys}
    for daySoup in dailySoup:
        data["minTemperature"].append(daySoup.find_all("td")[1].string)
        data["maxTemperature"].append(daySoup.find_all("td")[2].string)
        data["maxSustainedWind"].append(daySoup.find_all("td")[3].string)
        data["maxGustWind"].append(daySoup.find_all("td")[4].string)
        data["rainfall"].append(daySoup.find_all("td")[5].string)
        data["snowDepth"].append(daySoup.find_all("td")[6].string)
        data["barometricPressure"].append(daySoup.find_all("td")[7].string)
        data["description"].append(daySoup.find_all("td")[9].contents[0])

    df = pd.DataFrame(data)
    # day as index -> start index from 1
    df.index += 1
    df.to_excel("weather-data.xlsx", sheet_name="Sheet1")
