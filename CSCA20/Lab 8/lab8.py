# Import csv, matplotlib, and numpy
import csv
import matplotlib.pyplot as plt
import numpy as np

# Function to open csv and map one column to another
def csv_dict(csv_name, key_title, val_title):
    
    try:
        open(csv_name, 'r')

        with open(csv_name, 'r') as csv_file:
            read_csv = csv.DictReader(csv_file)
            csv_dict = {}

            for row in read_csv:
                csv_dict.update({row[key_title]:row[val_title]})
    
            return csv_dict, True 
    
    except:
        print('\nInvalid input. Try again.')
        return None, False

menu = '''\n=== UTSC Purchase Tracker ===
BDG = Add budget file
PRC = Add prices file
PCH = Add purchases file
G = Generate graph
E = Exit program
Must add all three files to graph.'''

# Variables tracking if all files have been added
got_bdg = False
got_prc = False
got_pch = False

while True:
    print(menu)
    menu_input = input('\nType here: ')
    
    if got_bdg and got_prc and got_pch and menu_input == 'G':
        
        # Name tuple for x-label
        names = tuple(bdg_dict.keys())
        
        # Open purchases file for reading and create dictionary
        with open(pch_file, 'r') as pch:
            pch_dicts = {}
            day = pch.readline().strip().replace('DAY:', '')
            pch_dicts[day] = {}
                    
            for row in pch:
                        
                if 'DAY:' in row:
                           
                    for name in names:
                                
                        if name not in pch_dicts[day].keys():
                            pch_dicts[day][name] = []
                            
                    day = row.strip().replace('DAY:', '')
                    pch_dicts[day] = {}
                        
                else:
                            
                    for name in names:
                                
                        if name not in pch_dicts[day].keys():
                            pch_dicts[day][name] = []
                                    
                    user_name = row.strip().split(':')[0]
                    user_data = row.strip().split(':')[1].split(',')
                            
                    if day not in pch_dicts.keys():
                        pch_dicts[day] = {user_name: user_data}
                            
                    else:
                        pch_dicts[day].update({user_name: user_data})
            
            # Sorts dictionary (Works only for Python 3.7 onwards)
            for day in pch_dicts:
                pch_dicts[day] = dict(sorted(pch_dicts[day].items()))
        
        for day in pch_dicts:
            
            # Calculate how many of each food each person bought in order of
            # name tuple
            counts = {}
            
            for food in prc_dict.keys():
                counts[food] = []
                
                for user_pch in pch_dicts[day].values():
                    
                    counts[food].append(user_pch.count(food))
            
            # Convert counts to dictionary of arrays instead of lists
            weight_counts = {}
            
            for food in counts:
                weight_counts[food] = np.array(counts[food])
            
            # Array of bottom value - array of zeros
            bottom = np.zeros(len(names))
            
            # Create new figure
            plt.figure()
            
            # Plots new bar where bottom is height of previous value
            for weight_count in weight_counts.values():
                plt.bar(names, weight_count, bottom = bottom)
                bottom += weight_count
            
            plt.xlabel('Users')
            plt.ylabel('Number of purchases')
            plt.title('Purchases per User on {0}'.format(day))
            plt.legend(prc_dict.keys())
            plt.show()
        
        wkly_count = {}
                
        # Count how many times a type of food appears for all days        
        for food in prc_dict.keys():
            wkly_count[food] = [0] * len(names)
            
            for day in pch_dicts:
                
                for i, name in zip(range(len(names)), names):
                
                    wkly_count[food][i] += pch_dicts[day][name].count(food)
                    
        wkly_dict = {}
        
        # Calculate total expenditure multiplying price by number purchased
        for food in prc_dict:
            wkly_dict[food] = [i * float(prc_dict[food].strip('$')) for i in wkly_count[food]]
        
        wkly_costs = [0] * len(names)
        
        for costs in wkly_dict:
            
            for i in range(len(names)):
                wkly_costs[i] += wkly_dict[costs][i]

        wkly_bdg = [float(i.strip('$')) for i in bdg_dict.values()]
        
        # Creates new figure
        plt.figure()
        
        # Creates range of arrays for position of label
        x_ax = np.arange(len(names))
        
        # Plots bar graphs that are side by side by offsetting position of label
        # by some amount
        plt.bar(x_ax - 0.2, wkly_costs, 0.4, label = 'Expenditure')
        plt.bar(x_ax + 0.2, wkly_bdg, 0.4, label = 'Budget')
        plt.xticks(x_ax, names)
        plt.xlabel('Users')
        plt.ylabel('Dollars ($)')
        plt.title('Expenditure vs. Budget per User')
        plt.legend()
        plt.show()
        
    elif menu_input == 'BDG':
        bdg_dict, got_bdg = csv_dict(input('\nFile name here: '), 'name', 'budget')
        
    elif menu_input == 'PRC':
        prc_dict, got_prc = csv_dict(input('\nFile name here: '), 'food item', 'price')
    
    elif menu_input == 'PCH':
        pch_file = input('\nFile name here: ')
            
        try:
            open(pch_file, 'r')
            got_pch = True
            
        except:
            print('\nInvalid input. Try again.')
        
    elif menu_input == 'E':
        raise SystemExit
    
    else:
        print('\nInvalid input. Try again.')