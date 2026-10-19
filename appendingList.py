numbers=[3,7,2,9,4,8]
result=[]
for n in numbers:
    if n%2==0:
        result.append(n**2)
print(result)