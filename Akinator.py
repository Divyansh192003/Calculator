# AKINATOR
import time

time.sleep(1)
print("                     HELLO , I AM  AKINATOR     ")
time.sleep(1)
print("                     I WILL READ YOUR MIND     ")
time.sleep(1)
print("                 TYPE \'1\' FOR \'YES\' AND \'0\' FOR \'NO\'  ")
time.sleep(1)
print()
print()

while 1 > 0:
    akinator = eval(input('IS YOUR CHARACTER A MALE??'))
    if (akinator == 1):
        time.sleep(1)
        a = eval(input("DOES YOUR CHARACTER HAVE A MOUSTACHE :"))
        b = eval(input("DOES YOUR CHARACTER WEAR SPECTACLES :"))
        c = eval(input("DOES YOUR CHARACTER TEACH IN CLASS :"))
        d = eval(input("IS YOUR CHARACTER MARRIED:"))
        e = eval(input("IS YOUR CHARACTER NEW TO THE SCHOOL :"))
        if [a, b, c, d] == [1, 1, 0, 0]:
            time.sleep(1)
            print("              THE CHARACTER IS AKSHAY SIR ")
        elif [a, b, c, d] == [0, 1, 1, 1]:
            time.sleep(1)
            print("              THE CHARACTER IS SANJAY SIR JR.")
        elif [a, b, c, d] == [1, 0, 1, 1]:
            time.sleep(1)
            print("              THE CHARACTER IS SANJAY JOSHI SIR ")
        elif [a, b, c, d] == [0, 0, 1, 1]:
            time.sleep(1)
            print("              THE CHARACTER IS SANJAY SIR ")
        elif [b, c, d, e] == [1, 0, 1, 0]:
            time.sleep(1)
            print("              THE CHARACTER IS MUKESH SIR")
        elif [a, b, c, d] == [1, 1, 1, 1]:
            time.sleep(1)
            print("              THE CHARACTER IS RAKESH SIR")
        elif [a, b, c, d] == [0, 0, 0, 0]:
            time.sleep(1)
            print("              THE CHARACTER IS JAIVEER  SIR")
        elif [a, b, c, e] == [0, 1, 0, 1]:
            time.sleep(1)
            print("              THE CHARACTER IS MANOJ SIR")
        elif [a, b, c, d] == [1, 1, 1, 0]:
            time.sleep(1)
            print("              THE CHARACTER IS PUNEET SIR")

        elif [a, b, c, d] == [0, 0, 0, 1]:
            time.sleep(1)
            print("              THE CHARACTER IS VIJAY SIR")

        else:
            print('I THINK YOU HAVE ENTERED SOMETHING WRONG!...PLEASE CHECK YOUR ANSWERS')

    if (akinator == 0):

        p = int(input("IS YOUR CHARACTER RELATED TO LANGUAGE: "))
        q = int(input("DOES YOUR CHARACTER USE SPECTACLES WHILE TEACHING: "))
        r = int(input("DOES YOUR CHARACTER TEACH IN CLASS: "))
        s = int(input("IS DISCIPLINE MAINTAINED WHEN YOUR CHARACTER TEACH IN CLASS: "))
        t = int(input("IS YOUR CHARACTER TEACHING FOR MORE THAN THREE YEARS: "))
        u = int(input("IS YOUR CHARACTER TALL: "))
        v = int(input("IS YOUR CHARACTER HAVE SMALL HAIR: "))
        w = int(input("DOES YOUR CHARACTER WALK SLOW: "))
        x = int(input("IS YOUR CHARACTER MARRIED: "))
        y = int(input("DOES YOUR CHARACTER HAS SOMEWHAT CURLY HAIR: "))
        z = int(input("DOES YOUR CHRACTER WEAR BLACK GOOGLES:"))
        n = int(input("IS YOUR CHARACTER PRESENT IN SCHOOL FOR VERY VERY LONG TIME: "))
        m = int(input("IS YOUR CHARACTER AMONG MAIN AUTHORITY OF THE SCHOOL: "))
        if p == 1:

            if q == 1:

                if [s, t, u] == [1, 1, 1]:
                    time.sleep(1)
                    print("              THE CHARACTER IS MEENAKSHI MAM")
                if [s, t] == [1, 0]:
                    time.sleep(1)
                    print("              THE CHARACTER IS KUSUM MAM")
                if [s, t, u] == [1, 1, 0]:
                    time.sleep(1)
                    print("              THE CHARACTER IS POONAM SHARMA MAM")
                if [s, t] == [0, 1]:
                    time.sleep(1)
                    print("              THE CHARACTER IS JAISHREE MAM")
                if [s, t] == [0, 0]:
                    time.sleep(1)
                    print("              THE CHARACTER IS NEW P.D MAM")
            if q == 0:
                if [v, u] == [1, 1]:
                    time.sleep(1)
                    print("              THE CHARACTER IS ANURADHA MAM")
                if [v, u, w] == [1, 0, 0]:
                    time.sleep(1)
                    print("              THE CHARACTER IS DEEPA MAM")
                if [v, u, w] == [1, 0, 1]:
                    time.sleep(1)
                    print("              THE CHARACTER IS MOHINI MAM")
                if [v, u] == [0, 1]:
                    time.sleep(1)
                    print("              THE CHARACTER IS POONAM MAKHIJA MAM")
        if p == 0:

            if r == 1:
                if [x, q, m] == [1, 1, 0]:
                    time.sleep(1)
                    print("              THE CHARACTER IS MEENA MAM")
                if [x, q, y] == [0, 0, 0]:
                    time.sleep(1)
                    print("              THE CHARACTER IS AMITA MAM")
                if [x, q, y] == [1, 0, 1]:
                    time.sleep(1)
                    print("              THE CHARACTER IS MANJU MAM")
                if [x, q, m] == [1, 1, 1]:
                    time.sleep(1)
                    print("              THE CHARACTER IS SONALI MAM")
                if [x, q, m, y] == [1, 0, 1, 0]:
                    time.sleep(1)
                    print("              THE CHARACTER IS YOGYATA MAM")
                if [x, q, m, y] == [1, 0, 0, 0]:
                    time.sleep(1)
                    print("              THE CHARACTER IS KOMAL MAM")

            if r == 0:
                if [x, z, u, n] == [1, 0, 0, 0]:
                    time.sleep(1)
                    print("              THE CHARACTER IS DEEPIKA MAM")
                if [x, z, u] == [0, 0, 0]:
                    time.sleep(1)
                    print("              THE CHARACTER IS MEENU MAM")
                if [x, z, u, n] == [1, 0, 1, 0]:
                    time.sleep(1)
                    print("              THE CHARACTER IS NEW P.EDU MAM")
                if [x, z, u] == [1, 1, 1]:
                    time.sleep(1)
                    print("              THE CHARACTER IS SILKY MAM")
                if [x, z, u] == [1, 1, 0]:
                    time.sleep(1)
                    print("              THE CHARACTER IS SUSHMA (SPORTS) MAM")
                if [x, z, u, n] == [1, 0, 0, 1]:
                    time.sleep(1)
                    print("              THE CHARACTER IS SUMAN MAM")
                if [x, z, u, n] == [1, 0, 1, 1]:
                    time.sleep(1)
                    print("              THE CHARACTER IS VIDHYADHARI MAM")

    print()
    time.sleep(2)
    print("           MADE BY AMAN , UDIT , ARYAN AND DIVYANSH  ")
    time.sleep(2)

