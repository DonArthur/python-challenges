#ask the user to enter their favorite color. If they enter red, print I like red too, otherwise
# print I don't like [colour], I prefer red

colour = input('Tell me your favorite color:')

if (colour.lower() == "red") :
    print("I like red too")
else:
    print("I don't like " + colour + ", I prefer red.")