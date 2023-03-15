# Progam to learn comparision operator and precedence
from arith_precedence import seperat

a = 5
b = 6
def print_a_b():
    print(f'a= {a} and b = {b} ')

seperat()
def arith_compare():

    result = a+b>=a-b
    print_a_b()
    print(f'a+b >= a-b:{result} ')
    seperat()

    result = a + b <= a - b
    print_a_b()
    print(f'a + b <= a - b:{result} ')
    seperat()



if __name__ == '__main__':
    arith_compare()
