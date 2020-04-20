def standardDate(date):
    date = date.strip().split('/')
    if len(date[1]) == 2:
        dd = date[1]
    else:
        dd = '0' + date[1]
    if len(date[0]) == 2:
        mm = date[0]
    else:
        mm = '0' + date[0]
    yyyy = '20' + date[2]
    return dd+'/'+mm+'/'+yyyy

def writeToFile(country, dates, confirmedCases, recoveredCases, deaths):
    with open("{country}CoronaData.csv".format(country = country.lower()), 'w') as outFile:
        outFile.writelines("date, confirmed_cases, recovered_cases, total_deaths\n")                                        #header of the CSV file
        count = 0
        for date in dates:
            outFile.writelines("{date},{CC},{RC},{D}\n".format(date = date, CC = confirmedCases[count], RC = recoveredCases[count], D = deaths[count]))
            count += 1
        print("{country}CoronaData.csv".format(country = country.lower()) + " is created...")
