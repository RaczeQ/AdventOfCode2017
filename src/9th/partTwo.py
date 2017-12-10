# -*- coding: utf-8 -*-
'''
Created on 10.12.2017

@author: RaczeQ
'''

INPUT = '''230,1,2,221,97,252,168,169,57,99,0,254,181,255,235,167'''

def main():
    skip_size = 0
    lengths = [ord(x) for x in INPUT] + [17, 31, 73, 47, 23]
    circular_list = range(256)
    actual_position = 0
    for turn in range(64):
        for length in lengths:
            temp_list = list(circular_list)
            if length < 256:
                for i in range(length):
                    circular_list[(actual_position + i)%256] = temp_list[(actual_position+length-1-i)%256]
                actual_position = (actual_position + length + skip_size) % 256
                skip_size += 1
    sparse_hashes = ""
    for cycle in range(16):
        sparse_hash = circular_list[cycle*16]
        for i in range(1, 16):
            sparse_hash = sparse_hash ^ circular_list[cycle*16 + i]
        sparse_hashes += ('0'+hex(sparse_hash)[2:])[-2:]
    print(sparse_hashes) # OUTPUT: 0c2f794b2eb555f7830766bf8fb65a16
    
if __name__ == "__main__":
    main()