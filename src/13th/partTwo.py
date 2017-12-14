# -*- coding: utf-8 -*-
'''
Created on 14.12.2017

@author: RaczeQ
'''

INPUT = '''ljoxqyyw'''

def main():
    base_lengths = INPUT + '-'
    hash_square = ''
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
        hash_square += row
    actual_group = 0
    hash_groups = {}
    for y in range(128):
        for x in range(128):
            hash_groups, created = createGroup(hash_square, hash_groups, x, y, actual_group)
            if created:
                actual_group += 1
    print(actual_group) # OUTPUT: 1074

def createGroup(hash_square, hash_groups, x, y, group_nr):
    index = y*128 + x
    created_group = False
    if x > -1 and x < 128 and y > -1 and y < 128 and hash_square[index] == '1' and not index in hash_groups:
        created_group = True
        hash_groups[index] = group_nr
        for y_p in [-1, 1]:
            hash_groups, c = createGroup(hash_square, hash_groups, x, y + y_p, group_nr)
        for x_p in [-1, 1]:
            hash_groups, c = createGroup(hash_square, hash_groups, x + x_p, y, group_nr)
    return hash_groups, created_group


if __name__ == "__main__":
    main()