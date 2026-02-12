#collection = single variable used to store multiple values
# list = [] ordered and changeable ,duplicate ok
# set = {} unordered and immutable, but add/remove ok, no duplicates
# tuple = () ordered and unchangeable, duplicates ok, faster

fruits = ['Apple','Orange', 'Banana']
#print(fruits)
print(f"the second fruit is {fruits[1]}")
print("All fruits we have are:",end=" ")
for x in fruits:
    if (x== "Orange"):
     print(x,end=' and ')
    else:
        print(x,end=",")


