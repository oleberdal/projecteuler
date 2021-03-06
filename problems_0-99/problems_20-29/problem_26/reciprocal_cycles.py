"""
Author: Berdal, Ole
Created: 23.02.2019
Edited: 03.10.2019
Version: Python 3.7.4

https://projecteuler.net/problem=26:
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

¹/₂ = 	0.5
¹/₃	= 	0.(3)
¹/₄	= 	0.25
¹/₅	= 	0.2
¹/₆	= 	0.1(6)
¹/₇	= 	0.(142857)
¹/₈	= 	0.125
¹/₉	= 	0.(1)
¹/₁₀= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that ¹/₇ has a 6-digit recurring cycle.

Find the value of d < 1000 for which ¹/d contains the longest recurring cycle in its decimal fraction part.
"""
import time
start_time = time.time()


def unit_fraction_with_longest_recurring_cycle(below):
    for p in reversed(list_of_primes(below=below)):
        if is_full_reptend_prime(prime=p):
            return p


def list_of_primes(below):
    primes = [2]
    sieve = [True] * ((below - 2) // 2)

    for i in range(len(sieve)):
        if sieve[i]:
            prime = 2 * (i + 1) + 1
            primes.append(prime)
            for r in range((prime**2 - 3) // 2, len(sieve), prime):
                sieve[r] = False

    return primes


def is_full_reptend_prime(prime):
    return not any([10**e % prime == 1 for e in range(1, prime - 1)])


def main():
    solution = unit_fraction_with_longest_recurring_cycle(below=10**3)

    print('Solution: %s.\nExecution time: %s seconds.' % (solution, time.time() - start_time))


if __name__ == '__main__':
    main()
