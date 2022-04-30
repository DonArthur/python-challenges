#ask user for their name and age. add 1 to their age and display [Name] next birthday you will be [new age]

name = input('Your name is: ')
current_age = int(input('Your current age is: '))
new_age = current_age + 1

print(name + ', next birthday you will be ' + str(new_age))