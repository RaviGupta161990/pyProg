"""
this file is to show different types of functions based on arguments
"""

# function which takes simple and single argument


def even_or_odd(x):
    '''
    This function will return "even" if given number is divisble 2 and "Odd" if its not
    :param x: any positve number greater than 1
    :return:even or odd
    '''
    return "Even" if x%2 == 0 else "Odd"


# function with default argument
def func_default_argument(name, year=1 ):
    '''
    this function will have default value of year as 1 if no value is given by user.
    :param name: Name of the user
    :param year:  Age of the user
    :return:  None
    '''
    print(f'My name is {name} and my age is {year}')


# functions with keyword arguments
def fun_keyword(name,age):
    '''
    while calling the function argument should be in key value or in same order as definition
    :param name:
    :param age:
    :return:
    '''
    print(f'My name is {name} and my age is {age}')


# function with variable non-keyword arguments

def fun_variable_nonkey(*args):
    '''

    :param args: variable length arguments
    :return: None
    '''
    for arg in args:
        print(arg, end=' ')


# function with variable keyword arguments

def fun_variable_key_value(**kwargs):
    '''

    :param args: variable length arguments
    :return: None
    '''
    for key,value in kwargs.items():
        print(f'keyword is: {key} and value: is {value}')


'''
print(even_or_odd(100))
print(even_or_odd(5))
func_default_argument("Raghav")
func_default_argument("Raghav",5)
func_default_argument(5)
func_default_argument("Raghave",year=5)


fun_keyword(age=5, name="Telangana",)
fun_keyword("Telangana",5)
'''
#fun_variable_nonkey("Ram", 1, 'Shyam', 5, 4.9, [34,34.7, 'Hello'])
fun_variable_key_value(name1='Ram', age1=1, name2='Shyam', age2=5)