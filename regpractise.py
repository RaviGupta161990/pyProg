import re


# Function to get all number from given string
# input: str1='hello 12 is my age 89789009 is my phone number'
# output: [12, 89789009]
def get_number(strseq):
    return re.findall(r'\d+', strseq)


# Function to check the given date is in format fo dd/sss/dddd
# input: 01/FEB/1990
# output: True
def check_date_format(date):
    valid = re.match(r'\d{2}/[A-Z]{3}/\d{4}', date)
    if valid:
        return 'Date is valid'
    else:
        return 'Date is not valid'


# function to get all occurrences of string before ':'
# input:Twelve:12 Eighty nine:89 thirty-two:32"
# output= ['Twelve', 'Eighty nine', 'two']
def get_string_pre_colon(userinput):
    return re.findall(r'\w+:', userinput)


#4.1 Function to remove all white spaces from given string
# string = 'abc 12\
# de 23 \n f45 6'
def rm_whitespace(userinput):
    #return ''.join(re.findall(r'\S+', userinput))
    return re.sub(r'\s','',userinput)

# 4.2Function to replace white space with '$'
def replace_whitespace(userinput):
    return re.sub(r'\s+', '$', userinput)


# 5.Function to check if python is present in string or not
def check_input_presence(userinput, str_to_check):

    valid = re.search(str_to_check, userinput, re.IGNORECASE)
    if valid:
        return f'{str_to_check } is present in "{userinput}"'
    else:
        return f'{str_to_check} is not present in "{userinput}"'


# Function to find pattern with 897 98
def find_patterns_string(userinput):

    return re.findall(r'\b\d{3} \d{2}\b', userinput)


#print(find_patterns_string('345 13 896 90 909 99765'))
#print(get_number('hello 12 is my age 89789009 is my phone number'))
#print(check_date_format('01/02/1990'))
#print(check_date_format('01/FEB/1990'))
#print(get_string_pre_colon('Twelve:12 Eighty nine:89 thirty-two:32'))
#print(get_string_pre_colon(':'))
print(rm_whitespace('hello 12 is my age 89789009 is my phone number'))
print(rm_whitespace('abc 12\
de 23 \n f45 '))
#print(replace_whitespace('abc 12\
#de 23 \n f45 '))
#print(replace_whitespace('hello 12 is my age 89789009 is my phone number'))
#print(check_input_presence("Python is easy to learn ..but only if you practice Python it can be easy", 'Python'))
#print(find_patterns_string('897 98 909O'))
#print(find_patterns_string('598I 89745678 98  987 87 909O'))
#print(find_patterns_string('098I 98'))