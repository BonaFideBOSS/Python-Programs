import csv
import itertools
import time


def csv_to_dict(filename):
    result_dict = {}
    with open(filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            word, definition = row
            result_dict[word] = definition
    return result_dict


def txt_to_list(filename):
    with open(filename, "r") as f:
        words = [line.strip() for line in f]
        return set(words)


# Read Dictionary
print("Reading dictionary...")
filename = "dictionary.csv"
dictionary = None
dictionary_with_definition = False
if filename.split(".")[-1] == "csv":
    dictionary = csv_to_dict(filename)
    dictionary_with_definition = True
else:
    dictionary = txt_to_list(filename)
print("Reading dictionary completed!")


def possible_words(letters):
    possible_words = set()
    letter_count = len(letters)
    letters = sorted(letters)
    while letter_count > 0:
        for word_combination in itertools.permutations(letters, letter_count):
            word_combination = "".join(word_combination)
            if word_combination in dictionary:
                possible_words.add(word_combination)
        letter_count -= 1
    return possible_words


def longest_words(letters):
    print("Processing...")
    words = possible_words(letters.lower())
    word_count = len(words)

    if word_count > 0:
        words = sorted(words, key=len)
        longest_word = words[-1]
        longest_len = len(longest_word)
        words.remove(longest_word)

        same_len_words = [item for item in words if len(item) == longest_len]
        print("Total number of possible words: ", word_count)
        print("Longest word length: ", len(longest_word))
        print("Longest Word: ", longest_word)
        if dictionary_with_definition:
            print("Definition: ", dictionary[longest_word])
        if same_len_words:
            print(f"Other {longest_len} letter words")
            if dictionary_with_definition:
                for word in same_len_words:
                    print(f"{word}: {dictionary[word]}")
            else:
                print(*same_len_words, sep="\n")
    else:
        print("No possible word found in dictionary.")


def program():
    letters = input("\nEnter letters: ")
    start = time.time()
    longest_words(letters)
    end = time.time()
    print("Processing completed!")
    print(f"Time taken: {end-start} seconds ")
    again()


def again():
    check_again = input("\nDo you want to run again? [Y/N]")

    if check_again.upper() == "Y":
        program()
    elif check_again.upper() == "N":
        print("See you later.")
    else:
        again()


program()
