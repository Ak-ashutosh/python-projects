# Calculator APP

num1, sign, num2 = input('Enter Calculations : ').split()

num1 = int(num1)
num2 = int(num2)

if sign == '+':
    print("Addittion is : ", num1+num2)
elif sign == '-':
    print('Subs is : ', num1-num2)
elif sign == '*':
    print('Multi is : ', num1*num2)
elif sign == '/':
    print('Division is : ', num1/num2)
else:
    print('Invalid Input')
