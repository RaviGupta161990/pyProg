# program to understand Break


input1 = "Today is Monday, first day of week"


def break_for():

    for letter in input1:
        if letter == ' ':
            continue

        print(letter,end=', ')
        if letter == 'y' or letter == 'k':
            print()
            print( 'coming out of for loop')
            break


    print('Out of for loop')

def break_while():
    leninput = len(input1)-1

    while leninput:
        if input1[leninput] == ' ':
            leninput -= 1
            continue
        print(input1[leninput], end= ', ')
        if input1[leninput] == 'd' or input1[leninput] == 'O':
            print()
            print('coming out of while loop')
            break
        elif input1[leninput] == ' ':
            pass
        leninput -= 1
    print('Out of while loop')


if __name__ == '__main__':
    break_while()

    print()
    break_for()