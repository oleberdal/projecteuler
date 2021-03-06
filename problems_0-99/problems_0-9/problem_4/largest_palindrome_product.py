"""
Author: Berdal, Ole
Created: 25.09.2018
Edited: 27.03.2019
Version: Python 3.6.7

https://projecteuler.net/problem=4:
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
import time
start_time = time.time()


def find_largest_palindrome(digits):
    palindromes = []
    for x in range(10**(digits - 1), 10**digits):
        for y in range(x, 10**digits):
            if is_palindrome(str(x * y)):
                palindromes.append(x * y)

    return max(palindromes)


def is_palindrome(n):
    return n == n[::-1]


def main():
    solution = find_largest_palindrome(digits=3)

    print('Solution: %s.\nExecution time: %s seconds.' % (solution, time.time() - start_time))


if __name__ == '__main__':
    main()
