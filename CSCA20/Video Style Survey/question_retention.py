'''
You are a member of the Universal Travel Statistics Corporation [UTSC],
and you are tasked with analyzing the most popular travel destinations among individuals.

Write a function that takes one argument: a dictionary where the keys are person names
and the values are lists representing the countries they have traveled to.
Your function should return a list of names of the countries that have been visited the most.

If there are ties (more than one country with the same maximum visit count),
return all the tied countries in the list.

Example:
travel_history = {'Alice': ['France', 'Italy', 'Spain'],
                  'Bob': ['Germany', 'France', 'Spain', 'Italy'],
                  'Charlie': ['USA', 'Canada', 'Mexico', 'France']}
print("Most visited country/countries: " + str(find_most_visited_country(travel_history)))
>>> Most visited country/countries: ['France', 'Spain']

Concepts you might need:
  - Dictionaries (with lists as values)
  - Elemental for loops
  - If statements
'''
travel_history = {'Alice': ['France', 'Italy', 'Spain'],
                  'Bob': ['Germany', 'France', 'Spain', 'Italy'],
                  'Charlie': ['USA', 'Canada', 'Mexico', 'France']}
def find_most_visited_country(travel_history):
    ''' PLEASE WRITE BELOW THIS COMMENT '''
    
    countries_visited = []
    
    for person in travel_history:
        
        for country in travel_history[person]:
            
            countries_visited.append(country)
            
    most_visited = []
    
    country_visits = {}
    
    for country in countries_visited:
        
        if country not in country_visits:
            
            country_visits[country] = countries_visited.count(country)
        
    for country in country_visits:
            
        if len(most_visited) == 3:
            break
        
        elif country_visits[country] == max(country_visits.values()) and country_visits[country] != 0:
                
            most_visited.append(country)
            country_visits[country] = 0
                
    return most_visited
        