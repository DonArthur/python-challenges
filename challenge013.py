#ask user to enter their age. if it's under 21, show 'Still too young', if it's 21 or over, show 'You are old enough'
number = int(input('Please tell me your age: '))

if (number < 21) :
    print("You're still too young")
else :
    print("You're old enough")