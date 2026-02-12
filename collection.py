#collection = single variable used to store multiple values
# list = [] ordered and changeable ,duplicate ok,not resizeable
# set = {} unordered and immutable, but add/remove ok, no duplicates
# tuple = () ordered and unchangeable, duplicates ok, faster

fruits = ['Apple','Orange', 'Banana']
#print(fruits)
print(f"we have {len(fruits)} fruits ",end=' ')
#print(f"the second fruit is {fruits[1]}")
print("which are:",end=" ")
#updating our fruit list
fruits[2]="Coconut"
for x in fruits:
    if (x== "Orange"):
     print(x,end=' and ')
    else:
        print(x,end=",")



