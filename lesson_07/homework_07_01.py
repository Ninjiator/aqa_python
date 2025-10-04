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

def find_substring(str1, str2):

    return -1

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
    """Func is calculating the unique symbols in a string, and returning amount as int."""
    return len(set(string))

print('Input any amount of symbols: ')
user_input = input()
print(f"Unique symbols in string : {calculate_uniq_symbols_in_string(user_input)}")

# task 8 from homework_06_03
def copy_str_from_list(original_list:list, list_of_strings:list) -> list:
    """Function copy all members with type str from original list to list_of_strings."""
    for k in original_list:
        if type(k) == str:
            list_of_strings.append(k)
    return list_of_strings

lst1 = ['1', '2', '3', True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = []

copy_str_from_list(lst1, lst2)
print(f"Result of func copy_str_from_list -> {lst2}")

# task 9
# task 10