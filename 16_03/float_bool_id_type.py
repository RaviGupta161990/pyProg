# program understand the memory mapping in float and bool

if __name__ == "__main__":
    numlist = (11.5,12.5,13.5,11.5,14.5)
    for num in numlist:
        print(f'id of {num} is {id(num)}')

    boollist = [True,False,False,True]
    for num in boollist:
        print(f'id of {num} is {id(num)}')

    print("type of numlist[0]:",type(numlist[0]))

    print("tupe of boolist[0]:", type(boollist[0]))

    bool1 = True
    bool2 = False
    print(f"memory address of bool1 is {id(bool1)}")
    print(f"memory address of bool2 is {id(bool2)}")