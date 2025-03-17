# Matthew Leung

# Lists in variables based on order of days per month chronologically
days_per_month = ['31', '28', '31', '30', '31', '30', '31', '31', '30', '31', '30', '31']
leapyear_days_per_month = list(days_per_month)
leapyear_days_per_month[1] = '29'
print ('Enter a year to find:\n - Number of days per month\n - Number of days in my birth month\n - Sum of days in year\n - Number of days in summer\n - Number of days in first three months\n - Number of days in last three months')

def leapyear_days_list():
    """Displays number of days per month for entire leap year, my birth month, summer, first three months, last three months, both first three months and last three months as well as sum
    of days"""
    print(' - Number of days per month are {}, and {}.'.format(', '.join(leapyear_days_per_month[:11]), leapyear_days_per_month[11]))
    print(' - Number of days in my birth month, December, is {}.'.format(leapyear_days_per_month[11]))
    print(' - Total number of days that year is {}.'.format(sum([int(days) for days in leapyear_days_per_month])))
    print(' - Number of days in summer are {} and {}.'.format(leapyear_days_per_month[6], leapyear_days_per_month[7]))
    print(' - Number of days in first three months of year are {}, and {}.'.format(', '.join(leapyear_days_per_month[:2]), leapyear_days_per_month[2]))
    print(' - Number of days in last three months of year are {}, and {}.'.format(', '.join(leapyear_days_per_month[9:11]), leapyear_days_per_month[11]))
    print(' - Number of days in first and last three months of year are {} and {}.'.format(', '.join(leapyear_days_per_month[:3]), ', '.join(leapyear_days_per_month[9:11]), leapyear_days_per_month[11]))

def days_list():
    """Displays number of days per months for entire normal year, my birth months, first three months, last three months, both first three months and last three months as well as sum of
    days"""
    print(' - Number of days per month are {}, and {}.'.format(', '.join(days_per_month[:11]), days_per_month[11]))
    print(' - Number of days in my birth month, December, is {}.'.format(days_per_month[11]))
    print(' - Total number of days that year is {}.'.format(sum([int(days) for days in days_per_month])))
    print(' - Number of days in summer are {} and {}.'.format(days_per_month[6], days_per_month[7]))
    print(' - Number of days in first three months of year is {}, and {}.'.format(', '.join(days_per_month[:2]), days_per_month[2]))
    print(' - Number of days in last three months of year is {}, and {}.'.format(', '.join(days_per_month[9:11]), days_per_month[11]))
    print(' - Number of days in first and last three months of year are {}, {}, and {}.'.format(', '.join(days_per_month[:3]), ', '.join(days_per_month[9:11]), days_per_month[11]))
    
while True:
    
    year = input('Year: ')

    try:
        int(year)

        year = int(year)

        if year % 4 == 0:
            
            if year % 100 == 0:

                if year % 400 == 0:
                    leapyear_days_list()
                    break

                else:
                    days_list()
                    break
                
            else:
                leapyear_days_list()
                break
            
        else:
            days_list()
            break
        
    except ValueError:
        print('Invalid input. Numbers only.')
        continue
