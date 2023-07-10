import csv
import sqlite3
from kaggle.api.kaggle_api_extended import KaggleApi
import zipfile

api = KaggleApi()
api.authenticate()
api.dataset_download_file('vivek468/superstore-dataset-final', file_name='Sample - Superstore.csv')
with zipfile.ZipFile('Sample%20-%20Superstore.csv.zip', 'r') as zipfile:
    zipfile.extractall()

db = sqlite3.connect('superstore.db')
cursor = db.cursor()

cursor.execute(
    '''
    DROP TABLE  IF EXISTS superstore
    '''
)

cursor.execute(
     '''
    CREATE TABLE IF NOT EXISTS superstore (
            [Row_ID] INTEGER PRIMARY KEY,
            [Order_ID] TEXT,
            [Order_Date] TEXT,
            [Ship_Date] TEXT,
            [Ship_Mode] TEXT,
            [Customer_ID] TEXT,
            [Customer_Name] TEXT,
            [Segment] TEXT,
            [Country] TEXT,
            [City] TEXT,
            [State] TEXT,
            [Postal_Code] INTEGER,
            [Region] TEXT,
            [Product_ID] TEXT,
            [Category] TEXT,
            [Sub_Category] TEXT,
            [Product_Name] TEXT,
            [Sales] INTEGER,
            [Quantity] INTEGER,
            [Discount] INTEGER,
            [Profit] INTEGER
    )
    '''
)


file = open('./Sample - Superstore.csv')
contents = csv.reader(file)
next(contents, None)

insert_records = "INSERT INTO superstore (Row_ID, Order_ID, Order_Date, Ship_Date, Ship_Mode, Customer_ID, Customer_Name, Segment, Country, City, State, Postal_Code, Region, Product_ID, Category, Sub_Category, Product_Name, Sales, Quantity, Discount, Profit) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
cursor.executemany(insert_records, contents)

db.commit()
db.close()
