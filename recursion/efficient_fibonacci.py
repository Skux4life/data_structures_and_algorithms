#!/usr/bin/env python3

def fibonacci(n, memo):
    if n == 0 or n == 1:
        return n
    elif not memo.get(n):
        memo[n] = fibonacci(n - 2, memo) + fibonacci(n - 1, memo)
    return memo[n]

def main():
    print(fibonacci(6, {}))

if __name__ == '__main__':
    main()