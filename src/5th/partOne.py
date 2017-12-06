# -*- coding: utf-8 -*-
'''
Created on 06.12.2017

@author: RaczeQ
'''

INPUT = '''10	3	15	10	5	15	5	15	9	2	5	8	5	2	3	6'''

def main():
    banks = [int(x) for x in INPUT.split('\t')]
    size = len(banks)
    history = [str(banks)]
    looped = False
    cycles = 0
    while not looped:
        value = max(banks)
        highest_index = banks.index(value)
        banks[highest_index] = 0
        for i in range(value):
            banks[(i+highest_index+1) % size] += 1
        if str(banks) in history:
            looped = True
        history.append(str(banks))
        cycles += 1
    print(cycles) # OUTPUT: 14029

if __name__ == "__main__":
    main()