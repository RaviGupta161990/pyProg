'''
program to decode message from space
input: AB[3CD]EF
output: ABCDCDCDEF
'''


import  re
def space_message(input):
    msglist = re.findall(r'\[(\w*)\]',input)
    for msg in msglist:
        # separating string literals
        str1 = re.search(r'[A-Z]+',msg).group()

        # separating the digits
        num = re.search(r'\d+',msg).group()
        msg = '['+msg+']'
        newmsg = int(num)*str1

        input = input.replace(msg,newmsg)
    return input

print(space_message('AB[33CD]EF'))

