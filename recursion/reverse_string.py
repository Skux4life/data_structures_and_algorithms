#!/usr/bin/env python3

def reverse(str):
    if len(str) == 1:
        return str[0]
    return reverse(str[1:]) + str[0]

def main():
    test_str = 'abcde'
    print(reverse(test_str))

if __name__ == '__main__':
    main()