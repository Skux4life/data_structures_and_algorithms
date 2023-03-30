#!/usr/bin/env python3

def find_x(str):
    if str[-1] == 'x':
        return len(str) - 1
    else:
        return find_x(str[:-1])

def main():
    print(find_x('abcdefghijklmnopqrstuvwxyz'))

if __name__ == '__main__':
    main()