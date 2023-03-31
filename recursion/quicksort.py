#!/usr/bin/env python3

class SortableArray:

    def __init__(self, arr) -> None:
            self.items = arr

    def quicksort(self, low, high):
        if low < high:
            
            # Find partition element such that elements smaller than the pivot are on the left
            # and elements greater than the pivot are on the right
            pivot_index = self.partition(low, high)

            # recursive call on the left of the pivot
            self.quicksort(low, pivot_index - 1)

            # recursive call on the right of the pivot
            self.quicksort(pivot_index + 1, high)

    def quickselect(self, kth_lowest_value, low, high):
        # Base case is subarray has one cell
        if high - low <= 0:
            return self.items[low]
        
        # Partition the array and grab the index of the pivot
        pivot_index = self.partition(low, high)

        if kth_lowest_value < pivot_index:
            # Recursively perform quickselect on the subarray to the left of the pivot
            return self.quickselect(kth_lowest_value, low, pivot_index - 1)
        elif kth_lowest_value > pivot_index:
            # Recursively perform quickselect on the subarray to the the right of the pivot
            return self.quickselect(kth_lowest_value, pivot_index + 1, high)
        else:
            return self.items[pivot_index]

    def partition(self, low, high):
        # Choose the right most element as the pivot
        pivot = self.items[high]

        # Pointer for greater element
        i = low - 1

        for j in range(low, high):
            if self.items[j] <= pivot:
                # if element smaller than pivot is found
                # swap it with the greater element pointed by i
                i += 1

                # swapping element at i with element at j
                (self.items[i], self.items[j]) = (self.items[j], self.items[i])
        
        # Swap the pivot element with the greater element specified by i
        (self.items[i + 1], self.items[high]) = (self.items[high], self.items[i + 1])

        # return the position from where partition is done
        return i + 1

def main():
    arr = [0, 50, 20, 10, 60, 30]
    sortable_arr = SortableArray(arr)
    print(sortable_arr.items)
    print(sortable_arr.quickselect(2, 0, len(arr) - 1))
    sortable_arr.quicksort(0, len(arr) - 1)
    print(sortable_arr.items)

if __name__ == '__main__':
    main()
