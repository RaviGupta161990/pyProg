# program to seed the memory mapping procdure of string:

if __name__ == "__main__":
    str1, str2, str3 = "Hello", "world", "Hello"
    print(f"Str1 id is {id(str1)}")
    print(f"Str2 id is {id(str2)}")
    print(f"Str3 id is {id(str3)}")

    print("Memmory address for str1 and str3 is same because\
     address of same object 'Hello' is assigned to str1 and str3")
    print("if we try to change the value of any character\
     inside str1, str2 and str3 it will through an error as strings are immutable")

    print("But if we assign any new object to str1 it will not through any error")
    str1 = "Hi"
    print(f'str1 is  {id(str1)}')
