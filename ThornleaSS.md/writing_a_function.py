# Matthew Leung

def letterCount():
    '''Asks user for a sentence and counts number of letters in sentence'''
    string = input("Enter a sentence here, and the number of a's will be counted. ")
    letter_numbers = string.count('a')
    return letter_numbers

print(f"There are {letterCount()} a's in your sentence.")
