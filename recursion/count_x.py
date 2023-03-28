#!/usr/bin/env python3

def count_x(str):
    # Base case: an empty string
    if len(str) == 0:
        return 0
    elif str[0] == 'x':
        return 1 + count_x(str[1:])
    else:
        return count_x(str[1:])

def main():
    test_string = 'axbxcxdxx'
    print(count_x(test_string))

if __name__ == '__main__':
    main()