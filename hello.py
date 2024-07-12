import sqlite3
import pandas as pd

con = sqlite3.connect('db.sqlite3')
wb = pd.read_excel('C:\\Users\\bimas\\OneDrive\\Desktop\\hydropower_1.xlsx',sheet_name = None)

for sheet in wb:
    wb[sheet].to_sql(sheet,con,index=False)
con.commit()
con.close()

