marks = [45, 70, 32, 85, 60, 28, 90, 50]
passed=[]
failed=[]
average=sum(marks)/len(marks)

for n in marks:
    if n>=50:
        passed.append(n)
    else:
        failed.append(n)
print(f"number ofstudents passed: {len(passed)} and failed: {len(failed)}")
print(f"total of all passing marks is:{sum(passed)}")
print(f"average marks of the class is:{average}")
    
 

 