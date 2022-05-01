#ask user to enter number between 10 and 20. if it's between range, show 'Thank you!', otherwise print 'Wrong answer'
number = int(input('Please enter a number between 10 and 20: '))
if (number >= 10 and number <= 20) :
    print('Thank you :)')
else :
    print('Wrong answer :(')