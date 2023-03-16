# program to find the prime number


def check_prime(num):
    '''

    :param num: to check whether it's prime or not
    :return: True if num is prime and False if not
    '''
    if num > 0: # nested  if
        if num in [2,3]: # if elif else
            return True
        elif num % 2 == 0:
            return False
        else :
            for i in range(3, num, 2):# for loop with skip +2
                if num % i == 0: #if case
                    return False
        return True

def display_prime_num(prime_list):
    '''
    this function is to print all number in prime_list
    :param prime_list: list of prime numbers
    :return:
    '''
    itr = 0
    while itr<len(prime_list): # while loop
        if itr % 4 == 0: # if else
            print()
            print(prime_list[itr], end='||')
        else:
            print(prime_list[itr],end='||')
        itr += 1


if __name__ =="__main__":
    max_num = int(input("Please enter a number and you will get all prime numbers till that number"))
    prime_list = list()
    for num in range(2,max_num+1,1): # for loop and range
        if check_prime(num):
            prime_list.append(num)
    display_prime_num(prime_list)