# Matthew Leung

while True:
    range_variable = input('\nPick a range for multiplication table. (q) to quit ')

    if range_variable == 'q':
        raise SystemExit

    else:

        try:
            int(range_variable)
            range_variable = int(range_variable)
            range_variable += 1
    
            for multiple1 in range(1, range_variable):

                for multiple2 in range(1, range_variable):
                    print(f'\n{multiple1} x {multiple2} = {multiple1 * multiple2}')

        except ValueError:
            print('\nInvalid input.')
            continue
