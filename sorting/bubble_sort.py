import time
import random


def bubble_sort(nums):
    n = len(nums)
    swapping = True
    while swapping:
        swapping = False
        for i in range(1, n):
            if nums[i - 1] > nums[i]:
                nums[i-1], nums[i] = nums[i], nums[i-1]
                swapping = True
    return nums

# -- TEST SUITE, DONT TOUCH BELOW THIS LINE --


def main():
    start = time.time()
    o1 = bubble_sort(get_nums(10))
    o2 = bubble_sort(get_nums(100))
    bubble_sort(get_nums(500))
    end = time.time()
    if (end - start) < 1:
        print("Fast :)")
    else:
        print("Slow :(")
    print(o1)
    print(o2)


def get_nums(num):
    nums = []
    random.seed(0)
    for i in range(num):
        nums.append(random.randint(0, len(nums)))
    return nums


main()
