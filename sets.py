#intersection and union
shoppingSet = {'Apple', 'toothpaste', 'Bread', 'eggs', 'milk'}
shoppingSet1 = {'Banana', 'toothbrush', 'Bread', 'eggs', 'milk'}
print("After intersection",shoppingSet.intersection(shoppingSet1))

print("after union with union function", shoppingSet.union(shoppingSet1))
print("after union with union symbol", shoppingSet|shoppingSet1)

str1 = "I am walking in the park with the pond in it"
set1= set(str1.split())

#discard() function return none if element is not found where as remove() will throw error
# both funtction are used to remove elements
shoppingSet.discard('toothpaste')
shoppingSet.discard('Breads')
shoppingSet1.remove('toothbrush')
#shoppingSet1.remove('egg') # it will throw error
print("after remove and discard operation", shoppingSet, shoppingSet1)

# add() is use add single element to set
#update() is used to add 1 or more than 1 element
shoppingSet.add('toothpaste')
shoppingSet.update(shoppingSet1,{'Vegetables'})
print ("After updation", shoppingSet)

#clear is used to remove all elements from set
print("after clearing the set", shoppingSet)

