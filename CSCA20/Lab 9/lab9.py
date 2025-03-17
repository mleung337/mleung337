# Import sqlite3 and sql_tools for usage
import sqlite3 as sql
import sql_tools

# Function that limits purchase categories
def pch_choice():
    print(pch_opt)
    choice = input('Select purchases: ')
    
    if choice == 'A':
        return 1
    
    elif choice == 'M':
        return 2
    
    elif choice == 'F':
        return 3
    
    else:
        print('\nInvalid input. Try again.')
        return 0
    
# Function that opens csv files
def csv_open():
    bdg = open('budgets.csv', 'r')
    fds = open('foods.csv', 'r')
    ppl = open('people.csv', 'r')
    pch = open('purchases.csv', 'r')
    return bdg, fds, ppl, pch
    
# Function that closes csv files
def csv_close():
    bdg.close()
    fds.close()
    ppl.close()
    pch.close()
    
# Menu where user can select information as these columns:
# > Customer name, item purchased, and day of week it was purchased
# > Customer ID, customer budget, and price of items purchased
# > Customer name, number of visits, name of food purchased, and day of week it
#   was purchased
# as well as purchase information as:
# > Include all purchases
# > Include purchases made by members only
# > Include purchases of fruits only

# Menu options
menu_opt = '''\n=== UTSC ===
CPD = Select information as name, item purchased, and day of week of purchase
CBP = Select information as ID, budget, and price of purchased items
CVFD = Select information as name, number of visits, food purchased, and day of
       week of purchase
E = Exit program
Ensure file names are in same location as program. Include budgets.csv,
foods.csv, people.csv, and purchases.csv.'''

# Purchases options
pch_opt = '''\nA = Include all purchases
M = Include member purchases only
F = Include fruit purchases only'''

# Create SQL database and cursor
db = sql.connect('customer_data.db')
crsr = db.cursor()

# Open csv files
bdg, fds, ppl, pch = csv_open()

# Read csv to SQL table
sql_tools.csv_to_table(db, bdg, 'budgets', ['INTEGER', 'REAL'])
sql_tools.csv_to_table(db, fds, 'foods', ['INTEGER', 'TEXT', 'REAL', 'TEXT', 'BOOL'])
sql_tools.csv_to_table(db, ppl, 'people', ['INTEGER', 'TEXT', 'INTEGER', 'TEXT', 'INTEGER', 'BOOL'])
sql_tools.csv_to_table(db, pch, 'purchases', ['INTEGER', 'INTEGER', 'INTEGER', 'TEXT'])

# Close csv files
csv_close()

# Construct queries, read SQL table to csv
# while loop allowing for repeated choices
while True:
    print(menu_opt)
    menu_choice = input('\nType here: ')
    
    if menu_choice == 'CPD':
        pchs = pch_choice()
        
        # Use people.csv for name and ID, purchases.csv for day of
        # purchase and food ID, foods.csv for food ID and name
        
        if pchs == 0:
            continue
        
        elif pchs == 1:
            
            with open('cpd_A.csv', 'w') as output:
                sql_tools.select_to_csv(db, output, '''
                SELECT people.name, foods.name, day
                FROM people, purchases, foods
                WHERE people.person_id = purchases.person_id
                AND foods.food_id = purchases.food_id;''')
                
            print('\nSuccess!')
                        
        elif pchs == 2:
            
            with open('cpd_M.csv', 'w') as output:
                sql_tools.select_to_csv(db, output, '''
                SELECT people.name, foods.name, day
                FROM people, purchases, foods
                WHERE people.person_id = purchases.person_id
                AND foods.food_id = purchases.food_id
                AND people.membership = TRUE;''')
                
            print('\nSuccess!')
        
        elif pchs == 3: 
            
            with open('cpd_F.csv', 'w') as output:
                sql_tools.select_to_csv(db, output, '''
                SELECT people.name, foods.name, day
                FROM people, purchases, foods
                WHERE people.person_id = purchases.person_id
                AND foods.food_id = purchases.food_id
                AND foods.is_fruit = TRUE;''')
                
            print('\nSuccess!')
            
    elif menu_choice == 'CBP':
        pchs = pch_choice() 
        
        # Use budgets.csv for ID and budget, purchases.csv and foods.csv to
        # match food ID of purchased items to price
        
        if pchs == 0:
            continue 
        
        elif pchs == 1:
            
            with open('cbp_A.csv', 'w') as output:
                sql_tools.select_to_csv(db, output, '''
                SELECT budgets.person_id, budget, SUM(price * quantity)
                FROM budgets, foods, purchases
                WHERE budgets.person_id = purchases.person_id
                AND foods.food_id = purchases.food_id
                GROUP BY budgets.person_id;''')
            
            print('\nSuccess!')
        
        elif pchs == 2:
            
            with open('cbp_M.csv', 'w') as output:
                sql_tools.select_to_csv(db, output, '''
                SELECT budgets.person_id, budget, SUM(price * quantity)
                FROM people, budgets, foods, purchases
                WHERE budgets.person_id = purchases.person_id
                AND foods.food_id = purchases.food_id
                AND people.person_id = budgets.person_id
                AND people.membership = TRUE
                GROUP BY budgets.person_id;''')
            
            print('\nSuccess!')
        
        elif pchs == 3:
            
            with open('cbp_F.csv', 'w') as output:
                sql_tools.select_to_csv(db, output, '''
                SELECT budgets.person_id, budget, SUM(price * quantity)
                FROM budgets, foods, purchases
                WHERE budgets.person_id = purchases.person_id
                AND foods.food_id = purchases.food_id
                AND foods.is_fruit = TRUE
                GROUP BY budgets.person_id;''')
            
            print('\nSuccess!')            
        
        
    elif menu_choice == 'CVFD':
        pchs = pch_choice()  
        
        # Use people.csv for name and number of visits, purchases.csv for food
        # ID purchased and day of purchase, foods.csv for name of food and food
        # ID       
        
        if pchs == 0:
            continue        
        
        elif pchs == 1:
            
            with open('cvfd_A.csv', 'w') as output:
                sql_tools.select_to_csv(db, output, '''
                SELECT people.name, num_visits, foods.name, day
                FROM people, purchases, foods
                WHERE people.person_id = purchases.person_id
                AND purchases.food_id = foods.food_id;''')
                
            print('\nSuccess!')
            
        elif pchs == 2:
            
            with open('cvfd_M.csv', 'w') as output:
                sql_tools.select_to_csv(db, output, '''
                SELECT people.name, num_visits, foods.name, day
                FROM people, purchases, foods
                WHERE people.person_id = purchases.person_id
                AND purchases.food_id = foods.food_id
                AND people.membership = TRUE;''')
                
            print('\nSuccess!')                        
            
        elif pchs == 3:
            
            with open('cvfd_F.csv', 'w') as output:
                sql_tools.select_to_csv(db, output, '''
                SELECT people.name, num_visits, foods.name, day
                FROM people, purchases, foods
                WHERE people.person_id = purchases.person_id
                AND purchases.food_id = foods.food_id
                AND foods.is_fruit = TRUE''')
                
            print('\nSuccess!')                        
            
    elif menu_choice == 'E':
        db.close()
        raise SystemExit
    
    else:
        print('\nInvalid input. Try again.')
