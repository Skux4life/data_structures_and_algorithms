def greatest_product(arr):
    """Return the greatest product of any 2 numbers in the array. There can be negative numbers. O(N)"""

    greatest_positive_num = 0
    next_greatest_positive_num = 0
    greatest_negative_num = 0
    next_greatest_negative_num = 0
    for num in arr:
        if num >= 1:
            if num > greatest_positive_num:
                next_greatest_positive_num = greatest_positive_num
                greatest_positive_num = num
            elif num > next_greatest_positive_num:
                next_greatest_positive_num = num
        else:
            if num < greatest_negative_num:
                next_greatest_negative_num = greatest_negative_num
                greatest_negative_num = num
            elif num < next_greatest_negative_num:
                next_greatest_negative_num = num
    
    positive_product = greatest_positive_num * next_greatest_positive_num
    negative_product = greatest_negative_num * next_greatest_negative_num
    return positive_product if positive_product > negative_product else negative_product


def main():
    arr = [5, -10, -6, 9, 4]
    print(greatest_product(arr))

    arr2 = [-6, -4, 3, -2, 5, -1, 8]
    print(greatest_product(arr2))

if __name__ == '__main__':
    main()