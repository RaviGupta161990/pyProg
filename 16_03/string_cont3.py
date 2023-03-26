s1 = "abcdef"
output = "abCdeF"

finalstr = ""
for i in range(2,len(s1),3):
    finalstr = finalstr+s1[i-2:i]+s1[i].upper()

print(finalstr)
chr