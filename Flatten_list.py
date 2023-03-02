import re

'''
take input of m*n list of list and return a single list
'''

def flaten_list(inlist):
    finallist = re.sub('\[|\]| ','',str(inlist))
    finallist = finallist.split(',')
    
    return[int(str) for str in finallist]

    '''
    lenlist = len(inlist)
    newlist = list()

    if lenlist == 1 or lenlist == 0:
        return inlist
    iter = 0
    while iter < lenlist:
        if type(inlist[iter]) != int:
            for num in inlist[iter]:
                newlist.append(num)
        else:
            newlist.append(inlist[iter])
        iter +=1
    return newlist
    '''
print(flaten_list([1, 2, [4, 5, 6], 11, 12]))