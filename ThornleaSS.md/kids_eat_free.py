# Matthew Leung

customer_name = input('Hello. What is your name? ')

while True:
    customer_age = input(f'Hello, {customer_name}, how old are you? ')

    try:
        float(customer_age)
        customer_age = float(customer_age)

        if customer_age <= 12:
            print('Your meal will be free. Enjoy!')
            break
        else:
            print('Sorry, you will have to pay for your meal - only kids 12 and under eat free.')
            break

    except ValueError:
        print('That is not a valid age.')
        continue
