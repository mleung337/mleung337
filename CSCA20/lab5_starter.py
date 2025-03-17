def matches_char(input_char, template_char):
    #INPUT:
    #    input_character and template_character are single character strings
    #OUTPUT:
    #    return True if any of the following conditions are met (returns
    #    False otherwise):
    #        - input_character and template_character are the same
    #        - template_character is '#' and input_character is a number
    #        - template_character is '&' and input_character is a letter
    
    if input_char == template_char:
        return True
    
    elif template_char == '#' and input_char.isdecimal():
        return True
    
    elif template_char == '&' and input_char.isalpha():
        return True
    
    elif template_char == '$' and not (input_char.isdecimal() or input_char.isalpha()):
        return True
    
    else:
        return False

def matches_str(input_str, template_str):
    #INPUT:
    #    input_string and template_string are strings of characters of the same
    #    length
    #OUTPUT:
    #    return True if: for every position p from 0 to the length of the strings,
    #    one of the following conditions is met:
    #        - input_string[p] and template_string[p] are the same
    #        - template_string[p] is '#' and input_string[p] is a number
    #        - template_string[p] is '&' and input_string[p] is a letter
    
    for p in range(len(input_str)):
        
        if matches_char(input_str[p], template_str[p]) == False:
            return False
        
    return True

    #NOTE: if there's a mismatch early on, the code should not continue to check
    #the rest of the string
    
def format_match(input_str, template_str, str_list):
   
    # Checks if input_str and template_str are of same length and if matches template using matches_str
    if len(input_str) == len(template_str) and matches_str(input_str, template_str):
        # Appends input_str to str_list if true
        str_list.append(input_str)
        return True
    
    else:
        # Error message if false
        print('\nInvalid format. Try again.\n')
        return False

phone_template = "(###)###-####"
donor_id_template = "&&####"
time_template = "##:##&M"

#MAKE YOUR MENU HERE

# Menu, as well as format specifications
print("""   === UTSC ===
= Donor Database =

Enter your phone number in format (###)###-####,
donor ID in format XX####,
and booking time in format ##:##AM/PM.
""")

# Creates lists for donor details
phones = []
donor_ids = []
times = []

# add variable for if user wants to add more variables, will stop loop if false
add = True

# donor_num variable to count how many donors were added
donor_num = 0

# while loop for adding donor details
while add:

    # Ask for phone number, donor ID, and booking time
    phone = input('Phone number: ')
    donor_id = input('Donor ID: ')
    time = input('Booking time: ')
    
    # Uses format_check function to check formats
    phone_check = format_match(phone, phone_template, phones)
    if not phone_check:
        continue
    
    donor_id_check = format_match(donor_id, donor_id_template, donor_ids)
    if not donor_id_check:
        continue
    
    time_check = format_match(time, time_template, times)
    if not time_check:
        continue
    
    elif time_check and ((int(time[3] + time[4]) >= 60) or (time[5] not in ['A', 'P'])):
        print('Invalid format. Try again.')
        continue
    
    # while loop for if user wants to add another donor
    while True:
        add_YN = input('\nAdd another donor? (Y/N) ')
        
        if add_YN == 'N':
            add = False
            break
        
        elif add_YN == 'Y':
            break
        
        else:
            print('\nBad input. Try again.\n')    