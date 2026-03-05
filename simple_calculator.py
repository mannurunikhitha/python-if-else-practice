# Simple calculator program
num1,num2=int(input('Enter Number: ')),int(input('Enter Number: '))
operator=input("Enter operator (+, -, *, /): ")
if operator=='+':
    print(num1+num2)
elif operator=='-':
    print(num1-num2)
elif operator=='*':
    print(num1*num2)
elif operator=='/':
    print(num1/num2)
else:

    print('Invalid Operator')
