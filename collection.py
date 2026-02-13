#collection = single variable used to store multiple values
# list = [] ordered and changeable ,duplicate ok,not resizeable
# set = {} unordered and immutable, but add/remove ok, no duplicates
# tuple = () ordered and unchangeable, duplicates ok, faster

fruits = ['Apple','Orange', 'Banana']
#print(fruits)
print(f"we have {len(fruits)} fruits ",end=' ')
#print(f"the second fruit is {fruits[1]}")
print("which are:",end=" ")
#changing our fruit indexed two our fruit list
fruits[2]="Coconut"
print(f"our last fruit was changed to:{fruits[2]}")
#adding new fruit
fruits.append('Banana')
print(f'the new fruit added is:{fruits[3]}')
for x in fruits:
    if (x== "Coconut"):
     print(x,end=' and ')
    else:
        print(x,end=",")
print('')
print(f'we removed this element from our list: {fruits[0]}')
fruits.remove(fruits[0])
print('updated list is:', end=' ')
for x in fruits:
    if (x== "Coconut"):
     print(x,end=' and ')
    else:
        print(x,end=",")
print('let us insert a new fruit at index 1')       
fruits.insert(1,"Grapes")
print('updated list is:', end=' ')
for x in fruits:
    if (x== "Coconut"):
     print(x,end=' and ')
    else:
        print(x,end=",")
print('sorting our list in alphabetical order')
fruits.sort()
print('our sorted list is:', end=' ')
for x in fruits:
    #if (x== "Coconut"):
     #print(x,end=' and ')
    #else:
        print(x,end=",")
        
print('let us reverse our list')
fruits.reverse()
print('our reversed list is:', end=' ')
for x in fruits:    
    #if (x== "Coconut"):
     #print(x,end=' and ')
    #else:
        print(x,end=",")
