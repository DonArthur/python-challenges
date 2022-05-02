#ask the user to type in first nursery rhyme and diplay the length of the string.
#ask for a starting number and an ending number and display that section of the string

rhyme = input('Type a nursery rhyme: ')
print(len(rhyme))
start = int(input('Enter starting position: '))
end = int(input('Enter end position: '))
print(rhyme[start:end])