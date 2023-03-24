#Porgram to lear string in build functions

print(dir(''))

s = "Divine \n divinity"
print(s.lower()) # convert string to lower
print(s.upper()) # convert string to upper
print('_'.join(s))  # it will join all string with given seperater
print(s.title())  #  convert 1st character to upper case
print(s.islower())   # checks
print(s.isupper())
print('99999'.isalnum())
print(s.find('n'))
print(s.replace('n','ty'))

print(s.strip('e'))
print(s.lstrip('d'))
print(s.rstrip('en'))
#print(s.split('i'))
print(s.splitlines())
print('Hello'.rjust(20,'*')) # right justified
print('Hello'.ljust(20,'*'))    #left justified
print('hello and hi'.rfind('h'))    #returns index of last
print('hello and hi'.rindex(''))







