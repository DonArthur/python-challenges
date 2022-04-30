#ask how many pizza slices the user started with and ask how many they have eaten
from ast import If


total_slices = int(input('How many pizza slices? '))
eaten_slices = int(input('How many have you eaten? '))
remaining_slices = total_slices - eaten_slices

if (remaining_slices < 0) : 
    print('You have eaten more than amount of the slices')
else :
    print('The remaining slices are ' + str(remaining_slices))