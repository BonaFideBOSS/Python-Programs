def palindrome():
    word = input("Please provide a word: ")

    palindrome = word[::-1]

    if word == palindrome:
        print("Hooray! Your word is a Palindrome!")
    else:
        print("Sorry, the given word is not a Palindrome.")

    again()

def again():
    check_again = input('''
Do you want to check again?
Please type Y for YES or N for NO.
''')

    if check_again.upper() == 'Y':
        palindrome()
    elif check_again.upper() == 'N':
        print('See you later.')
    else:
        again()

palindrome()
