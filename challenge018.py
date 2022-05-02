# ask the user to enter a number. If it's under 10, print Too low. If it's between 10 and 20, print Correct
#otherwise print Too high
number = int(input('Please enter a number: '))

if (number < 10) :
    print('Too low')
elif (number >= 10 and number <= 20) :
    print('Correct')
else :
    print('Too high')