# weather-scraping

This repo contains a weather web scraping python script (code and .bat) I made for my dad.

He records and analyzes weather data for our orchard. 🍇🌳🍐🍑🍎🍒

[C++ version 🔥](https://github.com/Hornflakes/fast-weather-scraping)

## What does it do?

-   extracts weather data from [freemeteo.ro](https://freemeteo.ro/vremea)
-   exports the data into Excel

## Setup

**Dev:**

Make sure the excel files are in the same folder from which you run the script (be it .py or .bat).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **Install packages:** `pip install -r reqs.txt`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **Compile to .exe:** `pyinstaller weather_script.py`

**User:**

1. download `Weather_Scraping.zip` from **Releases**

    or copy what's inside the `dist` folder

2. replace `weather_data.xlsx` with your own excel

    or use it (skip the next 2 steps)

3. add the date (dd.mm.yyyy) after which you want to get data
4. update `config.xlsx`

    - your excel name
    - your sheet name
    - the index of the first (date) column: `column number - 1`

        [Column letter to number converter](https://www.vishalon.net/blog/excel-column-letter-to-number-quick-reference)

5. run `weather_script.bat` and wait for the console window to close
6. PROFIT 📈📈📈

#

The CA certificate for the data request can expire. In that case, you can replace it.

The certificate is `app/certifi/cacert.pem`. [You can download certificates here.](https://curl.se/docs/caextract.html)
