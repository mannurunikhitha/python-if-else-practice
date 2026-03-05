# Program to find the highest number among three numbers
num1,num2,num3=int(input('Enter a Number: ')),int(input('Enter a Number: ')),int(input('Enter a Number: '))
if num1>num2:
    if num1>num3:
        print(f'{num1} is highest number')
    else:
        print(f'{num3} is highest number')
else:
    if num2>num3:
        print(f'{num2} is highest number')
    else:
        print(f'{num3} is highest number')