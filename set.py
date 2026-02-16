# set = {} unordered and immutable, but add/remove ok, no duplicates
fruits = {'Apple','Orange', 'Banana'}
print(f"we have {len(fruits)} fruits ",end=' ')
print("which are:",end=" ")
print(fruits)           
#adding new fruit
fruits.add('Grapes')    
print(f'after adding new fruit, our set is now: {fruits} ')
#removing a fruit   
fruits.remove('Apple')
print(f'we removed this element from our set: Apple')