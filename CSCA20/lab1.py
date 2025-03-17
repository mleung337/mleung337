# Matthew Leung

# Asks for given name
given_name = input ('Enter student given name: ') [:10]

# Asks for family name
family_name = input ('Enter student family name: ') [:10]

# Asks for student number
student_num = input ('Enter the student number for ' + given_name + ' ' + family_name + ': ')

# Asks for course codes
courses = []
num_courses = int(input('Number of courses this semester: '))
for i in range(num_courses):
    course_code = input('Enter course code #' + str(i + 1) + ': ')
    courses.append(course_code)

# Asks for grade values, immediately adds them to avg then divides by number of courses
avg = 0
for i in range(num_courses):
    grade = float(input('Enter grade for ' + courses[i] + ': '))
    avg += grade
    
avg = str(avg/num_courses)

print(family_name + ', \n' + given_name + ', \n' + student_num + ', \n' + avg)

