def process_numbers(numbers):
    result = []

    for n in numbers:
        if n % 2 != 0 and n > 5:
            result.append(n * 2)

    return result


values = [2, 5, 7, 8, 11, 13, 4]
print(process_numbers(values))

#adding 2 numbers

def add(a,b):
    return a + b

answer = add(5, 10)
print(f"The sum of 5 and 10 is: {answer}")


#updating the list with new values
def update_list(items):
    items.append(4)
    items = [10, 20]
    return items

numbers = [1, 2, 3]
result = update_list(numbers)

print(numbers)
print(result)

def modify(data):
    data[0] = 99
    data = [7, 8, 9]
    data.append(10)

numbers = [1, 2, 3]
modify(numbers)

print(numbers)

def modify(data):
    data.append(4)
    return data

numbers = [1, 2, 3]
result = modify(numbers)
result.append(5)

print(numbers)
print(result)