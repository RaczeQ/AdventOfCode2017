# -*- coding: utf-8 -*-
'''
Created on 13.12.2017

@author: RaczeQ
'''

INPUT = '''0: 3
1: 2
2: 4
4: 4
6: 5
8: 6
10: 8
12: 8
14: 6
16: 6
18: 8
20: 8
22: 6
24: 12
26: 9
28: 12
30: 8
32: 14
34: 12
36: 8
38: 14
40: 12
42: 12
44: 12
46: 14
48: 12
50: 14
52: 12
54: 10
56: 14
58: 12
60: 14
62: 14
66: 10
68: 14
74: 14
76: 12
78: 14
80: 20
86: 18
92: 14
94: 20
96: 18
98: 17'''

def main():
    rows = INPUT.split('\n')
    layers = {}
    actual_layer = 0
    length = int(rows[-1].strip().split(':')[0])
    for row in rows:   
        values = row.strip().split(':')
        layers[int(values[0])] = int(values[1])
    severity = 0
    for k, l in layers.iteritems():
        if k % ((l-1)*2) == 0:
            severity += k * l
    print(severity) # OUTPUT: 2160

if __name__ == "__main__":
    main()