numbers = [3, 8, 12, 5, 7, 10, 15, 20]
even_numbers=[]
even_counter=0
odd_numbers=[]
odd_counter=0
for n in numbers:
    if n%2==0:
        even_numbers.append(n)
        even_counter+=1
    else:
        odd_numbers.append(n)
        odd_counter+=1
print(f"Even numbers: {even_numbers}")
print(f"Count of even numbers: {even_counter}")
print(f"Odd numbers: {odd_numbers}")
print(f"Count of odd numbers: {odd_counter}")