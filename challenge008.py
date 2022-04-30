#ask for total price, then ask how many diners there are. Divide it to show how much each diners should pay
total_price = int(input('How much is the total price? '))
diner_amount = int(input('How many diners? '))

print('Each of diners should pay ' + str(total_price/diner_amount))