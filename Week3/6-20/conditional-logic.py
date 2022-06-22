


from enum import Flag
from re import L


def main():

    animal = "zebra"
    my_animal  = "zebra"

    if my_animal == animal:
        print("My fav animal is  a zebra too.")

    number = 24
    
    # AND : In order for AND to evaluate to True, both clauses must be true
    if(number > 0 and number < 10):
        print("That is a positive number")
        print()
        print()
        print()
        print()
        print("wow")
    

    # OR : In order for OR to evaluate to True, atleast one of the clauses must be true.
    if(number == -2 or number > 20 and number != 24):
        print("Nice Number")

    #NOT: A unary operator that gives us the inverse of our value. Not True = False , Not False = True
    if(not True):
        print("True")


    # Conditional Logic to determine if a number is even. If a number is not even, then it must be false
    # Therefore, we can include an else statement that captures that logic.
    number = 21
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")


    # Given a grade, we can code a bunch of if-statements to let the user know what grade they received.
    # Order is very important here. If we reverse the order, of our if-statement such as putting the grades 
    # in descending order, then if we have a grade of 82, 82 > 0 so the user can recieve an "F".
    # That is why we use the AND keyword to make sure that our user doesn't input a incorrect grade and recieves
    # the correct grade
    grade = 72
    if grade < 100 and grade > 90:
        print("A")

    # Remember: Elif = else if. It is a handy way to include more if statements like so. If our grade does not
    # fall within any of our elif-statements, then it must be an improper grade and that logic is handled
    # with our else-statement code block
    elif grade < 90 and grade > 80:
        print("B")
    elif grade < 80 and grade > 70:
        print("C")
    elif grade < 70 and grade > 0:
        print("F")
    else:
        print("Invalid Grade")


    # range(0,10) = (0,1,2,3,4,5,67,8,9)
    for number in range(0,100):
        if number % 2 == 0:
            print(f"{number} is an even number")
        else:
            print(f"{number} is an odd number")



if __name__ == "__main__":
    main()