# weather-scraping

This repo contains a weather web scraping python script (code and .exe) I made for my dad.

He records and analyzes weather data for our orchard. 🍇🌳🍐🍑🍎🍒

## What does it do?

- extracts weather data from [freemeteo.ro](https://freemeteo.ro/vremea)
- exports the data into Excel

## Setup

**Dev:**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `pip install -r reqs.txt`

**User:**

1. download `Weather_Scraping.zip` from **Releases**

   or copy what's inside the `dist` folder

2. create your excel at the same level
3. add the date (dd.mm.yyyy) after which you want to get data
4. update `config.xlsx`

   - your excel name
   - your sheet name
   - the index of the first (date) column: `column number - 1`

     [Column letter to number converter](https://www.vishalon.net/blog/excel-column-letter-to-number-quick-reference)

5. run `weather_script.exe` and wait for the console window to close
6. PROFIT 📈📈📈
