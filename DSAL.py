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

#task3
marks = [45, 70, 32, 85, 60, 28, 90, 50]
max_marks=marks[0]
for m in marks:
    if m>max_marks:
        max_marks=m
print("Maximum marks is:",max_marks)
min_marks=marks[0]
for m in marks:
    if m<min_marks:
        min_marks=m
print("Minimum marks is:",min_marks)
number_of_best_performer=0
for m in marks:
    if m>60:
      number_of_best_performer+=1
    
print("Number of student above 60 is:",number_of_best_performer)
 
total = 0

for m in marks:
    total += m

average = total / len(marks)

new_list = []

for m in marks:
    if m >= average:
        new_list.append(m)

print("Average:", average)
print("Marks >= average:", new_list)
#lesson 4
list4=[12, 18, 25, 30, 15]
total=0
greater_than_15=[]
for n in list4:
    total+=n
    if n>15:
        greater_than_15.append(n)
print("Total is:",total)
print("Number of numbers greater than 15 are:",len(greater_than_15))
#lesson 5 function
def greet(name):
    print("Hi! am just functioning",name)
greet("Alice")
# a fununction that return something
def cal_total(numbers):
    total=0
    for n in numbers:
        total+=n
    return total
numbers=[45, 70, 32, 85, 60]
result=cal_total(numbers)
average= result/len(numbers)
print("Average is:",average)

print("Total is:", result)
#lesson 5 practice
marks = [45, 70, 32, 85, 60, 28, 90, 50]
def calculate_total(marks):
    total=0
    for m in marks:
        total+=m
    return total


def calculate_average(marks):
    total=calculate_total(marks)
    average=total/len(marks)
    return average


def count_passed(marks):
    passed_std=[]
    for m in marks:
        if m>=50:
            passed_std.append(m)
    return len(passed_std)

print("Total marks is:",calculate_total(marks))
print("Average marks is:",calculate_average(marks))
print("Number of students who passed is:",count_passed(marks))
