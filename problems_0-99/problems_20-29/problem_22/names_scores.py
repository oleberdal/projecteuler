"""
Author: Berdal, Ole
Created: 07.02.2019
Edited: 03.10.2019
Version: Python 3.7.4

https://projecteuler.net/problem=22:
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938ᵗʰ name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""
import time
start_time = time.time()


def sum_of_name_scores(names):
    names.sort()

    return sum([((i + 1) * sum([ord(l) - 64 for l in name])) for i, name in enumerate(names)])


def main():
    with open('data/names', 'r') as file:
        line = file.readline()

    data = line.replace('"', '').split(',')

    solution = sum_of_name_scores(names=data)

    print('Solution: %s.\nExecution time: %s seconds.' % (solution, time.time() - start_time))


if __name__ == '__main__':
    main()
