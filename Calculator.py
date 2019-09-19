# Calculator version 2.0
import time
import math
print('Calculator version 2.0')
time.sleep(1)
while 1 > 0:
    def ceil(x):
        return math.ceil(x)


    def floor(x):
        return math.floor(x)


    def absolute_value(x):
        return math.fabs(x)


    def factorial(x):
        return math.factorial(x)


    def e_powerx(x):
        return math.exp(x)


    def nat_log(x):
        return math.log(x,2.71)


    def common_log(x):
        return math.log(x,10)


    def sqrt(x):
        return math.sqrt(x)


    def sin(x):
        return math.sin(x)


    def cos(x):
        return math.cos(x)


    def tan(x):
        return math.tan(x)


    def cosec(x):
        return cosec(x)


    def sec(x):
        return sec(x)


    def cot(x):
        return cot(x)


    def gcd(first_number,second_number):
        return math.gcd(first_number,second_number)


    def log(number,base):
        return math.log(number,base)


    def sum(first_number,second_number):
        return first_number+second_number


    def difference(first_number, second_number):
        if first_number > second_number:
            return first_number - second_number
        if first_number<second_number:
            return second_number - first_number


    def subtraction(first_number, second_number):
        return first_number - second_number


    def multiplication(first_number,second_number):
        return first_number*second_number


    def division(first_number,second_number):
        return first_number/second_number








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
        type = input('Do you want to solve for a function (involving a single variable) :').lower()
        if type == 'yes':
            time.sleep(1)
            print('''The functions available with us are:'
                  1. ceiling function
                  2. floor function
                  3. absolute value
                  4. factorial
                  5. e to the power x
                  6. natural logarithm
                  7. common logarithm
                  8. square root 
                  9. cosine 
                 10. sine
                 11. tangent
                 12. cotangent
                 13. secant
                 14. cosecant 
                  ''')
            function = eval(input(' Please enter the function you want to evaluate:')).lower()
            number = eval(input('Enter the number:'))
            if function == 'ceiling function' :
                print(ceil(number))
            elif function == 'floor function' :
                print(floor(number))
            elif function == 'absolute value':
                print(absolute_value(number))
            elif function == 'factorial' :
                print(factorial(number))
            elif function == 'e to the power x' :
                print(e_powerx(number))
            elif function == 'natural log':
                print(nat_log(number))
            elif function == 'common log ' :
                print(common_log(number))
            elif function == 'sqrt':
                print(sqrt(number))
            elif function == 'cos' :
                print(cos(number))
            elif function == 'sin' :
                print(sin(number))
            elif function == 'tan' :
                print(tan(number))
            elif function == 'cot' or 'cotangent':
                print(cot(number))
            elif function == 'sec' or 'secant':
                print(sec(number))
            elif function == 'cosec' or 'cosecant':
                print(cosec(number))
            else:
                print('Invalid function')






                                  
                                  

    time.sleep(1)
    rerun = input('''Do you want to get more solutions? 
    Please answer in a Yes or No : ''').lower()
    if rerun == 'no':
        break
    elif rerun == 'yes':
        time.sleep(1)
        print('Starting again....')
        time.sleep(2)



