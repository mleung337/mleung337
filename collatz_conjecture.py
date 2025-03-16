# Matthew Leung

steps = 0

while True:
    initial_number = input('\nEnter the initial number for the Collatz Conjecture here.\n')

    try:
        float(initial_number)
        initial_number = float(initial_number)

        if initial_number > 0:

            while True:

                if initial_number == 1:
                    steps += 1
                    print(f'Reached 1. \nTook {steps} steps.')
                    raise SystemExit

                elif initial_number % 2 != 0:
                    # Operations from assignment
                    initial_number = initial_number * 3 + 1
                    steps += 1
                    print(initial_number)

                elif initial_number % 2 == 0:
                    # Operations from assignment
                    initial_number = initial_number / 2
                    steps += 1
                    print(initial_number)

        elif initial_number < 0 or initial_number == 0:

            while True:
                warning = input('\nInput will never reach 1. \nContinue? (y)es/(n)o ')

                if warning == 'n':
                    break

                elif warning == 'y':

                    while True:

                        if steps == 100:
                            print(f'Stopped at {steps} steps.')
                            raise SystemExit

                        elif initial_number == 1:
                            steps +=1
                            print(f'Reached 1. \nTook {steps} steps.')
                            raise SystemExit
                        
                        elif initial_number % 2 != 0:
                            # Operations from assignment
                            initial_number = initial_number * 3 + 1
                            steps += 1
                            print(initial_number)

                        elif initial_number % 2 == 0:
                            #Operations from assignment
                            initial_number = initial_number / 2
                            steps += 1
                            print(initial_number)

                else:
                    print('\nInvalid input.')
                    continue

    except ValueError:
        print ('\nInvalid input.')
        continue


