#!/usr/bin/env python3

def no_of_anagram(str):
    if len(str) == 1:
        return 1
    return no_of_anagram(str[1:]) * (len(str[1:]) + 1)

def anagrams(str):
    if len(str) == 1:
        return [str]
    collection = []

    # Find all anagrams of the substring from the second character until the end
    substring_anagrams = anagrams(str[1:])

    for anagram in substring_anagrams:
        for i in range(0, len(substring_anagrams) + 1):
            new_str = anagram[:i] + str[0] + anagram[i:]
            collection.append(new_str)
    
    return collection

def main():
    print(no_of_anagram('abcd'))
    print(anagrams('abcd'))


if __name__ == '__main__':
    main()