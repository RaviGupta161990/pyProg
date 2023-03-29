
def max_ch_repeatition(s1):
    return max(len(group) for group in s1.split("1"))

if __name__=='__main__':
    print(max_ch_repeatition('000000101'))