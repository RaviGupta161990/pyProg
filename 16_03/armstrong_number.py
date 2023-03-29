#program to check whether given number is armstrong number or not
'''
An Armstrong number is a number that is equal to the sum of its own digits raised to the power of the number of digits. Here is an example of an Armstrong number:

153 is an Armstrong number because it has three digits and is equal to the sum of the cubes of its digits:

1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
'''


def check_armstrong(num):
    str_num = str(num)
    len_num = len(str_num)
    sum = 0

    for char in str_num:
        sum += eval(char+'**'+str(len_num))
    #print(sum)
    return num==sum


if __name__ == "__main__":
    print(check_armstrong(121))
    print(check_armstrong(153))
