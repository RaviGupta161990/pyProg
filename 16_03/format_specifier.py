# program to chech %s %d %f

s = 'python'
snum = '555'
fl = 32.590876
i = 15
A = 67


if __name__ == "__main__":
    print(f'General format {s:>10}')
    print(f'octal representation of {i} is :{i:o}')     # octal representaion
    print(f'binary representation of {i} is :{i:b}')    # binary representaion
    print(f'hexadecimal representation of {i} is :{i:x}')   # hexadecimal with small case
    print(f'Hexadecimal representation of {i} is :{i:X}')   # hexadecimal with upper case
    print(f'float number round of to 3 decimal places of {fl} is {fl:0.3f}')      #rounding of to 3 decimal places

    print(f'unicode representation of {i} is :{i:c}')   # right justified
    print(f'unicode  {A} is :{A:c}')   # right justified
    print(f'percentage representation of {i} is :{i:%}')   # number format
