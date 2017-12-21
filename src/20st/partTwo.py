# -*- coding: utf-8 -*-
'''
Created on 21.12.2017

@author: RaczeQ
'''

INPUT = '''../.. => #../.../..#
#./.. => ###/##./.#.
##/.. => ..#/..#/##.
.#/#. => ###/.../#..
##/#. => #../#.#/.#.
##/## => ##./##./...
.../.../... => .##./.##./#.##/#.##
#../.../... => #.#./####/..#./#..#
.#./.../... => #.../#..#/##.#/#.##
##./.../... => .##./##../..##/....
#.#/.../... => #.../..##/#.##/#...
###/.../... => ##.#/.#../####/....
.#./#../... => .###/#..#/####/...#
##./#../... => ##.#/#.../..#./####
..#/#../... => ####/###./..../#.#.
#.#/#../... => ..##/.#../.#.#/...#
.##/#../... => #.##/###./####/####
###/#../... => #.#./##.#/..#./####
.../.#./... => .##./#.../..../#...
#../.#./... => ###./.##./...#/....
.#./.#./... => .#../..#./###./....
##./.#./... => .##./..../.###/...#
#.#/.#./... => ###./.##./##.#/#.##
###/.#./... => ##../..##/####/...#
.#./##./... => ..#./#..#/##../.#..
##./##./... => .#../...#/###./##..
..#/##./... => .###/.###/####/...#
#.#/##./... => ####/#.#./###./##..
.##/##./... => ##../..#./###./..#.
###/##./... => ##../..../.##./#.#.
.../#.#/... => ..#./.#.#/.##./#.##
#../#.#/... => ####/..##/#.../#.#.
.#./#.#/... => #.../#..#/#.../..##
##./#.#/... => .#.#/##.#/.###/#..#
#.#/#.#/... => ..#./##.#/##../#..#
###/#.#/... => ####/#..#/.##./###.
.../###/... => .##./..##/..#./#...
#../###/... => .##./###./##../.###
.#./###/... => ##../..../..##/##..
##./###/... => ##.#/#.#./#.#./##..
#.#/###/... => ..##/.#.#/..../.#.#
###/###/... => ####/.#../...#/.#..
..#/.../#.. => .#.#/#..#/##../##.#
#.#/.../#.. => ...#/.#.#/##.#/###.
.##/.../#.. => ..##/##../#.../#.##
###/.../#.. => ..##/##../#.#./##..
.##/#../#.. => #.##/####/##../####
###/#../#.. => ##../#..#/#.##/####
..#/.#./#.. => #.#./#.##/...#/..#.
#.#/.#./#.. => ..../...#/..../#.#.
.##/.#./#.. => ...#/#..#/.#../##.#
###/.#./#.. => .#../..#./.#../.#..
.##/##./#.. => #.##/..../#.##/.#..
###/##./#.. => #.../##../#.#./#.##
#../..#/#.. => #.../..##/#.#./.#..
.#./..#/#.. => ##../#.../#..#/##.#
##./..#/#.. => ###./#..#/..##/....
#.#/..#/#.. => ...#/##.#/#.../####
.##/..#/#.. => .##./###./#.../#..#
###/..#/#.. => #.#./.#.#/.#.#/...#
#../#.#/#.. => ##.#/####/#.##/##.#
.#./#.#/#.. => ...#/.#.#/.#../.##.
##./#.#/#.. => ##.#/.##./#.##/####
..#/#.#/#.. => ##../.#../##.#/#.#.
#.#/#.#/#.. => ..#./###./#..#/.#.#
.##/#.#/#.. => ..../.##./..#./##.#
###/#.#/#.. => #.#./.#../###./##..
#../.##/#.. => ##.#/##.#/.#.#/#.##
.#./.##/#.. => ###./.##./..../####
##./.##/#.. => ####/#..#/##../###.
#.#/.##/#.. => ####/..#./#..#/.#.#
.##/.##/#.. => ##../##.#/#.##/.##.
###/.##/#.. => ..../..#./####/##.#
#../###/#.. => ####/.#.#/#..#/#...
.#./###/#.. => #.#./#.#./.#../#...
##./###/#.. => ..../#.#./.##./##..
..#/###/#.. => ##.#/...#/.#../#.#.
#.#/###/#.. => ####/.##./..##/..#.
.##/###/#.. => .###/..#./..#./##.#
###/###/#.. => ##../..##/.###/.##.
.#./#.#/.#. => ...#/##../.#.#/##.#
##./#.#/.#. => ##../##../..##/##..
#.#/#.#/.#. => .##./###./#.##/.##.
###/#.#/.#. => .#.#/.#../.#.#/.##.
.#./###/.#. => #.##/####/#..#/....
##./###/.#. => #.../#.#./#.../#.##
#.#/###/.#. => ###./#.#./##../#...
###/###/.#. => ..##/.#.#/###./#..#
#.#/..#/##. => #.../#.#./..##/#...
###/..#/##. => #.../##.#/#.#./.###
.##/#.#/##. => ###./#.../..##/...#
###/#.#/##. => ...#/.###/#.##/.#..
#.#/.##/##. => .###/..#./#..#/....
###/.##/##. => ..../##.#/#..#/##.#
.##/###/##. => #.#./..##/.##./##.#
###/###/##. => ..../#..#/..../...#
#.#/.../#.# => .###/#.../.##./....
###/.../#.# => .#../.#../.#../#...
###/#../#.# => ..../##.#/##../##..
#.#/.#./#.# => ..##/#.#./##../#...
###/.#./#.# => ##../..../#.../#..#
###/##./#.# => #.../.##./.###/..##
#.#/#.#/#.# => #.../..##/#.#./##.#
###/#.#/#.# => ...#/#.##/#.##/#...
#.#/###/#.# => ##.#/###./#..#/..##
###/###/#.# => ..##/####/.##./..#.
###/#.#/### => #.##/..../..../#.#.
###/###/### => ###./..##/.#.#/....'''

import numpy as np

def main():
    rules = []
    pattern = np.matrix([[0, 1, 0],[0, 0, 1],[1, 1, 1]])
    for r in INPUT.split('\n'):
        io = r.replace(' ', '').replace('#', '1').replace('.', '0').split("=>")
        i_mat = np.matrix([[int(d) for d in x] for x in io[0].split('/')])
        o_mat = np.matrix([[int(d) for d in x] for x in io[1].split('/')])
        for i in range(4):
            rules.append((np.rot90(i_mat, i).tobytes(), o_mat))
            rules.append((np.rot90(np.flipud(i_mat), i).tobytes(), o_mat))
    for iteration in range(18):
        size = pattern.shape[0]
        if size % 2 == 0:
            pattern = iterateFractal(pattern, size, 2, rules)
        elif size % 3 == 0:
            pattern = iterateFractal(pattern, size, 3, rules)
    print(np.sum(pattern)) # OUTPUT: 2264586

def iterateFractal(pattern, size, step, rules):
    new_patterns = []
    for i in range(0, size, step):
        temp_patterns = []
        for j in range(0, size, step):
            sub_pattern = pattern[i:i+step, j:j+step].tobytes()
            found = False
            for r in rules:
                if r[0] == sub_pattern and not found:
                    found = True
                    temp_patterns.append(r[1])
        temp_pat = temp_patterns[0]
        for t in range(1, len(temp_patterns)):
            temp_pat = np.concatenate((temp_pat, temp_patterns[t]),1)
        new_patterns.append(temp_pat)
    new_pat = new_patterns[0]
    for n in range(1, len(new_patterns)):
        new_pat = np.concatenate((new_pat, new_patterns[n]), 0)
    return new_pat

if __name__ == "__main__":
    main()