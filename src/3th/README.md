# Day 3th: High-Entropy Passphrases

Part 1 (copied from [AoC page](http://adventofcode.com/2017/day/4))
------
A new system policy has been put in place that requires all accounts to use a passphrase instead of simply a password. A passphrase consists of a series of words (lowercase letters) separated by spaces.

To ensure security, a valid passphrase must contain no duplicate words.

For example:

- aa bb cc dd ee is valid.
- aa bb cc dd aa is not valid - the word aa appears more than once.
- aa bb cc dd aaa is valid - aa and aaa count as different words.

The system's full passphrase list is available as your puzzle input. How many passphrases are valid?

My code:

    def main():
        result_sum = sum([check_row(row) for row in INPUT.split('\n')])
        print(result_sum)

    def check_row(row):
        phrases = row.split(' ')
        for i in range(len(phrases)):
            for j in range(i, len(phrases)):
                if i != j and phrases[i] == phrases[j]:
                    return 0
        return 1

Part 2 (copied from [AoC page](http://adventofcode.com/2017/day/4))
------
For added security, yet another system policy has been put in place. Now, a valid passphrase must contain no two words that are anagrams of each other - that is, a passphrase is invalid if any word's letters can be rearranged to form any other word in the passphrase.

For example:

- abcde fghij is a valid passphrase.
- abcde xyz ecdab is not valid - the letters from the third word can be rearranged to form the first word.
- a ab abc abd abf abj is a valid passphrase, because all letters need to be used when forming another word.
- iiii oiii ooii oooi oooo is valid.
- oiii ioii iioi iiio is not valid - any of these words can be rearranged to form any other word.

Under this new system policy, how many passphrases are valid?

My code

    def main():
        result_sum = sum([check_row(row) for row in INPUT.split('\n')])
        print(result_sum) # OUTPUT: 119

    def check_row(row):
        phrases = row.split(' ')
        for i in range(len(phrases)):
            for j in range(i+1, len(phrases)):
                if sorted(list(phrases[i])) == sorted(list(phrases[j])):
                    return 0
        return 1
