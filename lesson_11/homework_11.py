from os.path import split

def sum_of_numbers(array):
    for element in array:
        try:
            sum_of_int = sum(list(map(int, element.split(","))))
            print(f"Sum of element's in list [{element}] is {sum_of_int}")
        except ValueError:
            print(f"Element - [{element}] contain's a string")



arr = ['1,2,3,4', '1,2,3,4,50', 'qwerty1,2,3']
sum_of_numbers(arr)

