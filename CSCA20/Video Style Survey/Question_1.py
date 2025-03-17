'''You are a part of the Universal Temperature Seruveillance Corp [UTSC]
and you are responsible to create a system to find the most extreme temperatures.

Write a function that takes one argument: a dictinary where the keys are names of some heavily populated cities
and for each city the corresponding value is a list of average daytime temperatures for the last week of that city.
 Your function must return the highest and lowest temperatures (in that order) as a list.

Example:
    temperatures = {'Adelaide': [17, 18, 17, 21, 24, 22, 19], 'Toronto': [14, 7, 7, 6, 4, 11, 15]}
    print("Extreme temperatures of the past week: " + str(get_extremes(temperatures)))
    >>> Extreme temperatures of the past week: [24, 4]

Here are the concepts you might need to solve this question:
    - Dictionaries
    - Elemental for loops
    - If statements

Don't forget to check your code by running a few examples, including the one
given above.
'''
temperatures = {'Adelaide': [17, 18, 17, 21, 24, 22, 19], 'Toronto': [14, 7, 7, 6, 4, 11, 15]}
def get_extremes (temperatures):
    ''' PLEASE WRITE BELOW THIS COMMENT '''
    
    # INPUT:
    # Dictionary where key is city name and value is list of temperatures
    # OUTPUT:
    # List where first element is maximum of all cities, second element is
    # minimum of all cities
    
    # Create a maximum and minimum temperature set to values for comparison
    max_temp = 0
    min_temp = 100
    
    # Iterate through each element in the dictionary
    for city in temperatures:
        
        # Iterate through the city's corresponding list
        for temp in temperatures[city]:
            
            # Compare values of each element of the list to the max_temp and
            # min_temp variables
            if max_temp < float(temp):
                
                # If max_temp is less than the current element in the list,
                # replace it with that element
                max_temp = float(temp)
                
            if min_temp > float(temp):
                
                # If min_temp is greater than the current element in the list,
                # replace it with that element
                min_temp = float(temp)
                
    # Create a list containing max_temp and min_temp
    extremes = [max_temp, min_temp]
    
    # Return the list
    return extremes
