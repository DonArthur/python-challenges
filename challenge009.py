#ask a number of days and show how many hours, minutes, and seconds in that number of days
number_of_days = int(input('Type a number of days: '))
hours = number_of_days * 24
minutes = hours * 60
seconds = minutes * 60

print(str(number_of_days) + ' in hours: ' + str(hours) + ', in minutes: ' + str(minutes) + ', in seconds: ' + str(seconds))