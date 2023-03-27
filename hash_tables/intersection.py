#!/usr/bin/env python3

# Write a function that returns the intersection of two arrays.
# Complexity should be O(N)

def find_intersection(arr1, arr2):
    intersection = []
    hashed_arr = {}
    for item in arr1:
        hashed_arr[item] = True
    
    for item in arr2:
        if hashed_arr.get(item, None):
            intersection.append(item)
    
    return intersection

def main():
    arr1 = [1,2,3,4,5]
    arr2 = [0,2,4,6,8]
    intersection = find_intersection(arr1, arr2)
    print(intersection)

# --------------------------------------------------
if __name__ == '__main__':
    main()