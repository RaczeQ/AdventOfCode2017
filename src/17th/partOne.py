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
    rows = INPUT.split('\n')
    registers = {}
    actual_row = 0
    recovered = False
    recovered_val = 0
    while not recovered:
        val = rows[actual_row].split(' ')
        reg = val[1]
        if not reg in registers:
            registers[reg] = {'val':0}
        num = get_value(val[-1], registers)
        if val[0] == 'set':
            registers[reg]['val'] = num
        elif val[0] == 'snd':
            registers[reg]['snd'] = registers[reg]['val']
        elif val[0] == 'add':
            registers[reg]['val'] += num
        elif val[0] == 'mul':
            registers[reg]['val'] *= num
        elif val[0] == 'mod':
            registers[reg]['val'] %= num
        elif val[0] == 'rcv' and registers[reg]['val'] != 0 and 'snd' in registers[reg]:
            recovered = True
            recovered_val = registers[reg]['snd']
            registers[reg]['val'] = recovered_val
        elif val[0] == 'jgz' and registers[reg]['val'] > 0:
            actual_row += (num-1)
        actual_row += 1
    print(recovered_val) # OUTPUT: 3423

def get_value(val, registers):
    try:
        return int(val)
    except:
        return registers[val]['val']

if __name__ == "__main__":
    main()