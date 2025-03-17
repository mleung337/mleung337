# Matthew Leung

''' July was the hottest recorded month in history. The average
daytime temperature was 26 degrees celsius. You want to compare
this average to this week.

Write a program that takes the daytime temperature for the last 7 days and prints the
average tempereture of the last week. Don't forget to indicate to the user how they
should input the GPAs by using a prompt when asking for input, as follows:
    input("some prompt for the user")

Example:
    If the temperatures given by the user are: 23.2, 24.5, 22, 25, 26.3, 21.4, 18.6
    The expected output is: 23.0

FOR YOUR SUBMISSION TO BE GRADED CORRECTLY, YOUR OUTPUT SHOULD ONLY CONTAIN THE AVERAGE TEMPERATURE
(For the example above, the output should be just '23.0')

Here are the concepts you might need to use to solve this question:
    - Accumulators
    - Counted for loops

Don't forget to check your code by running a few examples, including the one
given above. '''

''' PLEASE WRITE BELOW THIS COMMENT '''

avg_temp = 0 
print('Input the daytime temperatures for the last 7 days')

for i in range(7):
    temp = float(input('Day ' + str(i + 1) + ': '))
    avg_temp += temp
    
avg_temp = avg_temp / 7
print(avg_temp)

    