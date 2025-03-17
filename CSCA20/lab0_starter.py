# Matthew Leung

#This is a python file... everything starting with the # symbol is a comment. It's just for humans to read. The rest is the code that python will run.

#PART 1:
#let's ask the user for their names, store those names in variables, and then print them back to the user. Run this code and try to follow what it's doing
first = input("What is your first name? ")
surname = input("What is your surname? ")
print("Your name is: " + first + " " + surname)

#PART2
#let's do some basic calculations with the values given to us by a user. Note that we will need to tell python that the input is in integers (int), otherwise it won't calculate properly
num_lectures = int(input("How many lectures are in the course? "))
num_hours = int(input("How many hours is each lecture? "))
num_words = int(input("How many words does Brian say per hour? "))

#now you need to replace the 0 in the code below with a calculation for the total number of words
total_words = num_lectures * num_hours * num_words

#note here that we need to convert total_words back to a string (str) so python knows to print it
#properly (don't worry if this part doesn't totally make sense to you yet, we'll learn a lot more
#about this in lecture)
print("Brian will say approximately " + str(total_words) +
      " words during this course")

#PART 3
#okay... now it's your turn... ask the user for something, do something with it, and print the result
#have fun with it...

# Gets input, slices and prints it backwards
u_input = input('input:')
u_output = u_input[::-1]
print('output:' + u_output)