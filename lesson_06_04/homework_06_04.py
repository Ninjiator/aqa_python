
print('Input some list of numbers:')
list_of_numbers = [2,5,5,9,13,4,8,6,0]
print(list_of_numbers)

sum = 0
for number in list_of_numbers:
    if number % 2 == 0:
       sum += number
print('Sum of all even numbers is ', sum)