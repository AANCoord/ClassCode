# Author: Adam Valencia
# Sample Print Statements to the console
print("adam")
print()
print(5)

print(type(5))
print(type('a'))
print(type('adam'))


print(5 + 6)
print( " Adam" + "Valencia")


# Variable Assignment. Save the  value of four different tests and calculate the average of the 4 tests
test1 = 60
test2 = 70
test3 = 80
final = 70

total = test1 + test2 + test3 + final

avg = total / 4


name = "Adam"
hot_pockets = "yummy"

print(name , final, test1, test2)

print(type(print))


# \n = insert a newline into a print statement
# \t = insert a tab into the print statement
print("Adam \n" + 'a\n' + "student\n")
print("Adam \t" + 'a\t' + "student\t")

# Each print statement ends with a newline
print("Adam")
print('a')
print("Student")



# Sample Input from User. Asking a user for their name and then 
# printing it out into the console
name = input("What is your name: ")
print(f"Your name is: {name}")



# Function that asks three people for their name and age and prints them
# to the console 
def ask_peoples_name():
    name1 = input("What is your name person1: ")
    name2 = input("what is your name person2: ")
    name3 = input("what is your name person3: ")
    
    age1 = int(input("What is your age person1: "))
    age2 = int(input("what is your age person2: "))
    age3 = int(input("what is your age person3: "))

    print(type(age1))
    print(f"Name: {name1} Age: {age1}")
    print(f"Name: {name2} Age: {age2}")
    print(f"Name: {name3} Age: {age3}")

    
    print((age1 + age2 + age3) / 3)

# Function call to run the above function or method
ask_peoples_name()


# Boolean Data Type and Truthy or Falsy Values
print(type(True))
print(type(False))

if int("0"):
    print("Booo")

if "":
    print("Booo") 

var1 = ""
var2 = str(var1)
print(var1)
print(var2)


int()
str()
bool()
float()

print(1 + 2.0)
print(type(1 + 2.0))
print()