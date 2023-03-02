
def match_ends(words):
    wdcount = 0
    for word in words:
        if word[0] == word[-1]:
            wdcount += 1
    return wdcount


def sort_last(tup):
    tup.sort(key=lambda tp: tp[-1])
    return tup

print(sort_last([(3, 2), (5,1), (6,4), (9,3)]))
