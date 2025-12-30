#2 Write a Python program to print the entire text.txt file.

with open('test.txt', 'r') as f:
    content = f.read()
    print(content)



#3 Write a single function that will append prediction for the current football year and print the test.txt file.

def append_and_print(file_path, prediction):
    with open(file_path, 'a') as f:
        f.write(f"\n{prediction}")
    
    with open(file_path, 'r') as f:
        content = f.read()
        f.seek(0)
        print(content)
append_and_print('test.txt', '2025-26 Tikvesh')




#4 Write a python program to find the longest word in test2.txt.

with open('test2.txt', 'r') as f:
    words = f.read().split()
    longest_word = max(words, key=len)
print(f"The longest word in test2.txt is: {longest_word}")




#5 Write a python program to find the most common word(s) in test2.txt.

with open('test2.txt', 'r') as f:
    words = f.read().split()
    word_count = {}
    for word in words:
        word = word.lower().strip('.,!?;"\'()[]{}')
        word_count[word] = word_count.get(word, 0) + 1
    max_count = max(word_count.values())
    most_common_words = [word for word, count in word_count.items() if count == max_count]
    print(f"The most common word(s) in test2.txt: {most_common_words} (appeared {max_count} times)")




#############################################################################################################
####################################  Homework: File Management #############################################
#############################################################################################################


#1 Write a program that will replace word “Seavus” with “Avenga” in test2.txt.

def replace_word_in_file(file_path, old_word, new_word):
    with open(file_path, 'r') as f:
        content = f.read()
    
    content = content.replace(old_word, new_word)
    
    with open(file_path, 'w') as f:
        f.write(content)
replace_word_in_file('test2.txt', 'Seavus', 'Avenga')
print("Replaced 'Seavus' with 'Avenga' in test2.txt")



#2 Write a program that will find the tennis surface with most unique winners in file test.csv.

def find_surface_with_most_unique_winners(file_path):
    surface_winners = {}
    with open(file_path, 'r') as f:
        next(f)  # Skip header
        for line in f:
            parts = line.strip().split(',')
            Year = parts[0]
            Tournament = parts[1]
            Winner = parts[2]
            Surface = parts[3]
            if Surface not in surface_winners:
                surface_winners[Surface] = set()
            surface_winners[Surface].add(Winner)
    most_unique_surface = max(surface_winners, key=lambda s: len(surface_winners[s]))
    return most_unique_surface, len(surface_winners[most_unique_surface])
surface, unique_count = find_surface_with_most_unique_winners('test.csv')
print(f"The tennis surface with most unique winners is: {surface} with {unique_count} unique winners")
