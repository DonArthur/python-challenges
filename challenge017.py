#ask for the user's age. if age >= 18, print You can vote. If age = 17, print you can learn to drive
#if they are 16, print You can buy a lottery ticket. If age < 16, print You can go Trick-or-Treating
age = int(input('Please tell me your age: '))

if (age >= 18) :
    print('You can vote')
elif (age == 17) :
    print('You can learn to drive')
elif (age == 16) :
    print('You can buy a lottery ticket')
elif (age < 16) :
    print('You can go Trick-or-Treating')