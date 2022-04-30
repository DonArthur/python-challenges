#ask the user to enter a number over 100 and then a number under 10, show how many times the small number
# goes into the larger number

large_num = int(input('Insert a number larger than 100: '))
small_num = int(input('Insert a number smaller than 10: '))

# if (large_num <= 100) :
#     print('The large number must be larger than 100')
# elif (small_num >= 10) : 
#     print('The small number must be smaller than 10')
# else :
#     print(str(small_num) + ' in ' + str(large_num) + ' shows ' + str(str(large_num).count(str(small_num))) + ' time(s).')

answer = large_num//small_num
print(small_num,'goes into',large_num,answer,'times')