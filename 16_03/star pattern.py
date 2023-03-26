# program to print below patter:
'''
*
12
***
1234
*****
'''
def star_num_patter(n):
    for i in range(1,n+1):
        if i % 2 != 0:
            print('*'*i)
        else:
            print(*range(1,i+1),sep='')


'''
star pyramid pattern
    *
   ***
  *****
 *******
*********

'''

def star_pyramid(n):
    for i in range(1,n+1):
        print(' '* (n-i),end='')    # to get space before that pettern
        print('*' * (2*i-1) , sep='')   # to get odd number of start


if __name__ == '__main__':
    star_num_patter(5)
    star_pyramid(5)