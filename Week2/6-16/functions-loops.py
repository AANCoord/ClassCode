

from configparser import LegacyInterpolation


def main():

    # Counts down from 100 to 0
    num = 100
    while num > 0:
        print(num)
        num = num - 1

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for letter in alphabet:
        print(letter)


    # Prints numbers between 0,9
    # range(0,10) == (0,1,2,3,4,5,6,7,8,9)
    for i in range(0,10):
        i = i + 1
        print(i)

    for j in range(0,10):
        print("Hello World")

    
    # Using while loop to calculate the amount we would owe after a loan that we take out
    loan_length = 5
    interest_rate = 12.57
    loan_amount = 25000
    current_year = 0

    while loan_length > current_year:
        interest_added = (interest_rate / 100) * loan_amount
        loan_amount += interest_added
        loan_length -=  1


    print(f"You owe ${loan_amount:,.2f} to the bank after a\n{loan_length} year term with a {interest_rate}% rate.")


if __name__ == "__main__":
    main()