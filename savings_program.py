# Matthew Leung

while True:
    savings_goal = input('\nHow much money do you need save? ')

    try:
        float(savings_goal)
        savings_goal = float(savings_goal)

        if savings_goal <= 0:

            while True:
                retry = input('\nNo need to save money.\nEnter different value? (q)uit/(c)ontinue ')

                if retry == 'c':
                    break

                elif retry == 'q':
                    raise SystemExit

                else:
                    print('\nInvalid input.')
                    continue

        else:

            while True:
                time_unit = input('\nHow often can you set aside money? (d)ay/(w)eek/(m)onth/(y)ear ')

                if time_unit == 'd':

                    while True:
                        money_saved_days = input('\nHow much money can you put aside each day? ')

                        try:
                            float(money_saved_days)  
                            money_saved_days = float(money_saved_days)

                            if money_saved_days <= 0:

                                while True:
                                    retry = input('\nSavings goal cannot be reached. \nEnter different value? (q)uit/(c)ontinue ')

                                    if retry == 'q':
                                        raise SystemExit
                                    
                                    elif retry == 'c':
                                        break

                                    else:
                                        print('Invalid input.')
                                        continue
                                        
                            else:
                                # payment_time variables based on conversion of time units
                                payment_time_days = savings_goal / money_saved_days
                                payment_time_weeks = payment_time_days / 7
                                payment_time_months = payment_time_days / 30
                                payment_time_years = payment_time_months / 12
                                print (f'\nIt will take about {"%.3f" % payment_time_days} days,\n{"%.3f" % payment_time_weeks} weeks,\n{"%.3f" % payment_time_months} months, or\n{"%.3f" % payment_time_years} years to save enough money to achieve your goal.')
                                raise SystemExit

                        except ValueError:
                            print('\nInvalid input. Numbers only.')
                            continue

                elif 'w' in time_unit:

                    while True:
                        money_saved_weeks = input('\nHow much money can you put aside each week? ')

                        try:
                            float(money_saved_weeks)
                            money_saved_weeks = float(money_saved_weeks)

                            if money_saved_weeks <= 0:

                                while True:
                                    retry = input('\nSavings goal cannot be reached. \nEnter different value? (q)uit/(c)ontinue ')

                                    if 'q' in retry:
                                        raise SystemExit

                                    elif 'c' in retry:
                                        break
                                        
                                    else:
                                        print('Invalid input. (q) or (c) only.')
                                        continue
                                    
                            else:
                                payment_time_weeks = savings_goal / money_saved_weeks
                                payment_time_days = payment_time_weeks * 7
                                payment_time_months = payment_time_days / 30
                                payment_time_years = payment_time_months / 12
                                print (f'\nIt will take about {"%.3f" % payment_time_days} days,\n{"%.3f" % payment_time_weeks} weeks,\n{"%.3f" % payment_time_months} months, or\n{"%.3f" % payment_time_years} years to save enough money to achieve your goal.')
                                raise SystemExit

                        except ValueError:
                            print('\nInvalid input.')
                            continue

                elif 'm' in time_unit:

                    while True:
                        money_saved_months = input('\nHow much money can you put aside each month? ')

                        try:
                            float(money_saved_months)
                            money_saved_months = float(money_saved_months)

                            if money_saved_months <= 0:

                                while True:
                                    retry = input('\nSavings goal cannot be reached. \nEnter different value? (q)uit/(c)ontinue ')

                                    if 'q' in retry:
                                        raise SystemExit

                                    elif 'c' in retry:
                                        break

                                    else:
                                        print('\nInvalid input.')
                                        continue

                            else:
                                payment_time_months = savings_goal / money_saved_months
                                payment_time_days = payment_time_months * 30
                                payment_time_weeks = payment_time_days / 7
                                payment_time_years = payment_time_months / 12
                                print(f'\nIt will take about {"%.3f" % payment_time_days} days,\n{"%.3f" % payment_time_weeks} weeks,\n{"%.3f" % payment_time_months} months, or\n{"%.3f" % payment_time_years} years to save enough money to achieve your goal.')
                                raise SystemExit

                        except ValueError:
                            print('\nInvalid input.')
                            continue

                elif 'y' in time_unit:

                    while True:
                        money_saved_years = input('\nHow much money can you put aside each year? ')

                        try:
                            float(money_saved_years)
                            money_saved_years = float(money_saved_years)

                            if money_saved_years <= 0:
                                
                                while True:
                                    retry = input('\nSavings goal cannot be reached. \nEnter different value? (q)uit/(c)ontinue ')

                                    if 'q' in retry:
                                        raise SystemExit

                                    elif 'c' in retry:
                                        break

                                    else:
                                        print('\nInvalid input.')
                                        continue

                            elif money_saved_years > 0:
                                payment_time_years = savings_goal / money_saved_years
                                payment_time_months = payment_time_years * 12
                                payment_time_days = payment_time_months * 30
                                payment_time_weeks = payment_time_days / 7
                                print(f'\nIt will take about {"%.3f" % payment_time_days} days,\n{"%.3f" % payment_time_weeks} weeks,\n{"%.3f" % payment_time_months} months, or\n{"%.3f" % payment_time_years} years to save enough money to achieve your goal.')
                                raise SystemExit

                        except ValueError:
                            print('\nInvalid input.')
                            continue

                else:   
                    print('\nInvalid input.')
                    continue

    except ValueError:
        print('\nInvalid input.')
        continue
