
from math import sqrt

def main():
    
    length_one = int(input("What is the length of side A: "))
    length_two = int(input("What is the length of side B: "))

    length_three = length_one**2 + length_two**2

    hypotenuse = sqrt(length_three)

    print()
    print(f"The length of the hypotenuse is {hypotenuse:.2f}")


if __name__ == "__main__":
    main()