'''
Fives and three only
will retrun true if given number can be reached by using:
add 3
 multiply by 5
'''

def only_5_and_3(input_num):
    if input_num < 3:
        return False

    while input_num > 0:
        if (input_num % 3 ==0) or (input_num % 5 ==0 ):
            return True
        input_num -= 3
    return False

print(only_5_and_3(14))
print(only_5_and_3(8))
print(only_5_and_3(80))
print(only_5_and_3(00))
print(only_5_and_3(23))
