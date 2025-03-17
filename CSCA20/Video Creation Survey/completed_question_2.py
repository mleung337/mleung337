# Matthew Leung

''' You are about to go to your supervisor to ask for a raise.
Having not recieved a raise for the past 5 years, you wish to determine
what a fair salary is when accounting for inflation.

Write a program that takes your current annual salary, and the inflation rates (in percentage)
for the last 5 years and prints the new salary you should request, ROUNDED DOWN TO AN INTEGER.

You can round down by casting the value to an integer.

Don't forget to indicate to the user how they should input the GPAs by using a prompt when 
asking for input, as follows:
    input("some prompt for the user")

Example:
    If your current salary is: 40000
    If the inflation rates for the last 5 years are: 2.27, 1.95, 0.72, 3.40, 6.80
    The requested salary should be: 46387

FOR YOUR SUBMISSION TO BE GRADED CORRECTLY, YOUR OUTPUT SHOULD ONLY CONTAIN THE NEW SALARY
(For the example above, the output should be just '46387')

Here are the concepts you might need to use to solve this question:
    - Accumulators
    - Counted for loops

Don't forget to check your code by running a few examples, including the one
given above. '''

''' PLEASE WRITE BELOW THIS COMMENT '''

current_salary = float(input('What is your current salary? '))
avg_inflation_rate = 0

inflation_rate = float(input('What is the inflation rate from 1 year ago? '))
avg_inflation_rate += inflation_rate / 100

for i in range(4):
    inflation_rate = float(input('What is the inflation rate from ' + str(i + 2) + ' years ago? '))
    avg_inflation_rate += inflation_rate / 100
    
avg_inflation_rate = avg_inflation_rate / 5
new_salary = int(current_salary * (1 + avg_inflation_rate))
print(new_salary)