#program to check if given string is rotation of another given string.

def check_rotation(main_string, rotated_string):
    return True if rotated_string in (main_string+main_string) else False


if __name__=="__main__":
    print(check_rotation('Rent', 'enRt'))