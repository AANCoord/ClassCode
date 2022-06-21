# NUMBER = 5

YEN = 1.604


from math import sqrt
from multiprocessing.dummy import freeze_support

def length(word):

    # len(): Returns the length of a string
    return len(word)

def cubeValue(number):

    return number ** 3
    # return number * number * number

def evenOrOdd(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

def pythagorenTheorem(a,b):

    return sqrt(a**2 + b**2)


def farenheit_celsius(temperature):
    tc = (temperature - 32) * 5 / 9
    return tc

# def celsius(f):

#     return (f - 32) * 5/9

def celsius_farenheit(temperature):
    tf = (temperature * 9/5) + 32
    return tf

def main():

    print("Hello World")


    # Functions: A chunk of resusable code that can be defined and given arguments.
    # Ex: print()    print(): prints a value to the console Arguements: Strings, Lists, integers, etc. etc.
    # print("Hello")
    # print(1,2,3,4,5)
    # print(True)
    # print([1,2,3,4])
    # print(5)

    # number = 6
    # evenOrOdd(number)

    # word = "mathematics"
    # length_of_word = length(word)
    # print(length_of_word)

    # number = 3
    # cubed_number = cube_value(number)
    # print(cubed_number)
    # a = 3
    # b = 4
    # c = pythagorenTheorem(a,b)
    # print(c)

    # temp = 98
    # temp_c = 36.6
    # # FZ = celsius(temp)
    # AGD = farenheit_celsius(temp)

    # print(f"{FZ} Celsius")
    # print(AGD)
    # print(celsius_farenheit(temp_c))
    # YEN = 3
    print(YEN)

if __name__ == "__main__":
    main()