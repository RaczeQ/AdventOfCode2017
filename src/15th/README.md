# Day 15th: Permutation Promenade

Part 1 (copied from [AoC page](http://adventofcode.com/2017/day/16))
------
You come upon a very unusual sight; a group of programs here appear to be dancing.

There are sixteen programs in total, named a through p. They start by standing in a line: a stands in position 0, b stands in position 1, and so on until p, which stands in position 15.

The programs' dance consists of a sequence of dance moves:

- Spin, written sX, makes X programs move from the end to the front, but maintain their order otherwise. (For example, s3 on abcde produces cdeab).
- Exchange, written xA/B, makes the programs at positions A and B swap places.
- Partner, written pA/B, makes the programs named A and B swap places.

For example, with only five programs standing in a line (abcde), they could do the following dance:

- s1, a spin of size 1: eabcd.
- x3/4, swapping the last two programs: eabdc.
- pe/b, swapping programs e and b: baedc.

After finishing their dance, the programs end up in order baedc.

You watch the dance for a while and record their dance moves (your puzzle input). In what order are the programs standing after their dance?

My code:

    def main():
        moves = INPUT.split(',')  
        programs = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']
        programs = calculate_moves(moves, programs)
        print(''.join(programs))

    def calculate_moves(moves, programs):
        for m in moves:
            val = m[1:].split('/')
            if m[0] == 'p':
                index_0 = programs.index(val[0])
                index_1 = programs.index(val[1])
                programs[index_0], programs[index_1] = programs[index_1], programs[index_0]
            elif m[0] == 'x':
                programs[int(val[0])], programs[int(val[1])] = programs[int(val[1])], programs[int(val[0])]
            elif m[0] == 's':
                for i in range(len(programs)-int(val[0])):
                    programs += [programs.pop(0)]
        return programs

Part 2 (copied from [AoC page](http://adventofcode.com/2017/day/16))
------
Now that you're starting to get a feel for the dance moves, you turn your attention to the dance as a whole.

Keeping the positions they ended up in from their previous dance, the programs perform it again and again: including the first dance, a total of one billion (1000000000) times.

In the example above, their second dance would begin with the order baedc, and use the same dance moves:

- s1, a spin of size 1: cbaed.
- x3/4, swapping the last two programs: cbade.
- pe/b, swapping programs e and b: ceadb.

In what order are the programs standing after their billion dances?

My code

    def main():
        moves = INPUT.split(',')
        programs_origin = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']   
        programs = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']
        term = 0
        while term == 0 or programs != programs_origin:
            programs_origin = calculate_moves(moves, programs_origin)
            term += 1
        for x in range(1000000000 % term):
            programs = calculate_moves(moves, programs)
        print(''.join(programs))

    def calculate_moves(moves, programs):
        for m in moves:
            val = m[1:].split('/')
            if m[0] == 'p':
                index_0 = programs.index(val[0])
                index_1 = programs.index(val[1])
                programs[index_0], programs[index_1] = programs[index_1], programs[index_0]
            elif m[0] == 'x':
                programs[int(val[0])], programs[int(val[1])] = programs[int(val[1])], programs[int(val[0])]
            elif m[0] == 's':
                for i in range(len(programs)-int(val[0])):
                    programs += [programs.pop(0)]
        return programs
 