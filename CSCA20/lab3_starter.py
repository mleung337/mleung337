#this will be our continue flag... if it's set to 'N', we're done, if it's
#set to 'Y' (or anything else really), we add more runners
cont = "Y"
#lists to hold our runners and their times, so runner[n] will be the name of
#the n'th place finisher and times[n] will be their time (in minutes)
runners = []
times = []

#loop until the user says they're out of runners to process
while(cont != "N"):
    #get the name and time of the next runner
    runner_name = input("Please enter name of next runner: ")
    runner_time = float(input("Please enter runner time: "))
    #add the name and time to their respective lists
    runners.append(runner_name)
    times.append(runner_time)
    #ask if the user is done
    cont = input("Any more runners to add? (Y/N) ")

average_time = 0
#NEED A LOOP HERE

# Adds all times in list times to average_time
for i in range(len(times)):
    average_time += times[i]

# Divides by number of elements in list times to get average
average_time = average_time/len(times)

print("Average time of all runners: " + str(average_time)) 


num_qualifiers = int(input("Enter number of runners who qualified: "))
average_time = 0
#NEED A LOOP HERE

# Adds times up to num_qualifiers value to average_time
for i in range(num_qualifiers):
    average_time += times[i]

# Divides by num_qualifiers to get average
average_time = average_time/num_qualifiers

print('Qualified runners:')

# Since times and runners are ordered fastest to slowest
# for loop to print runner names who qualified, starting from first element
for i in range(num_qualifiers):
    print(runners[i])
    
print("Average time for qualified runners: " + str(average_time))
    
cutoff_time = float(input("Enter cutoff time to qualify: "))
average_time = 0
#NEED A LOOP HERE

# Empty lists for qualifying runners and their times
qualifying_runners = []
qualifying_times = []

# for loop that appends qualifying runners under cutoff time to empty lists
for i in range(len(times)):
    
    if times[i] < cutoff_time:
        qualifying_runners.append(runners[i])
        qualifying_times.append(times[i])

# Adds all times in qualifying_times to average_time
for i in range(len(qualifying_times)):
    average_time += qualifying_times[i]

# Divides by number of elements in qualifying_times to get average
average_time = average_time/len(qualifying_times)
print('Qualifying runners:')

# for loop to print names of qualifying runners
for i in range(0, len(qualifying_runners), 3):
    print(qualifying_runners[i])
    
print("Average for qualifying runners: " + str(average_time))
