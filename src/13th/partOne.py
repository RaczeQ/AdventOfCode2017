# -*- coding: utf-8 -*-
'''
Created on 14.12.2017

@author: RaczeQ
'''

INPUT = '''ljoxqyyw'''

def main():
    base_lengths = INPUT + '-'
    used_squares = 0
    for r in range(128):
        srt_lengths = base_lengths + str(r)
        lengths = [ord(x) for x in str(srt_lengths)] + [17, 31, 73, 47, 23]
        circular_list = range(256)
        actual_position = 0
        skip_size = 0
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
        row = ""
        for s in sparse_hashes:
            row += bin(int(s, 16))[2:].zfill(4)
        used_squares += sum([int(x) for x in row])
    print(used_squares) # OUTPUT: 8316

if __name__ == "__main__":
    main()