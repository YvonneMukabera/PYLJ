#lesson1
students=["Alice","Bob","Carol","David"]
print("Entire students",students)
print("First student is :", students[0]) 
print("Last student is :", students[-1])
students[1]="Peter"
students.append("John")
students.insert(1,"Mary")
students.remove("Carol")
print("updated list",students)
print("Total number of students:",len(students))
#lesson 2
marks = [45, 70, 32, 85, 60, 28, 90, 50]
passed_std=[]
failed_std=[]
for m in marks:
     if m>=50:
         passed_std.append(m)
     else:
         failed_std.append(m)
         
print("passed students are:",passed_std,"and there ", len(passed_std))       
print("failed students are:",failed_std,"and there ", len(failed_std))

sum=0
for mark in marks:
    sum+=mark
average=sum/len(marks)
print("Average marks of students is:",average)