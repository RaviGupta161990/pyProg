#programs on opertor precedence

#Arithmetic opertors:
def seperat():
    print()
    print()
    print('*'*100)

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
    print(f'additon and substraction:')
    print(f'{a} + {b} - {c} = {result}')
    seperat()

    result = a + b - c * d
    print(f'additon, substraction, multiplication:')
    print(f'{a} + {b} - {c} * {d} = {result}')
    seperat()

    result = a + b - c * d / e
    print(f'additon, substraction, multiplication division: ')
    print(f'{a} + {b} - {c} * {d} / {e} = {result}')
    seperat()

    result = a + b - c * d / e % f
    print(f'additon, substraction, multiplication division modulo division:')
    print(f' {a} + {b} - {c} * {d} / {e} % {f} = {result}')
    seperat()

    result = a ** g + b - c * d / e % f
    print(
        f'exponent, additon, substraction, multiplication division modulo division:')
    print(f' {a} ** {g} + {b} - {c} * {d} / {e} % {f} = {result}')

    seperat()
    result = a ** g + (b - c) * d / e % f
    print(
        f'exponent, additon,brackets, substraction, multiplication, division, modulo division: ')
    print(f'{a} ** {g} + ({b} - {c}) * {d} / {e} % {f} = {result}')
    seperat()

    result = a ** g + (b - ~c) * d / e % f
    print(
        f'exponent, additon,brackets, bitwise not,  substraction, multiplication division modulo division: ')
    print(f'{a} ** {g} + ({b} - {~c}) * {d} / {e} % {f} = {result}')
    seperat()

    result = a ** (g>>1) + (b - ~c) * d / e % f
    print(
        f'exponent,left shit, additon,brackets, bitwise not,  substraction, multiplication division modulo division: ')
    print(f'{a} ** ({g}>>1) + ({b} - {~c}) * {d} / {e} % {f} = {result}')
    seperat()

if __name__ == '__main__':
    arith_precedence()



