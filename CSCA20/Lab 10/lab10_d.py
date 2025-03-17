# Part D: Extension Skills

import csv
import sqlite3 as sql
import sql_tools as tools
import matplotlib.pyplot as plt
import numpy as np

def verify_file(string):
    
    print('\nEnter name of {0} file.'.format(string))
    
    while True:
        
        file_name = input('\nFile name here: ')
        
        try:
            
            open(file_name)
            
            return file_name
        
        except:
            
            print('\nInvalid file name. Try again.')
            
def file_get():
    
    pch_name = verify_file('purchases')
    ppl_name = verify_file('customers')
    fd_name = verify_file('foods')
    bdg_name = verify_file('budgets')
    
    return pch_name, ppl_name, fd_name, bdg_name
    
def file_open():
    
    pchs = open(pch_name, 'r')
    ppls = open(ppl_name, 'r')
    fds = open(fd_name, 'r')
    bdgs = open(bdg_name, 'r')
    
    return pchs, ppls, fds, bdgs
    
def file_close():
    
    pchs.close()
    ppls.close()
    fds.close()
    bdgs.close()    

def csv_to_dict(csv_name, key_name, val_name):
    
    with open(csv_name, 'r') as csv_file:
        
        reader = csv.reader(csv_file)
        columns = next(reader)
        
        for title in range(len(columns)):
            
            if columns[title] == key_name:
                
                key = title
                
            elif columns[title] == val_name:
                
                val = title
        
        csv_dict = {}
        
        for row in reader:
            
            if row[key] in csv_dict.keys():
                
                csv_dict[row[key]].append(row[val])
                
            else:
                
                csv_dict[row[key]] = [row[val]]
            
        return csv_dict
    
def graph_output():
    
    row1 = crsr.execute('''SELECT budget, price FROM pricecomp;''').fetchall()
    
    budgets = []
    prices = []
    
    for tup in row1:
        
        budgets.append(tup[0])
        prices.append(tup[1])
        
    x1 = np.array(budgets)
    y1 = np.array(prices)
    
    plt.figure()
    plt.title('Budgets vs. Prices of Items Purchased')
    plt.xlabel('Budgets ($)')
    plt.ylabel('Item Prices ($)')
    plt.scatter(x1, y1)
    plt.show()
    
    row2 = crsr.execute('''SELECT age, quantity FROM quantitycomp;''').fetchall()
    
    ages = []
    quantities = []
    
    for tup in row2:
        
        ages.append(tup[0])
        quantities.append(tup[1])
        
    x2 = np.array(ages)
    y2 = np.array(quantities)
    
    plt.figure()
    plt.title('Age vs. Quantity of Items Purchased')
    plt.xlabel('Age')
    plt.ylabel('Quantity')
    plt.scatter(x2, y2)
    plt.show()    

got_files = False

db = sql.connect('customer_data.db')
crsr = db.cursor()

menu = '''\n=== UTSC ===
A = Add files
F = All foods purchased by a customer
D = All days on which a customer shopped
C = All customers who have spent past their budget
G = Generate graph and csv file
E = Exit program

Add files first before using other options.

Type here: '''

while True:
    
    menu_choice = input(menu)
    
    if menu_choice == 'A':
        
        pch_name, ppl_name, fd_name, bdg_name = file_get()
        got_files = True
        
    elif menu_choice == 'F' and got_files:
        
        pchs = csv_to_dict(pch_name, 'person_id', 'food_id')
        ppls = csv_to_dict(ppl_name, 'name', 'person_id')
        fds = csv_to_dict(fd_name, 'food_id', 'name')
        
        while True:
            
            customer = input('\nEnter customer name: ')
            
            if customer not in ppls.keys():
                
                print('\nCustomer does not exist. Try again.')
                
            else:
                
                break
        
        customer_ID = ppls[customer][0]
        food_IDs = pchs[customer_ID]
        foods = []
        
        for food_ID in food_IDs:
            
            foods.append(fds[food_ID][0])
        
        print('Foods purchased by {0}: {1}'.format(customer, set(foods)))
                    
    elif menu_choice == 'D' and got_files:
        
        pchs = csv_to_dict(pch_name, 'person_id', 'day')
        ppls = csv_to_dict(ppl_name, 'name', 'person_id')
        
        while True:
            
            customer = input('\nEnter customer name: ')
            
            if customer not in ppls.keys():
                
                print('\nCustomer does not exist. Try again.')
                
            else:
                
                break
        
        customer_ID = ppls[customer][0]
        
        print('Days where {0} shopped: {1}'.format(customer, set(pchs[customer_ID])))
        
    elif menu_choice == 'C' and got_files:
        
        pchs_id = csv_to_dict(pch_name, 'person_id', 'food_id')
        pchs_q = csv_to_dict(pch_name, 'person_id', 'quantity')
        ppls = csv_to_dict(ppl_name, 'person_id', 'name')
        fds = csv_to_dict(fd_name, 'food_id', 'price')
        bdgs = csv_to_dict(bdg_name, 'person_id', 'budget')
        
        pchs = {}
        
        for pch in pchs_id:
            
            if pch in pchs_q:
                
                pchs.update({pch:[pchs_id[pch][0], pchs_q[pch][0]]})
                
        for pch in pchs:
            
            if pchs[pch][0] in fds.keys():
                
                pchs[pch][0] = fds[pchs[pch][0]][0]
                
        for pch in pchs:
            
            pchs[pch] = float(pchs[pch][0]) * float(pchs[pch][1])
            
        overload = set()
        
        for pch in pchs:
            
            if float(bdgs[pch][0]) < pchs[pch]:
                
                overload.update(ppls[pch])
        
        for person in overload:
            
            print(person)
            
    elif menu_choice == 'G' and got_files:
        
        pchs, ppls, fds, bdgs = file_open()
            
        tools.csv_to_table(db, pchs, 'purchases', ['TEXT', 'TEXT', 'INTEGER', 'TEXT'])
        tools.csv_to_table(db, ppls, 'people', ['TEXT', 'TEXT', 'INTEGER', 'TEXT', 'INTEGER', 'BOOL'])
        tools.csv_to_table(db, fds, 'foods', ['TEXT', 'TEXT', 'REAL', 'TEXT', 'BOOL'])
        tools.csv_to_table(db, bdgs, 'budgets', ['TEXT', 'REAL'])
            
        crsr.execute('CREATE TABLE IF NOT EXISTS pricecomp(budget, price);')
        crsr.execute('CREATE TABLE IF NOT EXISTS quantitycomp(age, quantity);')
            
        purchase_opt = '''\nA = Include all purchases
M = Include member purchases only
F = Include fruit purchases only
            
Type here: '''
            
        while True:
                
            purchase_choice = input(purchase_opt)
                
            if purchase_choice == 'A':
                    
                crsr.execute('''
                INSERT INTO pricecomp
                SELECT budget, price FROM budgets, purchases, foods
                WHERE budgets.person_id = purchases.person_id
                AND purchases.food_id = foods.food_id;''')
                    
                crsr.execute('''
                INSERT INTO quantitycomp
                SELECT age, SUM(quantity) FROM people, purchases
                WHERE people.person_id = purchases.person_id
                GROUP BY purchases.person_id;''')                    
                    
                graph_output()
                    
                with open('pricecomp_a.csv', 'w') as pricecomp:
                    tools.table_to_csv(db, pricecomp, 'pricecomp')
                        
                with open('quantitycomp_a.csv', 'w') as quantitycomp:
                    tools.table_to_csv(db, quantitycomp, 'quantitycomp')
                        
                crsr.execute('''DROP TABLE IF EXISTS pricecomp;''')
                crsr.execute('''DROP TABLE IF EXISTS quantitycomp;''')
                file_close()
                break
                        
            elif purchase_choice == 'M':
                    
                crsr.execute('''
                INSERT INTO pricecomp
                SELECT budget, price FROM budgets, purchases, foods, people
                WHERE budgets.person_id = purchases.person_id
                AND purchases.food_id = foods.food_id
                AND people.person_id = budgets.person_id
                AND people.membership = TRUE;''')
                    
                crsr.execute('''
                INSERT INTO quantitycomp
                SELECT age, SUM(quantity) FROM people, purchases
                WHERE people.person_id = purchases.person_id
                AND people.membership = TRUE
                GROUP BY purchases.person_id;''')                    
                    
                graph_output()
                    
                with open('pricecomp_m.csv', 'w') as pricecomp:
                    tools.table_to_csv(db, pricecomp, 'pricecomp')
                        
                with open('quantitycomp_m.csv', 'w') as quantitycomp:
                    tools.table_to_csv(db, quantitycomp, 'quantitycomp')
                        
                crsr.execute('''DROP TABLE IF EXISTS pricecomp;''')
                crsr.execute('''DROP TABLE IF EXISTS quantitycomp;''')
                file_close()
                break
                
            elif purchase_choice == 'F':
                    
                crsr.execute('''
                INSERT INTO pricecomp
                SELECT budget, price FROM budgets, purchases, foods
                WHERE budgets.person_id = purchases.person_id
                AND purchases.food_id = foods.food_id
                AND foods.is_fruit = TRUE;''')
                    
                crsr.execute('''
                INSERT INTO quantitycomp
                SELECT age, SUM(quantity) FROM people, purchases, foods
                WHERE people.person_id = purchases.person_id
                AND purchases.food_id = foods.food_id
                AND foods.is_fruit = TRUE
                GROUP BY purchases.person_id;''')                    
                    
                graph_output()
                    
                with open('pricecomp_f.csv', 'w') as pricecomp:
                    tools.table_to_csv(db, pricecomp, 'pricecomp')
                        
                with open('quantitycomp_f.csv', 'w') as quantitycomp:
                    tools.table_to_csv(db, quantitycomp, 'quantitycomp')
                        
                crsr.execute('''DROP TABLE IF EXISTS pricecomp;''')
                crsr.execute('''DROP TABLE IF EXISTS quantitycomp;''')
                file_close()
                break
                    
            else:
                    
                print('\nInvalid purchases choice. Try again.')

    elif menu_choice == 'E':
        
        print('\nClosing...')
        
        db.close()
        
        raise SystemExit
    
    else:
        
        print('\nInvalid menu choice. Try again.')