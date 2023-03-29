# program to check whether two give string are anagram or not.

def check_anagram1(input_str1, input_str2):
    if len(input_str1) == len(input_str2):
        char_set = set(input_str1)  # creating set of characters to remove duplicate characters
        for char in char_set:
            if input_str1.count(char)!= input_str2.count(char):
                return False
        return True
    else:   #if length of both strings are not same return false
        return False

def check_anagram2(input_str1, input_str2):
    return sorted(input_str1) == sorted(input_str2)     #After sorting both strings should be same


if __name__ == "__main__":
    print(check_anagram1("mar","ram"))
    print(check_anagram2("mar","ram"))
    print(check_anagram2("mara","rama"))
    print(check_anagram1("mara","rama"))
    print(check_anagram2("zara","Raza"))
    print(check_anagram1("zara","Raza"))





