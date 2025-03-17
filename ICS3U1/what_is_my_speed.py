# Matthew Leung

time_in_minutes = 43.5
time_in_hours = time_in_minutes / 60

km_run = 10
km_per_mile = 1.61
mile_run = km_run / km_per_mile

avg_hpm_time = time_in_hours / mile_run
avg_mph_speed = mile_run / time_in_hours
print("Let's say you ran a 10 km race in 43 minutes and 30 seconds. \nYour average time would have been", avg_hpm_time, "in hours per mile, while your average speed would have been", avg_mph_speed, "miles per hour.")
