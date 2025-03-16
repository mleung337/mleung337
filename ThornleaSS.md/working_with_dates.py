# Matthew Leung

US_date = '09/30/2021.'
print(US_date)

year = US_date[6:10]
month = US_date[3:5]
day = US_date[:2]

CA_date = '{}/{}/{}'.format(year, month, day)
print(CA_date)
