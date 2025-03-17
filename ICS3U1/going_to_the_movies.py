# Matthew Leung

audience_name = input('\nHello, what is your name? ')

while True:
    audience_age = input(f'\nHello, {audience_name}, how old are you? ')

    try:
        float(audience_age)
        audience_age = float(audience_age)

        while True:
            ticket_quantity = input('\nHow many tickets would you like to purchase? ')

            try:
                int(ticket_quantity)
                ticket_quantity = int(ticket_quantity)

                if audience_age <= 3:
                    ticket_price = 0
                    print('\nOne ticket is free.')

                elif audience_age > 3 and audience_age <= 12:
                    ticket_price = 10
                    print(f'\nPrice of one ticket is {"%.2f" % ticket_price} dollars.')

                elif audience_age >= 65:
                    ticket_price = 15
                    print(f'\nPrice of one ticket is {"%.2f" % ticket_price} dollars.')

                else:
                    ticket_price = 25
                    print(f'\nPrice of one ticket is {"%.2f" % ticket_price} dollars.')

                total_price = ticket_price * ticket_quantity
                print(f'\nYour total cost is {"%.2f" % total_price} dollars, enjoy the movie!')
                raise SystemExit

            except ValueError:
                print('\nThat is not a valid ticket quantity.')
                continue

    except ValueError:
        print('\nThat is not a valid age.')
        continue
