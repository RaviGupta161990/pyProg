s1 = "abcdef"
finalstr = ""
output = "aB12cD23"
k = 0
for i in range(1,len(s1),2):
    if (i % 2) != 0:
        k += 1
        finalstr = finalstr + s1[i-1] + s1[i].upper()+str(k)+str(k+1)
print (finalstr)