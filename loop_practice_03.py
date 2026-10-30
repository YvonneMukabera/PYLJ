marks = [45, 70, 32, 85, 60, 28, 90]

highest = marks[0]

for n in marks:
    if n > highest:
        highest = n

second_max = marks[0]

for m in marks:
    if m < highest and m > second_max:
        second_max = m

print("Second highest:", second_max)