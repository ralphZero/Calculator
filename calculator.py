import os

clear = lambda: os.system('clear')
clear()

i = 0
while i == 0 :
    clear()
    x = float(input('Enter first number: \n'))
    y = float(input('Enter second number: \n'))
    res = 0

    choice = int(input('Choose operation..\n'
    '1 -- Addition\n'
    '2 -- Substraction\n'
    '3 -- Division\n'
    '4 -- Multiplication\n'
    '5 -- Quit\n'))

    if choice == 1:
        res = x + y
        print(f'The result is : {res}')
    elif choice == 2:
        res = x - y
        print(f'The result is : {res}')
    elif choice == 3:
        res = x / y
        print(f'The result is : {res}')
    elif choice == 4:
        res = x * y
        print(f'The result is : {res}')
    elif choice == 5:
        i = 1
    else:
        print('Wrong choice !')
        