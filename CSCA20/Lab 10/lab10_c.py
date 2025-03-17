# Part C: Advanced Skills

import csv

def verify_file(string):
    
    print('\nEnter name of {0} file.'.format(string))
    
    while True:
        
        file_name = input('\nFile name here: ')
        
        try:
            
            open(file_name)
            
            return file_name
        
        except:
            
            print('\nInvalid file name. Try again.')

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

menu = '''\n=== UTSC ===
A = Add files
F = All foods purchased by a customer
D = All days on which a customer shopped
C = All customers who have spent past their budget
E = Exit program

Add files first before using other options.

Type here: '''

got_files = False

while True:
    
    menu_choice = input(menu)
    
    if menu_choice == 'A':
        
        pch_name = verify_file('purchases')
        ppl_name = verify_file('customers')
        fd_name = verify_file('foods')
        bdg_name = verify_file('budgets')
        
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
        
    elif menu_choice == 'E':
        
        print('\nClosing...')
        
        raise SystemExit
    
    else:
        
        print('\nInvalid menu choice. Try again.')