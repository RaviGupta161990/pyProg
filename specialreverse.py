'''
Reverse the given set of string except special character
'''
def reverse_special(revstr):
    strlist = list()
    newlist= list()
    #sc_list = list()
    for char in revstr:
        if char.isalpha():
            strlist.append(char)
     #   else:
      #      sc_list.append()

    iter = 0
    while iter < len(revstr):
        if revstr[iter].isalpha():
            newlist.append(strlist.pop())
        else:
            newlist.append(revstr[iter])
        iter += 1

    return ''.join(newlist)

print(reverse_special('yunm$kl@#pot'))



