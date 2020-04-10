import math
from functools import reduce
from functools import partial

def squared(x):
    return x*x
def minus_one(x):
    return x-1

my_number = 3
my_number = minus_one(my_number)
my_number = squared(my_number)
print(my_number)

# functions as data
function_list = [
    minus_one,
    squared
]
my_number2 = 3
for func in function_list:
    my_number2 = func(my_number2)

print(my_number2)

# functions as argument
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def combine_2and3(func):
    return func(2,3)
print(combine_2and3(add)) # 5

def append_with_space(str1, str2):
    return f'{str1} {str2}'
def combine_name(func):
    return func('Tom','Liu')
print(combine_name(append_with_space))

# return functions
def create_printer():
    def printer():
        print('Hello function')
    return printer
my_printer = create_printer()
my_printer()

def create_multiplier(a):
    def multiplier(x):
        return a*x
    return multiplier

double = create_multiplier(2)
triple = create_multiplier(3)
print(double(5))
print(triple(5))

# Closure : the returning function still has access to my_number!
def create_printer2():
    my_number = 42
    def printer():
        print(f'My favouriate number is {my_number}')
    return printer

my_printer = create_printer2()
my_printer()

def create_counter():
    count = 0
    def get_count():
        return count
    def increment():
        nonlocal count
        count += 1

    return (get_count, increment)

get_count, increment = create_counter()
print(get_count()) ## 0
increment()
increment()
print(get_count()) ## 2

# Higer Order function
def divide(x,y):
    if 0 == y:
        print('Warning: someone is trying to divide by 0')
        return 
    return x / y

def second_argument_not_zero(func):
    def safe_version(*args):
        if args[1] == 0:
            print('Warning: someone is trying to divide by 0')
            return
        return func(*args)
    return safe_version

@second_argument_not_zero
def divide2(x,y):
    return x / y

divide_safe = second_argument_not_zero(divide2)
print(divide_safe(3,0)) #higer order
print(divide2(3,0)) #decorator

# Mapping
doubled_numbers = [1,2,3]
def double(x):
    return 2*x
print(list(map(double, doubled_numbers)))

# Filter
numbers = [1,2,3]
def even_number(x):
    return x % 2 == 0
print(list(filter(even_number, numbers)))

# Lambda : simple creating an inline function to replace a regular function

print(list(map(lambda x: x*2, doubled_numbers)))
print(list(filter(lambda x: x%2==0, numbers)))

def create_printer(): # make it easy for creating a function
    # def printer():
    #     print('Hello function')
    # return printer
    return lambda : 'Hello funciton'

# List comprehensions: do mapping and filtering at the same time
doubled = [x * 2 for x in numbers]
print(f'list comprehension {doubled}')

evens = [x for x in numbers if x%2==0]
print(f'list comprehension {evens}')

# Reducing 
def get_sum(acc, element):
    print(f'acc is {acc}, x is {element}')
    return acc+element
print(reduce(get_sum, numbers,0)) # return 1+2+3+0 = 6
print(reduce(get_sum, numbers,2)) # return 1+2+3+2= 8

# Partial
def add(x,y,z):
    return x+y+z
def add_one(x):
    return lambda y,z : x+y+z
def add_two(x,y):
    return lambda z : x+y+z
def add_partial(x):
    return lambda y : lambda z : x + y + z

add_5 = add_one(5)
print(add_5(6,7))
print(add_one(5)(6,7)) #currying

add_56 = add_two(5,6)
print(add_56(7))
print(add_one(5)(6,7))
print('currying:', add_partial(5)(6)(7))

print(partial(add, 5, 6,7)())
print(partial(add, 5, 6)(7))

# Recursion
def count_down(x):
    if x < 0:
        print('done')
        return
    print(x)
    count_down(x-1)

print(count_down(10))

