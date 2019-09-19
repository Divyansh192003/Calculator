# Calculator version 2.0
import time
import math
print('Calculator version 2.0')
time.sleep(1)
while 1 > 0:
    def ceil(x1):
        return math.ceil(x1)


    def floor(x2):
        return math.floor(x2)


    def absolute_value(x3):
        return math.fabs(x3)


    def factorial(x4):
        return math.factorial(x4)


    def e_powerx(x5):
        return math.exp(x5)


    def nat_log(x6):
        return math.log(x6,2.71)


    def common_log(x7):
        return math.log(x7,10)


    def sqrt(x8):
        return math.sqrt(x8)


    def sin(x9):
        return math.sin(x9)


    def cos(x10):
        return math.cos(x10)


    def tan(x11):
        return math.tan(x11)


    def cosec(x12):
        return cosec(x12)


    def sec(x13):
        return sec(x13)


    def cot(x14):
        return cot(x14)


    def gcd(first_number,second_number):
        return math.gcd(first_number,second_number)


    def log(number,base):
        return math.log(number,base)


    def sum(first_number2,second_number2):
        return first_number2+second_number2


    def difference(first_number3, second_number3):
        if first_number3 > second_number3:
            return first_number3 - second_number3
        if first_number3<second_number3:
            return second_number3 - first_number3


    def subtraction(first_number4, second_number4):
        return first_number4 - second_number4


    def multiplication(first_number5,second_number5):
        return first_number5*second_number5


    def division(first_number6,second_number6):
        return first_number6/second_number6








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
            function = eval(input(' Please enter the function you want to evaluate:'))
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
            elif function == 'cot' :
                print(cot(number))
            elif function == 'sec' :
                print(sec(number))
            elif function == 'cosec' :
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



