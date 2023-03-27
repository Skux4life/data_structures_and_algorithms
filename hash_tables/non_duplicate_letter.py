#!/usr/bin/env python3

# Write a function that returns the first non-duplicate character in a string.
# Complexity O(N)

def first_non_duplicate_letter(str):
    str_map = {}
    for char in str:
        if str_map.get(char, None):
            str_map[char] += 1
        else:
            str_map[char] = 1
    
    for char in str:
        if str_map.get(char, 0) == 1:
            return char
    return None

def main():
    test_string = 'minimum'
    print(first_non_duplicate_letter(test_string))

# --------------------------------------------------
if __name__ == '__main__':
    main()