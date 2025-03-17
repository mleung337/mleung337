def valid_file(user_input):
    
    try:
        open(user_input, 'r')
        
        file = open(user_input,'r')
        parties = file.readline().strip().split(',')

        districts = set()
        errors = set()
        
        for line in file:
            
            if 'REPORTING:' in line:
                district = line.replace('REPORTING:','')
                
                if district in districts:
                    errors.add(1)
                
                else:
                    districts.add(district)
        
            else:
                votes = line.split(',')
                
                if ',' in votes:
                    errors.add(2)
                
                else:
                    
                    try:
                        int(votes[1])
                        
                        if votes[0] not in parties:
                            errors.add(3)                           
                        
                    except:
                        errors.add(4)
                        
        file.close()
        return errors
                    
    except:
        print('\nFile error. Try again.')
        
def read_file(user_input):
    
    file = open(user_input, 'r')
    parties = file.readline().strip().split(',')
    party_dict = {}
    
    for party in parties:
        party_dict[party] = []
    
    anti_halifax = False
    for line in file:
        
        if 'REPORTING:' in line:
            
            if 'Halifax' in line:
                anti_halifax = True
            
            else:
                anti_halifax = False
            
        else:
            party_vote = line.split(',')
            party = party_vote[0]
            vote = int(party_vote[1])
            
            if anti_halifax == False:
                party_dict[party].append(vote)
    
    file.close()       
    return party_dict

menu = """\n=== UTSC Election Tracking Menu===
P = Get current party list
V = Validate file data
A = Add file data
TA = Get total for all parties
TS = Get total for specific party
E = Exit program"""

party_dict = {}

while True:
    print(menu)
    menu_input = input('\nType here: ')
    
    if menu_input == 'P':
        
        if len(party_dict) == 0:
            print('\nNo parties added. Add files first.')
            
        else:
            print('\nParties: ')
            
            for party in party_dict.keys():
                print(party)
            
    elif menu_input == 'V': 
        file_name = input('\nFile name here: ')
        file_validity = valid_file(file_name)
            
        if file_validity != None:
                
            if len(file_validity) == 0:
                print('\nFile is in valid format.')
                
            else:
                print('\nFile is in invalid format.')
                
                if 1 in file_validity:
                    print('\nAt least one district repeats one or more times.')
                
                if 2 in file_validity:
                    print('\nParty name and vote improperly separated in at least one line.')
                    
                if 3 in file_validity:
                    print('\nUnlabelled party in at least one line.')
                    
                if 4 in file_validity:
                    print('\nVote is not integer in at least one line.')                
            
    elif menu_input == 'A':
        file_name = input('\nFile name here: ')
        file_validity = valid_file(file_name)
            
        if file_validity != None:
                
            if len(file_validity) == 0:
                print('\nFile is in valid format.\nVotes have been updated.')
                party_dict.update(read_file(file_name))
                
            else:
                print('\nFile is in invalid format.')
                
                if 1 in file_validity:
                    print('\nAt least one district repeats one or more times.')
                
                if 2 in file_validity:
                    print('\nParty name and vote improperly separated in at least one line.')
                    
                if 3 in file_validity:
                    print('\nUnlabelled party in at least one line.')
                    
                if 4 in file_validity:
                    print('\nVote is not integer in at least one line.')
    
    elif menu_input == 'TA':
        
        for party in party_dict:
            print('\n{0} got {1} votes.'.format(party, sum(party_dict[party])))
    
    elif menu_input == 'TS':
        party_choice = input('Party name here: ')
            
        if party_choice in party_dict:
            print('\n{0} got {1} votes.'.format(party_choice, sum(party_dict[party_choice])))
            
        else:
            print('\nParty name not found. Try again.')
        
    elif menu_input == 'E':
        raise SystemExit
        
    else:
        print('\nInvalid input. Try again.')