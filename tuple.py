# tuple = () ordered and unchangeable, duplicates ok, faster
fruits = ('Apple','Orange', 'Banana')
print(f"we have {len(fruits)} fruits ",end=' ')
print("which are:",end=" ")
print(fruits)
#counting the number of times a specified value appears in the tuple
print(f"the number of times a specified value appears in the tuple is: {fruits.count('Apple')}")
#return the index of the first element with the specified value
print(f"the index of the first element with the specified value is: {fruits.index('Apple')}")
