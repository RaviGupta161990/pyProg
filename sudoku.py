'''
Mini sudoku
givne 3*3 metrice, have to return true if all 9 elements are b/w
0-9 and there should be no repetition
'''

def mini_sudoku(list):
    numlist = []

    for row in list:
        for num in row:
            if (num in numlist) or (num not in range(1,10)) :
                #print(num)
                return False
            else:
                numlist.append(num)
    return True


print(mini_sudoku([[3, 6, 4], [1,7,9], [2,8,5]]))
