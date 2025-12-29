#2 Write a program that checks if following list ["abba","mama","mom","kayak","peeps", "bird rib"] contains words that are palindromes. Use function for palindrome check (don’t use the [::-1] trick)

def is_palindrome(word):
    cleaned = word.replace(" ", "")
    left, right = 0, len(cleaned) - 1
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    return True
words = ["abba", "mama", "mom", "kayak", "peeps", "bird rib"]
palindrome_words = [i for i in words if is_palindrome(i)]
print("Palindromic words in the list:", palindrome_words)

#3 Write a program that will check which numbers are prime from a given range of 1 till 1001. Use function for prime number check.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

for num in range(1, 1002):
    if is_prime(num):
        print(f"{num} is a prime number.")

#4 Write a Python function to find the Max of three numbers.

def max_of_three(a=0, b=0, c=0):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

print("The maximum of the three numbers is:", max_of_three(10435345, 25345345, 1545345))


#5 Write a Python function to remove the duplicates of a list (don’t use set function).

def remove_duplicates(input_list):
    unique_list = []
    for i in input_list:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list
sample_list = [1, 2, 2, 3, 4, 4, 5, 1, 6, 7, 8, 8, "test", "test", "bla bla", "bla bla", "hello", "world", "hello", "world", "hello", "world", "hello"]
print(sample_list)
print("List after removing duplicates:", remove_duplicates(sample_list))

#6 Write a function that will count the letters occurrences in given full name.

def count_letter_occurrences(full_name):
    letter_count = {}
    for char in full_name:
        if char.isalpha():
            char = char.lower()
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1
    return letter_count
name = input("Enter your full name: ")
occurrences = count_letter_occurrences(name)
print("Letter occurrences in your name:", occurrences)

################################################
############  Homework: Functions  #############
################################################

#1 Write a program that will return the playing card out of two with higher priority.
"""
Example: 10 hearts is bigger(higher priority) than 9 clubs

Ace spades is bigger(higher priority) than Ace diamonds
"""
def card_priority(card):
    rank_order = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    suit_order = {'clubs': 1, 'diamonds': 2, 'hearts': 3, 'spades': 4}
    
    rank, suit = card.split()
    return (rank_order[rank], suit_order[suit])
def compare_cards(card1, card2):
    if card_priority(card1) > card_priority(card2):
        return card1
    else:
        return card2
card1 = input("Enter the first card: ")
card2 = input("Enter the second card: ")
higher_card = compare_cards(card1, card2)
print(f"The card with higher priority is: {higher_card}")

#2 Write a function is_pangram(sentence) to check if a sentence uses every letter of the alphabet.

def is_pangram(sentence):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    sentence_set = set(sentence.lower())
    for i in alphabet:
        if i.lower() not in sentence_set:
            return False
    return True
test_sentence = input("Enter a sentence to check if it's a pangram: ")
if is_pangram(test_sentence) == True:
    print("The sentence is a pangram.")
else:
    print("The sentence is not a pangram.")

#3 For the following dictionaries:
"""
dic1 = {"apple":3,"banana":2,"kiwi":6}
dic2 = {"banana":7}
dic3 = {"mango":4}
create a function that will aggregate the values under each unique element in each of the dictionaries.
Result: {'apple': 3, 'banana': 9, 'kiwi': 6, 'mango': 4}
"""

def aggregate_dicts(*dicts):
    aggregated = {}
    for i in dicts:
        for key, value in i.items():
            if key in aggregated:
                aggregated[key] += value
            else:
                aggregated[key] = value
    return aggregated
dic1 = {"apple": 3, "banana": 2, "kiwi": 6}
dic2 = {"banana": 7, "apple": 2, "kiwi": 4, "orange": 9, "grape": 1}
dic3 = {"mango": 4, "grape": 2, "orange": 5}
result = aggregate_dicts(dic1, dic2, dic3)
print("Aggregated dictionary:", result)