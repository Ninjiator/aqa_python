# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    result = 0
    while result <= 25:
        result = number * multiplier
        if result > 25:
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_of_two_numbers(number1, number2):
    return number1 + number2

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def average_in_list(list_numbers):
    return sum(list_numbers) / len(list_numbers)
# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_the_string(string):
    return string[::-1]

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def get_the_longest_word(list_of_words):
     sorted_list = sorted(list_of_words, key=len, reverse=True)
     return sorted_list[0]

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка,
та -1, якщо другий рядок
не є підрядком першого рядка."""

def find_substring(str1, str2) -> int:
    return str1.find(str2)

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
# task 7 function from homework_6_01
def calculate_uniq_symbols_in_string(string:str) -> int:
    """Func is calculating the unique symbols in a string:str, and returning amount as int.
    string:str - str with any symbols inside
    return:int - amount of unique symbols in string
    """
    return len(set(string))

print('Task 7 : Input any amount of symbols: ')
user_input = input()
print(f"Unique symbols in string : {calculate_uniq_symbols_in_string(user_input)}")

# task 8 from homework_06_03
def copy_str_from_list(original_list:list, list_of_strings:list) -> list:
    """Function add all members with type str from original list to list_of_strings.

    original_list:list - param from which str members will be copied
    list_of_strings:list - param to which str members will be added
    """
    for k in original_list:
        if type(k) == str:
            list_of_strings.append(k)
    return list_of_strings

lst1 = ['1', '2', '3', True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
print(f"Task 8 : lst1 = {lst1} ")
lst2 = []

copy_str_from_list(lst1, lst2)
print(f"Result of func copy_str_from_list -> {lst2}")

# task 9 from homework_06_04
print('Task 9: here some list of numbers:')
list_of_numbers = [2,5,5,9,13,4,8,6,0]
print(list_of_numbers)

def sum_of_even_numbers(lst_num:list)-> int:
    """
    function calculate summ of even numbers and return the sum
    :param lst_num: list of int odd/even numbers
    :return: sum of even numbers
    """
    return sum([k for k in lst_num if k % 2 == 0])

print('Result of func sum_of_even_numbers is ', sum_of_even_numbers(list_of_numbers))

# task 10 from homework_05_01

def search_cars_by_criteria(cars_info:dict, searched_params:tuple, amount_of_results:int=5) -> list:
    """
    Functions searched for cars that meet specified criteria
    and displays the specified number of results sorted by price

    :param cars_info: dict of cars where value is a tuple of brand data
    :param searched_params: tuple(year_min, engine_min, price_max)
    :param amount_of_results: expected amount of results
    :return: list of tuples fall under required criteria
    """
    year_min, engine_min, price_max = searched_params

    filtered_cars = sorted([
        (brand, *data)
        for brand, data in cars_info.items()
        if data[1] >= year_min and data[2] >= engine_min and data[4] <= price_max
    ], key=lambda price: price[5])
    return filtered_cars[:amount_of_results]

def print_list(list_to_print:list)->None:
    for k in list_to_print:
        print(k)

def print_dict(dict_to_print:dict)->None:
    for key, value in dict_to_print.items():
        print(key, value)

car_data = {
  'Mercedes': ('silver', 2019, 1.8, 'sedan', 50000),
  'Audi': ('black', 2020, 2.0, 'sedan', 55000),
  'BMW': ('white', 2018, 3.0, 'suv', 70000),
  'Lexus': ('gray', 2016, 2.5, 'coupe', 45000),
  'Toyota': ('blue', 2021, 1.6, 'hatchback', 25000),
  'Honda': ('red', 2017, 1.5, 'sedan', 30000),
  'Ford': ('green', 2019, 2.3, 'suv', 40000),
  'Chevrolet': ('purple', 2020, 1.4, 'hatchback', 22000),
  'Nissan': ('pink', 2018, 1.8, 'sedan', 35000),
  'Volkswagen': ('brown', 2021, 1.4, 'hatchback', 28000),
  'Hyundai': ('gray', 2019, 1.6, 'suv', 32000),
  'Kia': ('white', 2020, 2.0, 'sedan', 28000),
  'Volvo': ('silver', 2017, 1.8, 'suv', 45000),
  'Subaru': ('blue', 2018, 2.5, 'wagon', 35000),
  'Mazda': ('red', 2019, 2.5, 'sedan', 32000),
  'Porsche': ('black', 2017, 3.0, 'coupe', 80000),
  'Jeep': ('green', 2021, 3.0, 'suv', 50000),
  'Chrysler': ('gray', 2016, 2.4, 'sedan', 22000),
  'Dodge': ('yellow', 2020, 3.6, 'suv', 40000),
  'Ferrari': ('red', 2019, 4.0, 'coupe', 500000),
  'Lamborghini': ('orange', 2021, 5.0, 'coupe', 800000),
  'Maserati': ('blue', 2018, 4.7, 'coupe', 100000),
  'Bugatti': ('black', 2020, 8.0, 'coupe', 2000000),
  'McLaren': ('yellow', 2017, 4.0, 'coupe', 700000),
  'Rolls-Royce': ('white', 2019, 6.8, 'sedan', 500000),
  'Bentley': ('gray', 2020, 4.0, 'coupe', 300000),
  'Jaguar': ('red', 2016, 2.0, 'suv', 40000),
  'Land Rover': ('green', 2018, 3.0, 'suv', 60000),
  'Tesla': ('silver', 2020, 0.0, 'sedan', 60000),
  'Acura': ('white', 2017, 2.4, 'suv', 40000),
  'Cadillac': ('black', 2019, 3.6, 'suv', 55000),
  'Infinity': ('gray', 2018, 2.0, 'sedan', 35000),
  'Lincoln': ('white', 2021, 2.0, 'suv', 50000),
  'GMC': ('blue', 2016, 1.5, 'pickup', 30000),
  'Ram': ('black', 2019, 5.7, 'pickup', 40000),
  'Chevy': ('red', 2017, 2.4, 'pickup', 35000),
  'Dodge Ram': ('white', 2020, 3.6, 'pickup', 45000),
  'Ford F-Series': ('gray', 2021, 3.5, 'pickup', 50000),
  'Nissan Titan': ('silver', 2018, 5.6, 'pickup', 35000)
}

searched_criteria = (2017, 1.6, 36000)
amount_of_results = 7

print("Task 10: Here we have some car data:")
print_dict(car_data)
print(f"Here is criteria for the car search: \n"
      f" year min ≥ ({searched_criteria[0]}),\n"
      f" engine min ≥ ({searched_criteria[1]}),\n"
      f" price max ≤ ({searched_criteria[2]})\n"
      f" amount of results: {amount_of_results}\n")
cars = search_cars_by_criteria(car_data, searched_criteria, amount_of_results)
print(f"Here is result of search ")
print_list(cars)

