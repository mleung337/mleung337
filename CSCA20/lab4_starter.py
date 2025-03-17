
def AorR():
    
    while True:
        sel = input('A for all days, R for range of days: ')
        
        if sel == 'A':
            return 1
        
        elif sel == 'R':
            return None
        
        else:
            print('Invalid input. Please try again.')

def floatcheck():
        
    while True:
        var = input('Type here: ')
    
        try:
            float(var)
            return float(var)
        
        except:
            print('Invalid input. Please try again.')
            
def intcheck():
    
    while True:
        var = input('Type here: ')
    
        try:
            int(var)
            return int(var)
        
        except:
            print('Invalid input. Please try again.')

plastic_removed = []
day = 1

while True:
    print("""
    A = Add data
    T = Get total kg of plastic removed
    O = Get number of overload days
    M = Get maximum within range of days
    m = Get minimum within range of days
    E = End program
    """)
    menu_option = input('Choose an option: ')
    
    if menu_option == 'A':
        print('Enter kg of plastic removed or type "E" to exit.')
        
        while True:
            data = input('Day ' + str(day) + ': ')
            
            if data == 'E':
                break
            
            else:
                
                try:
                    float(data)
                    plastic_removed.append(float(data))
                    day += 1
                
                except:
                    print('Invalid input. Please try again.')
                
    elif menu_option == 'T':
        total = 0
        Tchoice = AorR()
        
        if Tchoice == 1: 
            
            for i in range(len(plastic_removed)):
                total += plastic_removed[i]
                
            print('Total removed: ' + str(total) + ' kg.')
            raise SystemExit
            
        else:
            
            while True:
                print('Enter a start day.')
                start_pos = intcheck()
                print('Enter an end day.')
                end_pos = intcheck()
                
                if (start_pos >= 1) and (end_pos <= len(plastic_removed)) and (start_pos < end_pos)and (end_pos - start_pos >= 7):
                    
                    for i in range(start_pos - 1, end_pos):
                        total += plastic_removed[i]
                        
                    print('Total removed: ' + str(total) + ' kg.')
                    raise SystemExit
                
                else:
                    print('Invalid dates. Please try again.')                
                    
    elif menu_option == 'O':
        oload_days = 0
        Ochoice = AorR()
        print('Enter max kg per rig.')
        threshold = floatcheck()
        
        if Ochoice == 1:
            
            for i in range(len(plastic_removed)):
                
                if plastic_removed[i] > threshold:
                    oload_days += 1
                    
            print('Number of overload days: ' + str(oload_days))
            raise SystemExit
            
        else:
            
            while True:
                print('Enter a start day.')
                start_pos = intcheck()
                print('Enter a end day.')
                end_pos = intcheck()
                
                if (start_pos >= 1) and (end_pos <= len(plastic_removed)) and (start_pos < end_pos) and (end_pos - start_pos >= 7):
                    
                    for i in range(start_pos - 1, end_pos):
                        
                        if plastic_removed[i] > threshold:
                            oload_days += 1
                        
                    print('Number of overload days: ' + str(oload_days))
                    raise SystemExit
                
                else:
                    print('Invalid dates. Please try again.')                
                
    elif menu_option == 'M':
        
        while True:
            print('Enter a start day.')
            start_pos = intcheck()
            print('Enter a end day.')
            end_pos = intcheck()
            
            if (start_pos >= 1) and (end_pos <= len(plastic_removed)) and (start_pos < end_pos) and (end_pos - start_pos >= 7):
                maxim = 0
                
                for i in range(start_pos - 1, end_pos):
                    
                    if plastic_removed[i] > maxim:
                        maxim = plastic_removed[i]
                        
                print('Maximum plastic removed was ' + str(maxim) + ' kg.')
                raise SystemExit
            
            else:
                print('Invalid dates. Please try again.')            
        
    elif menu_option == 'm':
        
        while True:
            print('Enter a start day.')
            start_pos = intcheck()
            print('Enter a end day.')
            end_pos = intcheck()
            
            if (start_pos >= 1) and (end_pos <= len(plastic_removed)) and (start_pos < end_pos) and (end_pos - start_pos >= 7):
                minim = plastic_removed[start_pos - 1]
            
                for i in range(start_pos, end_pos):
                    
                    if plastic_removed[i] < minim:
                        minim = plastic_removed[i]
                        
                print('Minimum plastic removed was ' + str(minim) + ' kg.')
                raise SystemExit
            
            else:
                print('Invalid dates. Please try again.')            
    
    elif menu_option == 'E':
        raise SystemExit
    
    else:
        print('Invalid input. Please try again.')