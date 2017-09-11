current_hours = 14;
current_minutes = 34;
current_seconds = 42;

# Write a program that prints the remaining seconds (as an integer) from a
# day if the current time is represented bt the variables

currenthours_insecounds = current_hours*60*60
currentminutes_insecounds = current_minutes*60

remaining_seconds = currenthours_insecounds+currentminutes_insecounds+current_seconds
# print((24-current_hours)*60*60 + (60-current_minutes)*60 + 60-current_se_conds)
print(remaining_seconds)

