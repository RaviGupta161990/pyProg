'''
Program to sort all positive numbers in asending order keeping intact position of negative numbers

'''
def pos_neg_sort(numlist):
    poslist=[num for num in numlist if num > 0]
    #print('positive numbers are:',poslist)
    poslist.sort( reverse=True)
    #print('sorted positive numbers are:', poslist)
    i = 0
    while i < len (numlist):
        if numlist[i] > 0:
            numlist[i] = poslist.pop()
            #print('new number is:', numlist[i])
        i += 1
    return numlist

print(pos_neg_sort([24,4,78,6,-1,34,-9,2,-98]))
