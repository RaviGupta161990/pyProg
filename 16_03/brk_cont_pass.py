# this program is to learn how break, continue and pass key words work

def find_least_mulitple(num):
    '''
    Function to return least multiple of given number
    :param num:
    :return:
    '''
    result = 0
    for itr in range(2,num):

        if num % itr == 0:
            result = itr
            #continue # if we want to go for max mulitple
            break # breaking the loop once we found the least multiple of that number
        else:
            pass # pass

    return result

if __name__ == "__main__":
    user_input = int(input('Enter a number to get its least multiple :'))
    least_multiple = find_least_mulitple(user_input)
    if least_multiple:
        print(f'Least multiple of {user_input} is : {least_multiple}')
        continue
    else:
        print('There is no list multiple except the number itself')