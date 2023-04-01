#!/usr/bin/env python3

# Given an array of positive numbers, write a function 
# that returns the greatest product of any 3 numbers
# Use sorting to implement the function O(NlogN)

def greatest_product(arr):
    arr.sort()
    return arr[-3] * arr[-2] * arr[-1]

# Finds the missing number from an array of integers
# Array is expected to have all integers from 0 up to the array length bar one
def missing_number(arr):
    arr.sort()
    for i in range(len(arr)):
        if i != arr[i]:
            return i
    return None

# Write 3 different implementations of a function that finds the greatest num in an array
# one O(N^2) one O(N logN) one O(N)

def max_1(arr):
    for num in arr:
        is_greatest_num = True
        for num2 in arr:
            if num2 > num:
                is_greatest_num = False
        if is_greatest_num:
            return num
    

def max_2(arr):
    arr.sort()
    return arr[-1]

def max_3(arr):
    max = arr[0]
    for num in arr:
        if num > max:
            max = num
    return max

def main():
    test_arr = [2, 8, 0, 3, 5, 1, 7, 6, 9]
    print(greatest_product(test_arr))

    print(missing_number(test_arr))

    print(max_1(test_arr))
    print(max_2(test_arr))
    print(max_3(test_arr))

if __name__ == '__main__':
    main()