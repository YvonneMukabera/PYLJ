#shopping cart program
"""foods=[]
prices=[]
total=0

while True:
    food=input("enter a food to buy {q to quit}:")
    if food.lower()=='q': #to make any choice lower case
        break
    else:
        price=float(input(f"enter the price of the {food}:$"))
        foods.append(food)
        prices.append(price)
        total+=price
        
print("your shopping cart:")
for i in range(len(foods)):
    print(f"{foods[i]}: ${prices[i]:.2f}")
print(f"your total is: ${total:.2f}")
"""
foods=[]
prices=[]
total=0

while True:
    food=input("enter the food you want to buy(or done to quit):")
    if food.lower()=='done':
        break
    else:
        price=float(input(f"enter the price of {food}:$"))
        foods.append(food)
        prices.append(price)
        total+=price
print("your shopping cart:")
for i in range(len(foods)):
    print(f'{foods[i]}: ${prices[i]:.2f}') 
print(f'amount to pay is: ${total:.2f}')  