import pandas as pd


configDf = pd.read_excel(
    io="config.xlsx",
    sheet_name="Config",
    converters={"EXCEL_SHEET_NAME": str, "DATE_COLUMN_EXCEL_INDEX": int},
)

EXCEL_FILE_NAME = configDf["EXCEL_FILE_NAME"][0] + ".xlsx"
EXCEL_SHEET_NAME = configDf["EXCEL_SHEET_NAME"][0]
DATE_COL_EXCEL_INDEX = configDf["DATE_COLUMN_EXCEL_INDEX"][0]
