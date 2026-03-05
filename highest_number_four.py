# Program to find the highest number among four numbers
num1,num2=int(input('Enter a Number: ')),int(input('Enter a Number: '))
num3,num4=int(input('Enter a Number: ')),int(input('Enter a Number: '))
if num1>num2:
    if num1>num3:
        if num1>num4:
            print(f'{num1} is highest number')
        else:
            print(f'{num4} is highest number')
    else:
        if num3>num4:
            print(f'{num3} is highest number')
        else:
            print(f'{num4} is highest number')
else:
    if num2>num3:
        if num2>num4:
            print(f'{num2} is highest number')
        else:
            print(f'{num4} is highest number')
    else:
        if num3>num4:
            print(f'{num3} is highest number')
        else:
            print(f'{num4} is highest number')
            
    
        
