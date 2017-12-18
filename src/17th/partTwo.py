# -*- coding: utf-8 -*-
'''
Created on 18.12.2017

@author: RaczeQ
'''

INPUT = '''set i 31
set a 1
mul p 17
jgz p p
mul a 2
add i -1
jgz i -2
add a -1
set i 127
set p 618
mul p 8505
mod p a
mul p 129749
add p 12345
mod p a
set b p
mod b 10000
snd b
add i -1
jgz i -9
jgz a 3
rcv b
jgz b -1
set f 0
set i 126
rcv a
rcv b
set p a
mul p -1
add p b
jgz p 4
snd a
set a b
jgz 1 3
snd b
set f 1
add i -1
jgz i -11
snd a
jgz f -16
jgz a -19'''

def main():
    data = [row.split() for row in INPUT.split('\n')]
    prog1 = {}
    prog2 = {}
    prog1['p'] = 0
    prog2['p'] = 1
    programs = [prog1, prog2]

    sent = 0
    instr = [0,0]
    queues = [[],[]]
    status = ['w','w'] # w -> work, r -> receive, f -> finished
    prog = 0
    reg = programs[prog]
    i = instr[0]
    while True:
        if not data[i][1] in reg:
            reg[data[i][1]] = 0
        val = get_value(data[i][-1], reg)
        if data[i][0] == 'set':
            reg[data[i][1]] = val
        elif data[i][0] == 'add':
            reg[data[i][1]] += val
        elif data[i][0] == 'mul':
            reg[data[i][1]] *= val
        elif data[i][0] == 'mod':
            reg[data[i][1]] %= val
        elif data[i][0] == 'snd':
            sent += prog == 1
            queues[prog].append(val)
        elif data[i][0] == 'jgz' and get_value(data[i][1], reg) > 0:
            i += val-1
        elif data[i][0] == 'rcv':
            if len(queues[1-prog]) > 0:
                status[prog] = 'w'
                reg[data[i][1]] = queues[1-prog].pop(0)
            else:
                if status[1-prog] == 'f' or (len(queues[prog])==0 and status[1-prog]=='r'):
                    break
                instr[prog] = i
                status[prog] = 'r'
                prog = 1 - prog
                i = instr[prog] - 1
                reg = programs[prog]
        i += 1
        if i < 0 or i >= len(data):
            if status[1-prog] == 'f':
                break
            status[prog] = 'f'
            instr[prog] = i
            prog = 1 - prog
            i = instr[prog]
            reg = programs[prog]
    print(sent) # OUTPUT: 7493

def get_value(val, registers):
    try:
        return int(val)
    except:
        return registers[val]

if __name__ == "__main__":
    main()