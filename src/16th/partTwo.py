# -*- coding: utf-8 -*-
'''
Created on 17.12.2017

@author: RaczeQ
'''

INPUT = '''386'''

def main():
    steps = int(INPUT)  
    actual_pos = 0
    actual_val = 0
    for i in range(1, 50000001):
        actual_pos = (actual_pos + steps % i) % i + 1
        if actual_pos == 1:
            actual_val = i
    print(actual_val) # OUTPUT: 46038988

if __name__ == "__main__":
    main()