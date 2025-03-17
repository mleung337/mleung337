'''You are a TA at UTSC, and your professor has asked you to help them generate a list
of students that have passed the course.

Write a function that takes one argument: a dictinary where the keys are names of the students
and for each student the corresponding value is a list of their assignment grades (in percentage)
Your function must return a list of student names whose assignment average is at least 50%.

Example:
    grades = {'Abby': [70, 80, 90], 'Tom': [30, 70, 40]}
    print("Students that past the course: " + str(get_passing_students(grades)))
    >>> Students that passed the course: ['Abby']

Here are the concepts you might need to solve this question:
    - Dictionaries
    - Elemental for loops
    - If statements

Don't forget to check your code by running a few examples, including the one
given above.
'''
grades = {'Abby': [70, 80, 90], 'Tom': [30, 70, 40]}
def get_passing_students (grades):
    ''' PLEASE WRITE BELOW THIS COMMENT '''
    
    # INPUT:
    # Dictionary where keys are student names and corresponding values are list
    # of assignment grades
    # OUTPUT:
    # Return list of student names whose averages are at least 50
    
    # Create list for students whose grade is at least 50
    passing_students = []
    
    # Iterate through dictionary for each student
    for student in grades:
        
        # Add grades for each student to a sum variable, and divide to get
        # average
        grade_sum = 0
        
        for grade in grades[student]:
            
            grade_sum += grade
            
        grade_average = grade_sum / len(grades[student])
        
        # Check if student average is at least 50
        if grade_average >= 50:
            
            # Append to list
            passing_students.append(student)
            
    # Return list
    return passing_students