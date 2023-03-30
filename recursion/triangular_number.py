#!/usr/bin/env python3

def triangluar_number(n):
    if n == 0:
        return 0
    return n + triangluar_number(n - 1)

def main():
    print(triangluar_number(7))

if __name__ == '__main__':
    main()