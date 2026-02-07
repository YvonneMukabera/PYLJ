principle=0
rate=0
time=0

while True:
    principle=float(input('Enter the principle amount:'))
    if principle<0:
        print('Principle can not be less than zero')
    else:
       break    
while True:
    rate=float(input('Enter the rate of interest:'))
    if rate<0:
        print('Rate can not be less than zero')
    else:
       break     
while True:
    time=float(input('Enter the time period:'))
    if time<0:
        print('Time can not be less than zero')
    else:
       break      
Amount=principle*(1+rate/100)**time #alternatively, Amount=principle*pow((1+rate/100),time)
print(f'The amount after {time} years is ${Amount:.2f}')