#program to understand indexing in string with +ve and -ve indexing

input_string = 'HelloTodayIsWednesday'
def seperater():
    print(80 * '*')

def check_range(start, end, step):

    print(f'Start is :{start} , end is: {end} and step is: {step} ')
    print("using range:", end='')
    for i in range(start, end, step):
        print(input_string[i], end=', ')
    print()
    print("using Slicing:",input_string[start:end:step])
    seperater()

if __name__ =='__main__':
    input_string = 'HelloTodayIsWednesday'
    lenstring = len(input_string)
    seperater()

    # -ve to +ve stepup
    print('1:-ve to +ve stepup')
    check_range(start = -(lenstring), end = 5, step = 1)

    # +ve to +ve stepup
    print('2: +ve to +ve stepup')
    check_range(start=5, end=lenstring-1, step=2 )

    # +ve to -ve stepup
    print('3: +ve to -ve stepup')
    check_range(start=5, end=-6, step=1)

    # -ve to -ve stepup
    print('4: -ve to -ve stepup')
    check_range(start=-15, end=-6, step=1)

    # +ve to -ve stepdpown
    print('5: +ve to -ve step down')
    check_range(start=5, end=-6, step=-1)


    # +ve to +ve stepdown
    print('6:+ve to +ve stepdown')
    check_range(start=20, end = 5, step = -1)

    # -ve to +ve stepdown
    print('7:-ve to +ve stepdown')
    check_range(start=-1, end=5, step=-1)

    # -ve to -ve stepdown
    print('8:-ve to -ve stepdown')
    check_range(start=-1, end=-lenstring, step=-1)


#out of index range value




