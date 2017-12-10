# -*- coding: utf-8 -*-
'''
Created on 10.12.2017

@author: RaczeQ
'''

INPUT = '''230,1,2,221,97,252,168,169,57,99,0,254,181,255,235,167'''

def main():
    skip_size = 0
    lengths = [int(x) for x in INPUT.split(',')]
    circular_list = range(256)
    actual_position = 0
    for length in lengths:
        temp_list = list(circular_list)
        if length < 256:
            for i in range(length):
                circular_list[(actual_position + i)%256] = temp_list[(actual_position+length-1-i)%256]
            actual_position = (actual_position + length + skip_size) % 256
            skip_size += 1
    result = circular_list[0] * circular_list[1]
    print(result) # OUTPUT: 2928
if __name__ == "__main__":
    main()