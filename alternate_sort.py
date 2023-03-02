'''
Program to sort the given sting in alternate order
input:['a', 'b', 'c',1 ,2, 3]
Output:[1, 'a', '2', 'b', 3, 'c']
'''


def alt_sort(inputlist):
    strlist = list()  # list to store str char from input list
    numlist = list()  # list to store digits from input list

    # seperating nums and string in respective lists using comprehension
    [strlist.append(item) if type(item) == str else numlist.append(item) for item in inputlist]

    # sorting num list and string list
    numlist.sort()
    strlist.sort()
    i = 0
    newlist = list() # final list to be returned
    while i < len(numlist):
        newlist.append(numlist[i])
        newlist.append(strlist[i])
        i += 1
    print(newlist)


alt_sort(['a', 1])
