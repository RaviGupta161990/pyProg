#program to get 1s and 2s complement of given whole number

def ones_complement(num):
    if num > 0 and num < 128:
        bin_val = str(bin(num)[2:].rjust(8,'0'))
        comp_val = ''
        print(f'Binary value of {num} is: {bin_val}')
        for ch in bin_val:
            if ch == '1':
                comp_val += '0'
            else:
                comp_val += '1'
        print(f'1 s complement for {num} is: {comp_val} and decimal value is {(int(comp_val,2))}')
        return comp_val

def two_comple(num):
    bin_val = str(bin(num)[2:].rjust(8, '0'))
    comp_val = ones_complement(num)
    two_comp_val = ''
    len_comp = len(comp_val)-1
    if bin_val[len_comp] == "1":
        two_comp_val = comp_val[:len_comp]+bin_val[len_comp]
    else:
        while bin_val[len_comp] != "1":
            len_comp -= 1
        two_comp_val = comp_val[:len_comp]+bin_val[len_comp:]

    print(f'1 s complement for {num} is: {two_comp_val} and decimal value is {(int(two_comp_val, 2))}')
    return comp_val







two_comple(5)
two_comple(2)
two_comple(32)
