#!/usr/bin/env python3

# Write a function that accepts a string that contains all the letters of the alphabet
# except one and returns the missing letter.
# complexity O(N)

def find_missing_letter(str):
    hashTable = {}
    for char in str:
        if char != ' ':
            hashTable[char] = True
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    for letter in alphabet:
        if not hashTable.get(letter, None):
            return letter
    return None

def main():
    test_string = 'the quick brown box jumped over the lazy dog'
    print(find_missing_letter(test_string))

# --------------------------------------------------
if __name__ == '__main__':
    main()