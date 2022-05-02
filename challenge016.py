#ask the user if it's raining, if it's yes, ask if it's windy (if no, print Enjoy your day). 
# if yes, print It is too windy for an umbrella. if no print Take an umbrella
question1 = input('Is it raining today? (Yes/No) ')

if (question1.lower() == "yes") :
    question2 = input('Is it windy too? (Yes/No) ')
    if (question2.lower() == "yes") :
        print("It is too windy for an umbrella")
    else :
        print("Take an umbrella")
else :
    print("Enjoy your day")