# Calculator version 2.0
import time
import math
print('Calculator version 2.0')
time.sleep(1)
while 1 > 0:

    print('''
                    Press 1 for solving an equation
                        Press 0 for arithmetic calculation ''')
    category = eval(input('>>'))

    if category == 1:
        type = input('Is your equation linear or quadratic?:').lower()
        if type == 'quadratic' :
            time.sleep(1)
            print("Please enter values of a, b, and c for quadratic equation in form 'ax^2 + bx + c = 0' ")
            time.sleep(1)
            a = eval(input("ENTER the coefficient of x^2 (a) :"))
            b = eval(input("ENTER the coefficient of x (b) :"))
            c = eval(input("ENTER the value of constant (c) :"))
            eqn = f'{a}x^2 + {b}x + {c} = 0 '
            time.sleep(1)
            print(eqn)
            solution = (b ** 2) - (4 * a * c)
            x1 = (-b + (solution) ** (1 / 2)) / (2 * a)
            x2 = (-b - (solution) ** (1 / 2)) / (2 * a)
            print()
            print("THE ROOTS OF THE EQUATION ARE", x1, 'AND ', x2)
        elif type == 'linear':
            time.sleep(1)
            print("Please enter the value of a and b for equation in form 'ax + b = 0'  ")
            time.sleep(1)
            a = eval(input('Enter the coefficient of x (a) : '))
            b = eval(input('Enter the constant(b) :'))
            eqn = f'{a}x+{b} = 0 '
            time.sleep(1)
            print(eqn)
            solution = f'x = {(-1)*(b)/(a)}'
            time.sleep(1)
            print('The solution to your equation is:',solution)
        else:
            print('''
                    We can only solve quadratic and linear equations right now!
                    Please answer as quadratic or linear.....
                    ''')


    elif category == 0:
        pass
    time.sleep(1)
    rerun = input('''Do you want to get more solutions? 
    Please answer in a Yes or No : ''').lower()
    if rerun == 'no':
        break
    elif rerun == 'yes':
        time.sleep(1)
        print('Starting again....')
        time.sleep(2)



