
# Assume our name is: "Britney Spears"
name = input("What is your full name ")
age = int(input("what is your age "))
birth_location = input("Where you were born ")

# Each character in a string has a numbered position called an index. You can access the character at the Nth position by putting 
# the number N in between two square brackets ([ and ]) immediately after the string: 

flavor = "apple pie"
letter = flavor[1]              #Returns 'p'

# flavor[1] returns the character at position 1 in "apple pie", which is p. Wait, isn’t a the first character of "apple pie"?
# In Python—and most other programming languages—counting always starts at zero. To get the character at the beginning of a string, 
# you need to access the character at position 0:

first_letter = flavor[0]
# String:           a  p  p  l  e  p  i  e
# Index:            0  1  2  3  4  5  6  7
# Negative Index:  -8 -7 -6 -5 -4 -3 -2 -1          


# When we try and index a value outside of our string, we get an error
# For example: flavor[100] will gives us an index error

# What if we want to retrieve the world "apple" from our flavor? We can do this by indexing like so
apple = flavor[0:6]         #Returns 'apple'

# We can also rewrite this as
apple = flavor[:6]         #Returns 'apple'
pie = flavor[5:]           #Returns 'pie'
# When we do not have a number before or after the colon, we index from the begining or to the end. Note, that the value
# to the right of the colon  is excluded. We return everything up to that index but not that value. If the value is to 
# the left of the colon we include that value in our "slice" of the word.

# # A method that gives us the index of the character that we pass it.
space_index = name.find(" ")        #Returns index 7
letter_s = name.find("S")           #Returns index 8
empty = name.find("x")              #Returns -1 since the value is not in our string



# Returns the length of the string that we pass it.
length_name = len(name)

# Methods that convert our string to uppercase and lowercase
print(name.upper())
print(name.lower())


# Suppose you have a string name = "Zaphod" and two integers heads = 2 and arms = 3. You want to display them in 
# the following line: Zaphod has 2 heads and 3 arms. This is called string interpolation, which is just a fancy way 
# of saying that you want to insert some variables into specific locations in a string.
# >>> f"{name} has {heads} heads and {arms} arms"
# We usedd to write our print statements like so:    
# print("Your name is " + name + "Age: " .....)
print(f"Your name is {name} Age in Ten Years: {age + 10} You were born in {birth_location}")



# Operators
a = 1 + 2               #Addition  
b = 2 - 1               #Subtraction
c = 3 * 2               #Multiplication
d = 4 / 2               #Division
e = 2 == 2              #Equality

f = 5 // 2              #INteger Division
g = 7 % 2               #Modulus
h = 4 > 2               #Greater Than
i = 6 < 2               #Less Than
j = 4 >= 2              #Greater than or equal to
k = 6 <= 2              #Less than or equal to

print(a)                # 3
print(b)                # 1
print(c)                # 6
print(d)                # 2.0
print(e)                # True

print(f)                # 2
print(g)                # 1
print(h)                # True
print(i)                # False
print(j)                #True
print(k)                #False


print('a' > 'c')
print('z' > 'a')

age = "9"
age2 = "adam"

print(age2 > age)