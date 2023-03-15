# program to practice assighment operator and their precedence

def assign_precedence():
    x = 9
    print(f'x = 3 results in value of x: {x}')

    x += 9
    print(f'x += 9 results in value of x: {x}')

    x -= 9
    print(f'x -= 9 results in value of x: {x}')

    x *= 9
    print(f'x *= 9 results in value of x: {x}')
    x /= 9
    print(f'x /= 9 results in value of x: {x}')
    x //= 9
    print(f'x //= 9 results in value of x: {x}')
    x = int(x)
    x |= 9
    print(f'x |= 9 results in value of x: {x}')
    x &= 9
    print(f'x &= 9 results in value of x: {x}')

    x ^= 9
    print(f'x ^= 9 results in value of x: {x}')
    x = 9
    x <<= 3
    print(f'x <<= 9 results in value of x: {x}')
    x >>= 9
    print(f'x >>= 9 results in value of x: {x}')

assign_precedence()