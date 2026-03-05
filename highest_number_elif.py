# Program to find the highest number among four numbers
num1,num2,num3,num4=1000,400,28,49
if num1>num2 and num1>num3:
     if num1>num4:
         print(f' {num1} is highest number')
     else:
         print(f' {num4} is highest number')
elif num2>num3 and num2>num4:
    print(f' {num2} is highest number')
elif num3>num4:
    print(f' {num3} is highest number')
else:
    print(f' {num4} is highest number')

# Program to find the highest number among four numbers
num1,num2,num3,num4=1000,400,28,49
if num1>num2 and num1>num3 and num1>num4:
    print(f' {num1} is highest number')
elif num2>num3 and num2>num4:
    print(f' {num2} is highest number')
elif num3>num4:
    print(f'{num3} is highest number')
else:
    print(f' {num4} is highest number')
