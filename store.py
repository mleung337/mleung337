"""CSCA08 Summer 2024 Assignment 1.

This code is provided solely for the personal and private use of
students taking the CSCA08 course at the University of
Toronto. Copying for purposes other than this use is expressly
prohibited. All forms of distribution of this code, whether as given
or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2024 Bilal Syed.

"""

from constants import (PID, INV, DISC, PRICE, CID, AGE, BUDGET, SPID,
                       PURCHASE_NUM, DISCOUNT_RATE)


# This function solution is provided as an example of a function that uses
# constants, complete with correct documentation.
def get_pid(product: str) -> str:
    '''Returns the ID of product 'product'.

    Pre-condition: 'product' is a valid product.

    >>> get_pid('372908ALL147')
    '3729'
    >>> get_pid('999999SEN999')
    '9999'
    '''
    
    return product[PID:PID + 4]


# This function solution is provided as an example of a function that uses
# constants, complete with correct documentation.
def get_inventory(product: str) -> int:
    '''Returns the current inventory of product 'product'.

    Pre-condition: 'product' is a valid product.

    >>> get_inventory('372908ALL147')
    8
    >>> get_inventory('999999SEN999')
    99
    '''
    
    return int(product[INV:INV + 2])


# We provide the docstring for this function to help you get started.
def get_discount(product: str) -> str:
    '''Returns the discount type of product 'product'.

    Pre-condition: 'product' is a valid product.

    >>> get_discount('372908ALL147')
    'ALL'
    >>> get_discount('999999SEN999')
    'SEN'
    '''
    
    return product[DISC:DISC + 3]


# We provide the docstring for this function to help you get started.
def get_price(product: str) -> int:
    '''Returns the price of product 'product'.

    Pre-condition: 'product' is a valid product.

    >>> get_price('372908ALL147')
    147
    >>> get_price('999999SEN009')
    9
    >>> get_price('999999SEN089')
    89
    '''
    
    return int(product[PRICE:PRICE + 3])


def get_cid(customer: str) -> str:
    '''Returns the ID of customer 'customer'.
    
    Pre-condition: 'customer' is a valid customer.
    
    >>> get_cid('MARK17008')
    'MARK'
    >>> get_cid('ABCD64999')
    'ABCD'
    '''
    
    return customer[CID:CID + 4]


def get_age(customer: str) -> int:
    '''Returns the age of customer 'customer'.
    
    Pre-condition: 'customer' is a valid customer.
    
    >>> get_age('MARK17008')
    17
    >>> get_age('ABCD64999')
    64
    '''
    
    return int(customer[AGE:AGE + 2])


def get_budget(customer: str) -> int:
    '''Returns the budget of customer 'customer'.
    
    Pre-condition: 'customer' is a valid customer.
    
    >>> get_budget('MARK17008')
    8
    >>> get_budget('ABCD64999')
    999
    '''
    
    return int(customer[BUDGET:BUDGET + 3])


def get_spid(shopping_list: str) -> str:
    '''Returns the product ID of shopping list 'shopping_list'.
    
    Pre-condition: 'shopping_list' is a valid shopping list.
    
    >>> get_spid('018427')
    '0184'
    >>> get_spid('330904')
    '3309'
    '''
    
    return shopping_list[SPID:SPID + 4]


def get_purchase_num(shopping_list: str) -> int:
    '''Returns the amount of product to purchase of shopping list
    'shopping_list.'
    
    Pre-condition: 'shopping_list' is a valid shopping list.
    
    >>> get_purchase_num('018427')
    27
    >>> get_purchase_num('330904')
    4
    '''
    
    return int(shopping_list[PURCHASE_NUM:PURCHASE_NUM + 2])


def check_discount_eligibility(product: str, customer: str) -> bool:
    '''Returns True if and only if customer 'customer' is eligible for discount
    on product 'product'.
    
    Pre-condition: 'product' and 'customer' are valid products and customers,
    respectively.
    
    >>> check_discount_eligibility('372908ALL147', 'MARK17008')
    True
    >>> check_discount_eligibility('999999SEN999', 'ABCD64999')
    False
    '''
    
    product_disc = get_discount(product)
    customer_age = get_age(customer)
    
    all_disc = product_disc == 'ALL'
    teen_disc = product_disc == 'TEE' and 13 <= customer_age <= 19
    senior_disc = product_disc == 'SEN' and customer_age >= 65
    
    return all_disc or teen_disc or senior_disc
    
    
def calc_discounted_price(product: str, customer: str) -> int:
    '''Returns the price of product 'product' after applying discounts that
    customer 'customer' is eligible for, rounded to the nearest integer.
    
    Pre-condition: 'product' and 'customer' are valid products and customers
    respectively.
    
    >>> calc_discounted_price('372908ALL147', 'MARK17008')
    110
    >>> calc_discounted_price('999999SEN999', 'ABCD64999')
    999
    '''
    
    product_price = get_price(product)
    if check_discount_eligibility(product, customer):
        return int((1 - DISCOUNT_RATE) * product_price)
    return product_price
    
    
def calc_total_price(product: str, customer: str, shopping_list: str) -> int:
    '''Returns the total price of product 'product' after applying discounts
    that customer 'customer' is eligible for, according to the amount of that
    product purchased noted on the shopping list 'shopping_list'.
    
    Pre-conditions: 'product, 'customer', and 'shopping_list' are all valid
    products, customers, and shopping lists respectively. The product ID for
    product 'product' matches the product ID noted on shopping list
    'shopping_list'.
    
    >>> calc_total_price('372908ALL147', 'MARK17008', '372927')
    2970
    >>> calc_total_price('999999SEN999', 'ABCD64999', '999904')
    3996
    '''
    
    disc_price = calc_discounted_price(product, customer)
    product_num = get_purchase_num(shopping_list)
    return disc_price * product_num


def check_available_inventory(product: str, shopping_list: str) -> bool:
    '''Returns True if and only if current inventory of product 'product' can
    fulfill the order of the amount of product to be purchased listed on the
    shopping list 'shopping_list'.
    
    Pre-conditions: 'product' and 'shopping_list' are valid products and
    shopping lists respectively. The product ID for product 'product' matches
    the product' ID noted on shopping list 'shopping_list'.
    
    >>> check_available_inventory('372908ALL147', '372927')
    False
    >>> check_available_inventory('999999SEN999', '999904')
    True
    '''
    
    return get_inventory(product) >= get_purchase_num(shopping_list)


def within_budget(product: str, customer: str, shopping_list: str) -> bool:
    '''Returns True if and only if the customer 'customer' has enough budget to
    purchase the amount of product 'product' listed on shopping list
    'shopping_list'.
    
    Pre-conditions: 'product, 'customer', and 'shopping_list' are all valid
    products, customers, and shopping lists respectively. The product ID for
    product 'product' matches the product ID noted on shopping list
    'shopping_list'.
    
    >>> within_budget('372908ALL147', 'MARK17008', '372927')
    False
    >>> within_budget('999999SEN999', 'ABCD64999', '999901')
    True
    '''
    
    customer_budget = get_budget(customer)
    total_price = calc_total_price(product, customer, shopping_list)
    return customer_budget >= total_price


def checkout(product: str, customer: str, shopping_list: str) -> bool:
    '''Returns True if and only if customer 'customer' is capable of purchasing
    the amount of product 'product' listed on shopping list 'shopping_list'.
    
    Pre-conditions: 'product, 'customer', and 'shopping_list' are all valid
    products, customers, and shopping lists respectively. The product ID for
    product 'product' matches the product ID noted on shopping list
    'shopping_list'.
    
    >>> checkout('372908ALL147', 'MARK17008', '372927')
    False
    >>> checkout('999999SEN999', 'ABCD64999', '999901')
    True
    '''
    purchaseable = within_budget(product, customer, shopping_list)
    available = check_available_inventory(product, shopping_list)
    return purchaseable and available


def change_inventory(product: str, shopping_list: str) -> str:
    '''Returns new product string based on the amount of product 'product' that 
    is being purchased listed on shopping list 'shopping_list' only if there is
    available inventory for the purchase.
    
    Pre-conditions: 'product' and 'shopping_list' are valid products and
    shopping lists respectively. The product ID for product 'product' matches
    the product' ID noted on shopping list 'shopping_list'.
    
    >>> change_inventory('372908ALL147', '372927')
    '372908ALL147'
    >>> change_inventory('999999SEN999', '999904')
    '999995SEN999'
    '''
    
    if check_available_inventory(product, shopping_list):
        new_inv = str(get_inventory(product) - get_purchase_num(shopping_list))
        return product[:INV] + new_inv + product[INV + 2:]
    return product


def change_price(product: str, price: int) -> str:
    '''Returns new product string for product 'product' with new price 'price'.
    
    Pre-condition: 'product' is a valid product. 'price' is a valid price for a
    product string.
    
    >>> change_price('372908ALL147', 136)
    '372908ALL136'
    >>> change_price('999999SEN999', 988)
    '999999SEN988'
    '''
    
    return product[:PRICE] + str(price) + product[PRICE + 3:]


def compare_products(product1: str, product2: str) -> str:
    '''Returns the product ID of the better of the two products. Product
    'product1' is better if:
    > Each digit of product 'product1'’s ID is greater than the respective digit
    of product 'product2'’s ID, not comparing the third digit
    > The current inventory of product ‘product1’ is at least as much as the
    current inventory of product ‘product2’
    > The price of product ‘product1’ is lower than that of product ‘product2’
    
    Pre-condition: 'product1' and 'product2' are valid products.
    
    >>> compare_products('372908ALL147', '999999SEN999')
    '9999'
    >>> compare_products('233560NON095', '123450ALL100')
    '2335'
    '''
    
    product1_id = get_pid(product1)
    product2_id = get_pid(product2)
    
    better_digit1 = int(product1_id[0]) > int(product2_id[0])
    better_digit2 = int(product1_id[1]) > int(product2_id[1])
    better_digit4 = int(product1_id[3]) > int(product2_id[3])
    
    better_id = better_digit1 and better_digit2 and better_digit4
    better_inv = get_inventory(product1) >= get_inventory(product2)
    better_price = get_price(product1) < get_price(product2)
    
    if better_id and better_inv and better_price:
        return product1_id 
    return product2_id


if __name__ == '__main__':
    import doctest
    doctest.testmod()
