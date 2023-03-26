s1 = "a2b3c4"
num =''
str1 = ''
for ch in s1:

    if ch.isdigit():

        num = num+ch
        #print(num)
    else :

        str1 = str1+ch
        #print(num)
print(str1,num)
finalstr = ""
i= 0
while i < len(str1):
    finalstr = finalstr+(str1[i] * int(num[i]))
    i += 1
print(finalstr)

finalstr1 = ""
for i in range(1,len(s1),2):
    finalstr1 = finalstr1+(s1[i-1]*int(s1[i]))

print("second method is:",finalstr1)