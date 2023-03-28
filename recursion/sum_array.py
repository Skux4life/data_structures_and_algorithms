#!/usr/bin/env python3

def sum(arr):
    if len(arr) == 1:
        return arr[0]
    return arr[0] + sum(arr[1:])

def main():
    arr = [1, 2, 3, 4, 5, 6]
    print(sum(arr))

if __name__ == '__main__':
    main()