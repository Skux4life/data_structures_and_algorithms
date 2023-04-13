def find_longest_consecutive_sequence(arr):
    """accepts an array and returns the length of the longest consecutive sequence O(N)"""

    hash_arr = {}
    for num in arr:
        hash_arr[num] = True

    longest_sequence = 1
    for num in arr:
        # Check that the number is the first in the sequence
        if not hash_arr.get(num - 1):
            sequence = 1
            i = 1
            while hash_arr.get(num + i):
                sequence += 1
                i += 1
            if sequence > longest_sequence:
                longest_sequence = sequence

    return longest_sequence



def main():
    arr = [10, 5, 12, 3, 55, 30, 4, 11, 2]
    arr2 = [19, 13, 15, 12, 18, 14, 17, 11]
    print(find_longest_consecutive_sequence(arr))
    print(find_longest_consecutive_sequence(arr2))

if __name__ == '__main__':
    main()