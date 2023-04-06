

def calc(operator,num1,num2):
    dict_operator = {
        'add' : '+',
        'substract': '-',
        'multiply': '*',
        'divide': '/',
        'modulo': '%',
        'power': '**'
    }

    return eval(str(num1)+dict_operator[operator.lower()] +str(num2))

print(calc('add',5,6)
      )
print(calc('substract',5,6))
print(calc('multiply',5,6))
print(calc('divide',5,6))
print(calc('modulo',5,6))
print(calc('power',5,6))
