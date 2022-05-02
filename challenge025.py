first_name = input('Enter your first name: ')

if(len(first_name) < 5) :
    surname = input('Enter your surname: ')
    print((first_name + surname).upper())
else :
    print(first_name.lower())