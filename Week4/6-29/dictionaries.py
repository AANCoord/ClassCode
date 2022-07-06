# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered, changeable and do not allow duplicates.
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "drivers": ["Me", "Myself", "I"]
}


print(car["brand"])             # Ford
print(car["model"])             # Mustang
print(car["year"])              # 1964
print(car["drivers"])           #["Me", "Myself", "I"]
print(car["drivers"][1])        # Me

# We can change values in a dictionary like so, furthermore, if a value doesn't exist it is created
car["year"] = 1990
print(car["year"])              # 1990
car["AWD"] = False
print(car)                      # {"brand": "Ford", "model": "Mustang", "year": 1964, "drivers": ["Me", "Myself", "I"], "AWD": False}



LETTERS = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
 "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
POINTS = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 
3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# The dict(zip()) function will create a dictionary from two lists.

scrabble_dictionary = dict(zip(LETTERS, POINTS))
print(scrabble_dictionary)

# scrabble_dictionary.update({"M":5})
scrabble_dictionary["M"] = 5


# Given a list of words, use the dictionary to calculate a score for a given word.
def score(words):

    points = 0

    for word in words:
        for letter in word:
            points += scrabble_dictionary[letter]

    return points


# Function to determine if a word such as "tacoocat" is a palindrome. I.e. written
# backwards the same way forward
def palindorme(word):
    
    length = len(word)
    for index in range(length // 2):
        if word[index] != word[length - index - 1]:
            return False
    
    return True

def main():
    
    # letter_position = LETTERS.find("A")
    # points = POINTS[letter_position]

    my_Words = ["MONEY", "HELLO", "SHRIMP", "TRIPLE", "GLASSDOOR"]
    # print(my_Words)

    my_Words[2] = "SHRIMPS"
    # print(my_Words)

    unique_letters = []

    for word in my_Words:
        unique_word = set(word)
        unique_letters.append(unique_word)

    # print(unique_letters)
    # print(f"Unique points for words: {my_Words} is {score(my_Words)}")



    scores = {"ABEM" : 52, "Zoila" : 58}
    # print(scores)s

    scores["ABEM"] +=  20
    # print(scores)
    # print(scrabble_dictionary)

    word = "hollywood"
    print(f"Is the word {word} a palindrome? {palindorme(word)}")



################# DO NOT EDIT BELOW THIS LINE #################
if __name__ == "__main__":
    main()
