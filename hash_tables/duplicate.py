#!/usr/bin/env python3

# Write a function that accepts an array of strings and returns the first duplicate value it finds.
# O(N) complexity

def find_duplicate(arr):
    hashed_arr = {}
    for item in arr:
        if not hashed_arr.get(item, None):
            hashed_arr[item] = True
        else:
            return item
    return None

def main():
    arr = ['a', 'b', 'c', 'd', 'c', 'e', 'f']
    print(find_duplicate(arr))

# --------------------------------------------------
if __name__ == '__main__':
    main()