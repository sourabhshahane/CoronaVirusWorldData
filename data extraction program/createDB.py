import sqlite3
import requests
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = '''https://covid.ourworldindata.org/data/owid-covid-data.csv'''


def getCSV(address, fName):
    with open(address + fName, 'w') as outFile:
        print("Writing web contents to File {Location}{Filename}...".format(Location=address, Filename=fName))
        csv = requests.get(url)
        outFile.write(csv.text)


country = input('Enter full name of the country:')
localAddress = "C:\\Users\\Sourabh Shahane\\CoronaVirusWorldData\\"  # Enter your local location here
sqliteFileName = "{country}Data.sqlite".format(country=country)
csvFileName = "coronaData.csv"

getCSV(localAddress, csvFileName)  # save a csv file named 'coronaData.csv'(fileName)in localAddress

connection = sqlite3.connect(localAddress + sqliteFileName)
cursor = connection.cursor()

cursor.executescript('''DROP TABLE IF EXISTS data;
CREATE TABLE data
( "serial number"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
"date"	TEXT NOT NULL,
"total_cases"	INTEGER,
"new_cases"	INTEGER,
"total_deaths"	INTEGER,
"new_deaths"	INTEGER
);'''.format(country=country))

head = False

with open(localAddress + csvFileName) as fh:
    with open(localAddress+sqliteFileName.split('.')[0]+'.csv', 'w') as outFile:
        for line in fh:
            line = line.split(',')
            if head is False:
                outFile.write(line[2]+ ',' + line[3]+ ',' +  line[4]+ ',' +  line[5]+ ',' +  line[6] + '\n')
                head = True
                continue
            if line[1].lower().strip() == country.lower():
                outFile.write(line[2]+ ',' + line[3]+ ',' + line[4]+ ',' +  line[5]+ ',' +  line[6] + '\n')
                print(line[2], int(line[3]), int(line[4]), int(line[5]), int(line[6]))
                cursor.execute('''INSERT INTO data(date, total_cases, new_cases, total_deaths, new_deaths)
                VALUES ( ? ,? ,? ,? ,? )''', (line[2], int(line[3]), int(line[4]), int(line[5]), int(line[6])))
connection.commit()
