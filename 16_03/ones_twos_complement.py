#program to get 1s and 2s complement of given whole number

def ones_complement(num):
    '''
    Function to get 1's complement
    :param num: integer number
    :return: 1's complement of num
    '''
    if num > 0 and num < 128:
        bin_val = str(bin(num)[2:].rjust(8,'0'))
        comp_val = ''
        print(f'Binary value of {num} is: {bin_val}')
        for ch in bin_val:# for and in
            if ch == '1':
                comp_val += '0'
            else:
                comp_val += '1'
        print(f'1 s complement for {num} is: {comp_val} and decimal value is {(int(comp_val,2))}')
        return comp_val

def two_comple(num):
    '''
    Function to get 2's complement
    :param num:
    :return:
    '''
    bin_val = str(bin(num)[2:].rjust(8, '0')) # 8 bit representaion of binary number
    comp_val = ones_complement(num) # calling 1's complement
    two_comp_val = ''
    len_comp = len(comp_val)-1
    if bin_val[len_comp] == "1": # if last bit is one the except last bit all bits are reversed
        two_comp_val = comp_val[:len_comp]+bin_val[len_comp]
    else:
        while bin_val[len_comp] != "1": # if last bit is 0 then before last 1 all digits will be reversed
            len_comp -= 1
        two_comp_val = comp_val[:len_comp]+bin_val[len_comp:]

    print(f'1 s complement for {num} is: {two_comp_val} and decimal value is {(int(two_comp_val, 2))}')
    return comp_val







two_comple(5)
two_comple(2)
two_comple(32)
two_comple(35)
