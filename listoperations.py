colors= ['red', 'green', 'yellow', 'white', 'purp']
list1 = ["apples", "bananas", "pineapples"]
shoppingList= ['apples', 'apples', 'bananas', 'apples', 'pear', 'pineapples', 'pear', 'apples','banana']
num = [1.0, 1.5,9.0, 10.7, 2]
bakeItems = ['bread', 'biscuit', 'cupcake', 'pastry', 'pancake']

#code for baked items list
bakeItems.sort(reverse=True)
print(bakeItems)

# code to sort mixed list
num.sort()
print('sorted numbers are', num)

#code for shoping list elemnts
for item in list1:
    print(f'{item}=> {shoppingList.count(item)}')

max = 0  # variable to stor max length
maxcolor = ''  # String to keep largest string
for color in colors:  # Iterating through each element to get length of each color
    if len(color) > max: # comparing the length of current color
        max = len(color)
        maxcolor = color

print(f'Largest string in color list is {maxcolor}')

print('colors with length greater then 5 are: ', end=' ')
print(' '.join([color for color in colors if len(color) > 5]))

print('colors with sane first and last character are : ', end=' ')
print(' '.join([color for color in colors if color[0] == color[-1]]))
colors.sort(key=lambda item: len(item))
print(colors)




