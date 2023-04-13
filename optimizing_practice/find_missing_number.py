def find_missing_number(arr):
    """In an array of distinct integers from 0, 1, 2 ... up to N find the missing integer, O(N)"""

    found = {}
    max_num = 0
    for num in arr:
        found[num] = True
        if num > max_num:
            max_num = num
    
    for num in range(max_num + 1):
        if not found.get(num):
            return num
    return None


def alternative(arr):
    """alternative solution that checks the difference between the sums"""

    full_sum = 0
    for num in range(1, len(arr) + 1):
        full_sum += num

    current_sum = 0
    for num in arr:
        current_sum += num
    
    return full_sum - current_sum
    

def main():
    arr = [2, 3, 0, 6, 1, 5]
    print(find_missing_number(arr))
    arr2 = [8, 2, 3, 9, 4, 7, 5, 0, 6]
    print(alternative(arr2))

if __name__ == "__main__":
    main()