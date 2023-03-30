#!/usr/bin/env python3

def only_even(arr):
    if len(arr) == 0:
        return []
    elif arr[0] % 2:
        return only_even(arr[1:])
    else:
        return [arr[0]] + only_even(arr[1:])

def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(only_even(arr))

if __name__ == '__main__':
    main()