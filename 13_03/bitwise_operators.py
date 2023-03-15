# program to learn bitwise operator
x = 128
y = 99
def print_x_y():
    print(f'  x = {bin(x)[2:].rjust(8, "0")}')
    print(f'  y = {bin(y)[2:].rjust(8, "0")}')

def print_seperater():
    print('------------------')
def print_new_opert():
    print("#######################################")
def bit_opertor():

    print_x_y()
    print_seperater()
    print(f'x|y = {bin(x|y)[2:].rjust(8,"0")}')
    print_new_opert()
    print_x_y()
    print_seperater()
    print(f'x&y = {bin(x&y)[2:].rjust(8,"0")}')
    print_new_opert()
    print_x_y()
    print_seperater()
    print(f'x^y = {bin(x^y)[2:].rjust(8,"0")}')
    print_new_opert()

    print_x_y()
    print_seperater()
    print(f' ~x = {bin(~x)[:].rjust(10, "0")}')
    print(f' ~y = {bin(~y)[:].rjust(10, "0")}')
    print_new_opert()

    print(f'  x = {bin(x)[2:].rjust(8, "0")}')
    print(f'x>>2= {bin(x>>2)[2:].rjust(8, "0")}')
    print_new_opert()
    print(f'  y = {bin(y)[2:].rjust(8, "0")}')
    print_seperater()
    print(f'y<<2 = {bin(y<<2)[2:].rjust(8, "0")}')
    print_new_opert()

    print(f'y<< 2 ^ 5 = {bin(y<<2^5)[2:].rjust(8, "0")} ')
    print(f'y<< 2 ^ 5 & 3 = {bin(y<<2^5&3)[2:].rjust(8, "0")} ')
    print(f'y<< 2 ^ 5 & 3 | 9= {bin(y<<2^5&3|9)[2:].rjust(8, "0")} ')

bit_opertor()