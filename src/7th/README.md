# Day 7th: Memory Reallocation

Part 1 (copied from [AoC page](http://adventofcode.com/2017/day/8))
------
You receive a signal directly from the CPU. Because of your recent assistance with jump instructions, it would like you to compute the result of a series of unusual register instructions.

Each instruction consists of several parts: the register to modify, whether to increase or decrease that register's value, the amount by which to increase or decrease it, and a condition. If the condition fails, skip the instruction without modifying the register. The registers all start at 0. The instructions look like this:

    b inc 5 if a > 1
    a inc 1 if b < 5
    c dec -10 if a >= 1
    c inc -20 if c == 10

These instructions would be processed as follows:

- Because a starts at 0, it is not greater than 1, and so b is not modified.
- a is increased by 1 (to 1) because b is less than 5 (it is 0).
- c is decreased by -10 (to 10) because a is now greater than or equal to 1 (it is 1).
- c is increased by -20 (to -10) because c is equal to 10.

After this process, the largest value in any register is 1.

You might also encounter <= (less than or equal to) or != (not equal to). However, the CPU doesn't have the bandwidth to tell you what all the registers are named, and leaves that to you to determine.

What is the largest value in any register after completing the instructions in your puzzle input?

My code:

    multiplier = {
        'inc': 1,
        'dec': -1
    }
    rows = INPUT.split('\n')
    registers = {}
    max_val = 0
    for row in rows:
        values = row.split(' ')
        register_name = values[0]
        if register_name not in registers:
            registers[register_name] = 0
        instruction = multiplier[values[1]]
        value = int(values[2])
        cond_register = values[4]
        if cond_register not in registers:
            registers[cond_register] = 0
        cond_predicate = values[5]
        cond_value = int(values[6])
        if eval('{} {} {}'.format(registers[cond_register], cond_predicate, cond_value)):
            registers[register_name] += value * instruction
    for k,v in registers.iteritems():
        if v > max_val:
            max_val = v
    print(max_val)

Part 2 (copied from [AoC page](http://adventofcode.com/2017/day/8))
------
To be safe, the CPU also needs to know the highest value held in any register during this process so that it can decide how much memory to allocate to these operations. For example, in the above instructions, the highest value ever held was 10 (in register c after the third instruction was evaluated).

My code

    multiplier = {
        'inc': 1,
        'dec': -1
    }
    rows = INPUT.split('\n')
    registers = {}
    max_val = 0
    for row in rows:
        values = row.split(' ')
        register_name = values[0]
        if register_name not in registers:
            registers[register_name] = 0
        instruction = multiplier[values[1]]
        value = int(values[2])
        cond_register = values[4]
        if cond_register not in registers:
            registers[cond_register] = 0
        cond_predicate = values[5]
        cond_value = int(values[6])
        if eval('{} {} {}'.format(registers[cond_register], cond_predicate, cond_value)):
            registers[register_name] += value * instruction
            if registers[register_name] > max_val:
                max_val = registers[register_name]
    print(max_val)
 