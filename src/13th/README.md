# Day 13th: Disk Defragmentation

Part 1 (copied from [AoC page](http://adventofcode.com/2017/day/14))
------
Suddenly, a scheduled job activates the system's disk defragmenter. Were the situation different, you might sit and watch it for a while, but today, you just don't have that kind of time. It's soaking up valuable system resources that are needed elsewhere, and so the only option is to help it finish its task as soon as possible.

The disk in question consists of a 128x128 grid; each square of the grid is either free or used. On this disk, the state of the grid is tracked by the bits in a sequence of knot hashes.

A total of 128 knot hashes are calculated, each corresponding to a single row in the grid; each hash contains 128 bits which correspond to individual grid squares. Each bit of a hash indicates whether that square is free (0) or used (1).

The hash inputs are a key string (your puzzle input), a dash, and a number from 0 to 127 corresponding to the row. For example, if your key string were flqrgnkx, then the first row would be given by the bits of the knot hash of flqrgnkx-0, the second row from the bits of the knot hash of flqrgnkx-1, and so on until the last row, flqrgnkx-127.

The output of a knot hash is traditionally represented by 32 hexadecimal digits; each of these digits correspond to 4 bits, for a total of 4 * 32 = 128 bits. To convert to bits, turn each hexadecimal digit to its equivalent binary value, high-bit first: 0 becomes 0000, 1 becomes 0001, e becomes 1110, f becomes 1111, and so on; a hash that begins with a0c2017... in hexadecimal would begin with 10100000110000100000000101110000... in binary.

Continuing this process, the first 8 rows and columns for key flqrgnkx appear as follows, using # to denote used squares, and . to denote free ones:

    ##.#.#..-->
    .#.#.#.#   
    ....#.#.   
    #.#.##.#   
    .##.#...   
    ##..#..#   
    .#...#..   
    ##.#.##.-->
    |      |   
    V      V   

In this example, 8108 squares are used across the entire 128x128 grid.

Given your actual key string, how many squares are used?

My code:

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
    print(used_squares)

Part 2 (copied from [AoC page](http://adventofcode.com/2017/day/14))
------
Now, all the defragmenter needs to know is the number of regions. A region is a group of used squares that are all adjacent, not including diagonals. Every used square is in exactly one region: lone used squares form their own isolated regions, while several adjacent squares all count as a single region.

In the example above, the following nine regions are visible, each marked with a distinct digit:

    11.2.3..-->
    .1.2.3.4   
    ....5.6.   
    7.8.55.9   
    .88.5...   
    88..5..8   
    .8...8..   
    88.8.88.-->
    |      |   
    V      V   

Of particular interest is the region marked 8; while it does not appear contiguous in this small view, all of the squares marked 8 are connected when considering the whole 128x128 grid. In total, in this example, 1242 regions are present.

How many regions are present given your key string?

My code

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
        print(actual_group)

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
 