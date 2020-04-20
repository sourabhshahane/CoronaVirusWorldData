'''
    THIS PROGRAM IS DEVELOPED BY SOURABH_SHAHANE TO GATHER ALL THE NECESSARY INFORMATION ABOUT COVID-19 IN ANY COUNTRY
    YOU WISH.
    THIS DATA CAN BE USED TO ANALYSE THE FUTURE PATTERNS OF COVID-19 IN ANY COUNTRY.
    THIS PROGRAM IS UNDER FURTHER DEVELOPMENT.
    THIS PROGRAM WILL WORK FINE WITH ALL THE COUNTRIES IN THE DATABASE HAVING ONLY ONE GEOGRAPHIC POSITION (LIKE INDIA),
     BUT FURTHER COMPATIBILITY ISSUES NEED TO BE RESOLVED

    LAST UPDATED 21/04/2020
'''

import requests
import ssl
import helperFunctions

#IGNORE SSL CERTIFICATE ERRORS
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

confirmedCasesURL = '''https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_confirmed_global.csv&filename=time_series_covid19_confirmed_global.csv'''
recoveredCasesURL = '''https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_recovered_global.csv&filename=time_series_covid19_recovered_global.csv'''
deadCasesURL = '''https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_deaths_global.csv&filename=time_series_covid19_deaths_global.csv'''

country = 'india'                                                                                                       #TYPE THE FULL NAME OF THE COUNTRY HERE

dates = list()
confirmedCases = list()
recoveredCases = list()
deaths = list()
headerLine = True

print("Getting data from web...")
confirmedCSV = requests.get(confirmedCasesURL)
print('Collected confirmed cases...')
recoverdCSV = requests.get(recoveredCasesURL)
print('Collected recovered cases...')
deadCSV = requests.get(deadCasesURL)
print('Collected dead cases...')
print('Collected all the data from web... ')

Ctext = confirmedCSV.text
Rtext = recoverdCSV.text
Dtext = deadCSV.text

for line in Ctext.rstrip('\n').split('\n'):
    line = line.rstrip('\r').split(',')
    if headerLine is True:
        headerLine = False
        for date in line[4:]:
            dates.append(helperFunctions.standardDate(date))
        continue
    if line[1].lower().strip() == country.lower():
        for cCases in line[4:]:
            confirmedCases.append(cCases)

for line in Rtext.rstrip('\n').split('\n'):
    line = line.rstrip('\r').split(',')
    if line[1].lower().strip() == country.lower():
        for rCases in line[4:]:
            recoveredCases.append(rCases)

for line in Dtext.rstrip('\n').split('\n'):
    line = line.rstrip('\r').split(',')
    if line[1].lower().strip() == country.lower():
        for dCases in line[4:]:
            deaths.append(dCases)

print('creating data.csv file of your chosen country...')
helperFunctions.writeToFile(country,dates, confirmedCases, recoveredCases, deaths)                                      #WRITING ALL DATA TO FILES
