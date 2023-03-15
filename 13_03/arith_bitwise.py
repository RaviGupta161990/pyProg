# program see the precedence in bitwise and arithmatic opertor

from arith_precedence import seperat

a=256
b=6
def arith_bitwise():
    result = a >> 1 + b
    print(f'{a} >> 1 + {b} = {result}')
    seperat()

    result = a-b >> 4
    print(f'{a} - {b} >> 4 = {result}')
    seperat()

    result = a - b >> 4 & 5
    print(f'{a} - {b} >> 4 & 5 = {result}')
    seperat()


arith_bitwise()


