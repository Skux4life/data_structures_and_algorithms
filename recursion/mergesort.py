#!/usr/bin/env python3

def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        sub_arr_1 = arr[:mid]
        sub_arr_2 = arr[mid:]

        mergesort(sub_arr_1)
        mergesort(sub_arr_2)

        # initial values for pointers to keep track of where we are in each array
        i = j = k = 0

        # Until we reach the end of either start or end, pick larger among elements start and end
        # place them in the correct position in the sorted array
        while i < len(sub_arr_1) and j < len(sub_arr_2):
            if sub_arr_1[i] < sub_arr_2[j]:
                arr[k] = sub_arr_1[i]
                i += 1
            else:
                arr[k] = sub_arr_2[j]
                j += 1
            k += 1
        
        # When all the elements are traversed in either array1 or array2,
        # pick up the remaining elements and put in a sorted array
        while i < len(sub_arr_1):
            arr[k] = sub_arr_1[i]
            i += 1
            k += 1
        
        while j < len(sub_arr_2):
            arr[k] = sub_arr_2[j]
            j += 1
            k += 1

def main():
    arr = [10, 9, 2, 4, 6, 13]
    mergesort(arr)
    print(arr)

if __name__ == '__main__':
    main()

