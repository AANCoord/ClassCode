# This line of code imports a function randrange. Given two integers, like on line 7,
# we are given a number in that range
from random import randrange


# Lists
animals = ["dog", "cat", "giraffe"]
animal = "hippo"
letter_p = animal[2]
print(letter_p)

length_animals = len(animals)
print(length_animals)

print(len(animal))

# list.append(value) : Adds our argument "value" to the end of our list "list"
animals.append(animal)
print(animals)
# > ["dog", "cat", "giraffe", "hippo"]

# Similarily, list.pop() removes the very last thing in our list.
animals.pop()
print(animals)
# > ["dog", "cat", "giraffe"]

# Just like strings, we can use indexing to give us values in our list
words = ['h','a','p','p','y']
print(words[2])
# > p
print(words[:2])
# > ['h', 'a']
print(words[1:3])
# > ['a', 'p']


# Say we want to calculate our average grades. We can do it like so.
grades = [80, 60, 82, 91]

sum = 0
for grade in grades:
    sum += grade

average_grade = sum / len(grades)
print(average_grade)
# > 78.25


# This is an easy way to generate a list of numbers between 0 and 100.
list_100 = []
for num in range(0,100):
    list_100.append(num)

print(sum(list_100))
# >[0,1,2,3,4,5,6,7,8,10...95,96,97,98,99,]


# A factorial is represented as 5! = 5 * 4 * 3 * 2 * 1 = 120
# Let us create a loop that solves the factorial of a given number and creates a list of all the factors.
values = []
factorial_number = 6
summation = 1

# Keep in mind, we add +1 to include the number 6 in our range. Range is exclusive so range(0,3) = (0,1,2)
for i in range(1, factorial_number + 1):
    summation = summation * i
    values.append(i)

print(summation)
# > 120
print(values)
# > [1,2,3,4,5]



# Lists can contain multiple data types. They can include strings, integers, floats, or even booleans!
l = [1,2,3, "hi", "bye", False, 4.2]

# Say we want to generate a list of random numbers as input for a function. 
# We create an empty list called random_numbers and want to fill it with random values between 0 and 8
random_numbers = []
for _ in range(10):
    random_numbers.append(randrange(0,8))

print(random_numbers)
# > [0,5,1,7,7,3,2,1,5,4]
