import itertools
from collections import defaultdict
import random
import time

print("====================================")
print("Proccessing...")

#initializing vowels and consonants
vowel = list("aeiou")
consonant = list("bcdfghjklmnpqrstvwxyz")

start = time.time()

# method that generates vowels and consonants
def vowels_consonants(vow, cons):
    vowels = [letter for letter in vow if letter in vow]
    consonants = [c for c in cons if c in cons]
    randConsonant = random.sample(consonants, 4)
    randVowel = random.sample(vowels, 5)
	
    newstring = randConsonant + randVowel
    vowelsconsonantsword = "".join(newstring)
    return vowelsconsonantsword
    
# read from file and and populate the dictionary
words = defaultdict(list)
file = open('dictionary.txt','r')
f = file.readlines()
for word in f:
	word=word.strip()
	words[''.join(sorted(word))].append(word)

# searching for the longest anagram, get the vowels and consonants and check against the words in dictionary
def generate_longest_word():
    outputlist = []
    inputWord = "iseudospo"     #assign generated vowels and consonants to variable inputWord 
    print("Randomly Generated letters are: ", inputWord)
    length_of_word = len(inputWord)
    #sort the vowels and consonants
    inputWord = sorted(inputWord) 
    while length_of_word > 0:
        # generate possible combinations of anagrams based on the length_of_word
        #itertools combinations will maintain the sort order of the letters
        for wordcombination in itertools.combinations(inputWord, length_of_word):  
            result = ''.join(wordcombination)
            if result in words:
            #returns list that contains all possible generated anagrams that match any of the engilsh words in the dictionary 
                outputlist+=words[result]

        length_of_word = length_of_word - 1
    return list(set(outputlist))
        
found = False
#this function will sort the list of anagrams in ascending order and prints out the longest word from the sorted list
def print_longestWords():
    list = generate_longest_word()
    #check to see if the matched_word list is not empty
    if(list is not None):
        outputresult = sorted(list, key=len) #this builds a new sorted list of anagrams from an iterable.
        longest_word = outputresult[-1]
        longest_len = len(longest_word)
        outputresult.remove(longest_word)
        same_len_words = [item for item in outputresult if len(item) == longest_len]
        print("Total Number of Anagrams: ",len(list))
        print("Longest Word: ",longest_word)
        if same_len_words:
            print(f"Other {longest_len} letter words")
            print(*same_len_words,sep="\n")
        found = True
    else:
        print("No Longest Word Found...Please try again")
    
print_longestWords()

end = time.time()

print("Processing Finished...")
print("Time taken... %s seconds " % (end - start))     
