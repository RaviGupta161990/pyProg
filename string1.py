
def donuts(count):
    if count >= 10:
        return 'Number of donuts: many'
    else:
        return f'Number of donuts: {count}'


def both_ends(s):
    if (len(s)<2):
        return ""
    else:
        return s[:2]+s[-2:]


def fix_start(s):
    ns = s[0]

    ns1 = s[0]+(s[1:].replace(s[0], '*'))
    for ch in s[1:]:
        if ch == s[0]:
            ns += '*'
        else:
            ns += ch
    return ns, ns1


def mix_up(a,b):
    lst = list()
    lst.append(b[:2]+a[2:])
    lst.append(a[:2]+b[2:])
    return ' '.join(lst)

print(mix_up('dog', 'dinner'))



