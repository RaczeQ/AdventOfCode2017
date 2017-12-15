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
    a_list = []
    b_list = []
    index = 0
    while index < 5000000:
        if gen_a % 4 == 0:
            a_list.append(gen_a)
        if gen_b % 8 == 0:
            b_list.append(gen_b)
        if len(a_list) > index and len(b_list) > index:
            pairs += bin(a_list[index])[-16:] == bin(b_list[index])[-16:] 
            index += 1
        gen_a = gen_a * a_factor % divider
        gen_b = gen_b * b_factor % divider
    print(pairs) # OUTPUT: 316

if __name__ == "__main__":
    main()