# Matthew Leung

leaving_time_hours = 6 + 52/60
print(f'You left at {"%.2f" % leaving_time_hours} AM to run.')

# Numbers taken from assignment
easy_pace_minpkm = 8 + 15/60
tempo_pace_minpkm = 7 + 12/60
print(f'Your easy pace time is {"%.2f" % easy_pace_minpkm} minutes, while your tempo pace time is {"%.2f" % tempo_pace_minpkm} minutes.')

# Numbers taken from assignment, paces multiplied by 2 for turn-around point, 60 for hour
running_time_minutes = 2 * (2 * easy_pace_minpkm + 3 * tempo_pace_minpkm)
running_time_hours = running_time_minutes/60

returning_time_hours = leaving_time_hours + running_time_hours
print(f'You would return at {"%.2f" % returning_time_hours} AM for breakfast.')
