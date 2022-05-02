#ask the user to enter their firstname and surname, join and print the name with the length
first_name = input('Enter your first name: ')
surname = input('Enter your surname: ')
full_name = first_name + ' ' + surname

print('Your full name is ' + full_name + ', the length is ' + str(len(full_name)))