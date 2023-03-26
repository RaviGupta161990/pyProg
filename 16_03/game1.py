import random
randnum = random.randint(1,20)
#print(randnum)

for i in range(5):
    userin = int(input("select a number between 1 and 20: "))
    if (userin - randnum) == 0:
        print(f"you have guessed it right with {i+1} attempts.")
        break
    elif(userin > randnum):
        print('your number is bigger than actual number.')
    else:
        print("you number is smaller than actual number.")

if i == 5:
    print(f"you used all your attempts, the actual number was:{randnum}")