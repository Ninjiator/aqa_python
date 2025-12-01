import logging

#task 1
def generator_1(number:int):
    i = 0
    while i <= number:
        if i % 2 == 0:
            yield i
        i += 1

def generator_fibo(number:int):
    a = 1
    b = 1
    while number > 0:
        yield a
        summ = a + b
        a = b
        b = summ
        number -= 1

#task 2
class ReverselistGenerator:
    def __init__(self, arr: list[int]):
        self.arr = arr
        self.current_index = len(arr)

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index == 0:
            raise StopIteration
        else:
            self.current_index -= 1
            return self.arr[self.current_index]

class EvenGenerator:
    def __init__(self, num):
        self.num = num
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.start + 2 <= self.num:
            self.start += 2
            return self.start
        else:
            raise StopIteration


#task 3
def decorator_for_func_logging(func):
    def wrapper(*args, **kwargs):
        print(f'LOGGING: args: {args}, kwargs: {kwargs}')
        result = func(*args, **kwargs)
        print("Func result is:", result)
        return result
    return wrapper

def try_except_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except Exception:
            print('Exception raised be aware')
        return None
    return wrapper


