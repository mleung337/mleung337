# Matthew Leung

while True:
    age_of_people = input('\nEnter the age of the people you want to calculate the average age of. \nEnter all, seperated with commas. ').split(',')
    
    try:
        [int(ages) for ages in age_of_people]
        age_of_people = [int(ages) for ages in age_of_people]
        age_of_people = list(map(int, age_of_people))
        number_of_people = len(age_of_people)
        average_age = sum(age_of_people) / number_of_people
        print(f'\nYou entered the age of {number_of_people} people. Their average age is {"%.1f" % average_age}.')
        break

    except ValueError:
        print('\nInvalid input.')
        continue
        
