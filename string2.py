def verbing(s):
    if len(s) < 3:
        return s
    else:
        if s[-3:] == 'ing':
            return s+'ly'
        else:
            return s+'ing'


def not_bad(s):
    noti = s.find('not')
    badi = s.find('bad')
    if(noti < badi):
        return s[:noti]+'good'+s[badi+3:]
    else:
        return s

def front_back(a,b)

    return a[:len(a)//2]+ b[:len(b)//2]
print(not_bad('The movie is not so bad'))
print(not_bad ('The dinner is not that bad!'))
print(not_bad('The tea is not hot'))
print(not_bad('it\'s bad yet not'))
