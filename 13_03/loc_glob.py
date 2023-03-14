#program to understand local and global variables

def loc_variable():

    var = "I am local variable"
    print(var)
var = "I am global Variable"


def glob_inside_loc():
    #global var
    #var += "I am local variable"
    print(var)

loc_variable()
glob_inside_loc()
print(var)


