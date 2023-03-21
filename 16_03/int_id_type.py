# program to see the memory mapping and dtype of int type


def int_id(num):
    print(f'Memory address  of {num} is:{id(num)}')


def int_type(num):

    print(f'class type address  of {num} is:{type(num)}')


if __name__ =="__main__":

    # the addres of each integer is  fixed
    list1=[2,3,4,5,2,3]
    for int_item in list1:
        int_id(int_item)

    #lets try to change the value of list[4] = 2
    print("Before changing the list[4] memmory address are:")
    int_id(list1[0])
    int_id(list1[4])
    list1[4] = 6
    print("After chaning changing the memmory address are:")
    int_id(list1[0])
    int_id(list1[4])
    print("which is equal to memory address of 6")
    int_id(6)



    print(f'type of list1 is {type(list1)}')
    for int_item in list1:
        int_type(int_item)




