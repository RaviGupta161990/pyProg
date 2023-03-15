#programs on opertor precedence
'''
print(bin(3)[2:])

print(bin(5)[2:].rjust(8,'0'))
print(bin(6)[2:].rjust(8,'0'))
print(bin(eval('5 and 6'))[2:].rjust(8,'0'))

print(5 and 6)
'''
#Arithmetic opertors:
def arith_precedence():
    a = 5
    b = -2
    c = 4
    d = 23
    e = 6
    f = 9
    g = 3
    h = 56
    result = a + b - c
    print(f'additon and substraction: {a} + {b} - {c} = {result}')
    result = a + b - c * d

    print(f'additon, substraction, multiplication: {a} + {b} - {c} * {d} = {result}')

    result = a + b - c * d / e

    print(f'additon, substraction, multiplication division: {a} + {b} - {c} * {d} / {e} = {result}')

    result = a + b - c * d / e % f

    print(f'additon, substraction, multiplication division modulo division: {a} + {b} - {c} * {d} / {e} % {f} = {result}')
    result = a ** g + b - c * d / e % f

    print(
        f'additon, substraction, multiplication division modulo division: {a} ** {g} + {b} - {c} * {d} / {e} % {f} = {result}')


arith_precedence()



