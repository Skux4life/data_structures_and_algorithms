#!/usr/bin/env python3

def charcount(arr):
    if len(arr) == 0:
        return 0
    return len(arr[0]) + charcount(arr[1:])

def main():
    arr = ['ab', 'c', 'def', 'ghij']
    print(charcount(arr))

if __name__ == '__main__':
    main()