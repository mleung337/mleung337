from os import name, system
from secrets import choice
from time import sleep


def generate_set(start, stop):
    '''Return set of characters using start and stop provided as unicode
    decimals.'''
    
    return {chr(a) for a in range(start, stop + 1)}


def get_length():
    '''Returns user input as an integer representing password length.'''
    clear()
    
    while True:
        print(LEN_SEL)
        user_input = input('> ')
        i = 0
        
        for tog in toggles:
            if tog:
                i += 1
        
        if user_input.isnumeric():
            if int(user_input) >= i:
                return int(user_input)
            
            else:
                clear()
                print(
'''
ERROR: Length too short to contain a character from all chosen character sets.
''')
        
        else:
            clear()
            print('\nERROR: Pick an integer.\n')
            
            
def content_check(string):
    '''Returns True or False depending on if user input has at least one
    character from each set given.'''
    
    ucases_bool, lcases_bool, nums_bool, specs_bool = toggles
    ucases_bool = not ucases_bool
    lcases_bool = not lcases_bool
    nums_bool = not nums_bool
    specs_bool = not specs_bool
    
    for char in string:
        if char in UCASES and toggles[0]:
            ucases_bool = True
            
        elif char in LCASES and toggles[1]:
            lcases_bool = True
            
        elif char in NUMS and toggles[2]:
            nums_bool = True
            
        elif char in SPECS and toggles[3]:
            specs_bool = True
            
    return ucases_bool and lcases_bool and nums_bool and specs_bool


def password_menu():
    '''Password creation menu.
    If creating a password, returns a random password that does not contain
    characters from the character blacklist.
    If creating a character blacklist, modifies set 'blacklist' based on user
    input.
    '''
    
    while True:
        print(PASSWORD_MENU)
        user_input = input('> ')
        
        if user_input == '1':
            password = get_password()
            return password
        
        elif user_input == '2':
            toggle_sets()
        
        elif user_input == '3':
            modify_blacklist()
            
        elif user_input == '4':
            clear()
            print(HELP_MENU)
            
        elif user_input == '5':
            clear()
            break
        
        else:
            clear()
            print('\nERROR: Pick a menu option.\n')
            
            
def get_password():
    '''Returns randomly generated password.'''
    
    exists_set = False
    
    for tog in toggles:
        if tog:
            exists_set = True
    
    if exists_set:
        length = get_length()
        chars = set()
        
        for i in range(4):
            if toggles[i]:
                chars.update(CHAR_LIST[i])
                
        gen_chars = list(chars - blacklist)
        contains_char = False
        
        while not contains_char:
            password = ''
            
            while len(password) < length:
                password += choice(gen_chars)
                
            contains_char = content_check(password)
        
        clear()
        print('\nYour new password is ' + password + '.\n')        
        return password
    
    else:
        clear()
        print('\nERROR: Choose at least one character set.\n')
            
            
def toggle_sets():
    clear()
    
    while True:
        print(TOGGLE_SETS.format(bool_to_on[toggles[0]],
                                 bool_to_on[toggles[1]],
                                 bool_to_on[toggles[2]],
                                 bool_to_on[toggles[3]]))
        user_input = input('> ')
        
        if user_input in ['1', '2', '3', '4']:
            i = int(user_input) - 1
            toggles[i] = not toggles[i]
            clear()
            
        elif user_input == '5':
            clear()
            break
            
        else:
            clear()
            print('\nERROR: Pick a menu option.\n')            
            
            
def modify_blacklist():
    '''Modifies the set 'blacklist' by either updating it or emptying it.'''
    
    clear()
    print(MOD_BLACKLIST)
    user_input = input('> ')
    
    if user_input == '!CLEAR':        
        blacklist.clear()
        clear()
        print('\nBlacklist cleared.\n')
        
    elif user_input == '!BACK':
        pass
        
    else:
        blacklist.update(set(i for i in user_input))
        clear()
        print('\nBlacklist modified.\n')           
    
            
def clear():
    if name == 'nt':
        _ = system('cls')    


MAIN_MENU = '''
-<>- PASSWORD GENERATOR -<>-
1. Create new password
2. Store current password
3. About
4. Exit
'''

ABOUT = '''
<> About Section <>
A cryptographically strong password generator.
'''

PASSWORD_MENU = '''
<> Password Creation Menu <>
1. Create password
2. Toggle character sets
3. Blacklist characters
4. Help
5. Back
'''

LEN_SEL = '''
<> Password Length Selection <>
Enter a length below. Make sure it is long enough to contain at least one
character from each of your chosen character sets.
'''

TOGGLE_SETS = '''
<> Character Set Toggle Menu <>
Toggle the character sets you want to include in password generation.
By default, all character sets are included.

1. Toggle uppercase letters ({})
2. Toggle lowercase letters ({})
3. Toggle numbers ({})
4. Toggle special characters ({})
5. Back
'''

MOD_BLACKLIST = '''
<> Character Blacklist Menu <>
Enter a sequence of characters you want to add to the blacklist below.
Enter !CLEAR to empty the blacklist, or !BACK to go back to the password
creation menu.
'''

HELP_MENU = '''
<> Password Creation Tips <>
Ideally, the length of your password should be between 8-22 characters.
To maximize randomness, and thus the hardiness, of your password, include as
many kinds of characters as possible.

If your password cannot have certain character sets (i.e. special characters),
use the toggle character sets feature to remove those character sets from
password generation.

If your password cannot have certain characters but not entire character sets
(i.e. just tildes), use the blacklist feature to remove those characters from
password generation.
'''

UCASES = generate_set(ord('A'), ord('Z'))
LCASES = generate_set(ord('a'), ord('z'))
NUMS = generate_set(ord('0'), ord('9'))

ADD_DICT = {'!':'/', ':':'@', '[':'`', '{':'~'}
SPECS = set()
for key in ADD_DICT:
    SPECS.update(generate_set(ord(key), ord(ADD_DICT[key])))

CHAR_LIST = [UCASES, LCASES, NUMS, SPECS]

bool_to_on = {True:'On', False:'Off'}
toggles = [True, True, True, True]
blacklist = set()

while True:
    print(MAIN_MENU)
    user_input = input('> ')
    
    if user_input == '1':
        clear()
        current_password = password_menu()
        
    elif user_input== '2':
        clear()
        print('\nThis feature has not been implemented yet.\n')
    
    elif user_input == '3':
        clear()
        print(ABOUT)
        
    elif user_input == '4':
        clear()
        print('\nExiting...\n')
        sleep(3)
        break
    
    else:
        clear()
        print('\nERROR: Pick a menu option.\n')