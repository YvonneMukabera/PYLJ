p1=2.232344
p2=-6.7898454
p3=5.679893058
#rounding to 3,4,5 decimal places
print(f'price 1 is ${p1:.3f}')
print(f'price 2 is ${p2:.4f}')
print(f'price 3 is ${p3:.5f}') 
#padding with spaces to make total width 10
print(f'price 1 is ${p1:10}') 
print(f'price 2 is ${p2:10}') 
print(f'price 3 is ${p3:10}') 
#assigning signs   
print(f'price 1 is ${p1:+5}') 
print(f'price 2 is ${p2:+5}') 
print(f'price 3 is ${p3:+5}')   

print(f'price 1 is ${p1:010.3f}')#precede nbr with 0
print(f'price 2 is ${p2:<10.4f}') #left justified
print(f'price 3 is ${p3:>10.5f}')   #right justified
