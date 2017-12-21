# Day 20st: Fractal Art

Part 1 (copied from [AoC page](http://adventofcode.com/2017/day/21))
------
You find a program trying to generate some art. It uses a strange process that involves repeatedly enhancing the detail of an image through a set of rules.

The image consists of a two-dimensional square grid of pixels that are either on (#) or off (.). The program always begins with this pattern:

    .#.
    ..#
    ###

Because the pattern is both 3 pixels wide and 3 pixels tall, it is said to have a size of 3.

Then, the program repeats the following process:

- If the size is evenly divisible by 2, break the pixels up into 2x2 squares, and convert each 2x2 square into a 3x3 square by following the corresponding enhancement rule.
- Otherwise, the size is evenly divisible by 3; break the pixels up into 3x3 squares, and convert each 3x3 square into a 4x4 square by following the corresponding enhancement rule.

Because each square of pixels is replaced by a larger one, the image gains pixels and so its size increases.

The artist's book of enhancement rules is nearby (your puzzle input); however, it seems to be missing rules. The artist explains that sometimes, one must rotate or flip the input pattern to find a match. (Never rotate or flip the output pattern, though.) Each pattern is written concisely: rows are listed as single units, ordered top-down, and separated by slashes. For example, the following rules correspond to the adjacent patterns:

    ../.#  =  ..
              .#

                    .#.
    .#./..#/###  =  ..#
                    ###

                            #..#
    #..#/..../#..#/.##.  =  ....
                            #..#
                            .##.

When searching for a rule to use, rotate and flip the pattern as necessary. For example, all of the following patterns match the same rule:

    .#.   .#.   #..   ###
    ..#   #..   #.#   ..#
    ###   ###   ##.   .#.

Suppose the book contained the following two rules:

    ../.# => ##./#../...
    .#./..#/### => #..#/..../..../#..#

As before, the program begins with this pattern:

    .#.
    ..#
    ###

The size of the grid (3) is not divisible by 2, but it is divisible by 3. It divides evenly into a single square; the square matches the second rule, which produces:

    #..#
    ....
    ....
    #..#

The size of this enhanced grid (4) is evenly divisible by 2, so that rule is used. It divides evenly into four squares:

    #.|.#
    ..|..
    --+--
    ..|..
    #.|.#

Each of these squares matches the same rule (../.# => ##./#../...), three of which require some flipping and rotation to line up with the rule. The output for the rule is the same in all four cases:

    ##.|##.
    #..|#..
    ...|...
    ---+---
    ##.|##.
    #..|#..
    ...|...

Finally, the squares are joined into a new grid:

    ##.##.
    #..#..
    ......
    ##.##.
    #..#..
    ......

Thus, after 2 iterations, the grid contains 12 pixels that are on.

How many pixels stay on after 5 iterations?

My code:

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
        for iteration in range(5):
            size = pattern.shape[0]
            if size % 2 == 0:
                pattern = iterateFractal(pattern, size, 2, rules)
            elif size % 3 == 0:
                pattern = iterateFractal(pattern, size, 3, rules)
        print(np.sum(pattern))

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

Part 2 (copied from [AoC page](http://adventofcode.com/2017/day/21))
------
How many pixels stay on after 18 iterations?

My code

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
 