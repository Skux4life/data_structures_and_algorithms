#!/usr/bin/env python3

# For a staircase of n steps and with the ability to climb 1, 2 or 3 steps at a time
# Return how many possible paths there are

def staircase(n):
    if n < 0:
        return 0
    elif n == 1 or n == 0:
        return 1
    else:
        return staircase(n - 1) + staircase(n - 2) + staircase(n - 3)

def main():
    print(staircase(11))

if __name__ == '__main__':
    main()