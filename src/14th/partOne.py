# -*- coding: utf-8 -*-
'''
Created on 15.12.2017

@author: RaczeQ
'''

INPUT = '''Generator A starts with 618
Generator B starts with 814'''

def main():
    rows = INPUT.split('\n')
    a_factor = 16807
    b_factor = 48271
    divider = 2147483647
    gen_a = int(rows[0].split(' ')[-1]) * a_factor
    gen_b = int(rows[1].split(' ')[-1]) * b_factor
    pairs = 0
    for i in range(40000000):
        pairs += (bin(gen_a)[-16:] == bin(gen_b)[-16:])
        gen_a = gen_a * a_factor % divider
        gen_b = gen_b * b_factor % divider
    print(pairs) # OUTPUT: 577

if __name__ == "__main__":
    main()