# Program to check if a number is divisible by 2, 3, 5, or 7
num=int(input('Enter a Number:'))
if num%2==0:
    print(f'{num} is divisible by 2')
if num%3==0:
    print(f'{num} is divisible by 3')
if num%5==0:
    print(f'{num} is divisible by 5')
if num%7==0:
    print(f'{num} is divisible by 7')
else:
    print('no factor')
