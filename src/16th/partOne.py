# -*- coding: utf-8 -*-
'''
Created on 17.12.2017

@author: RaczeQ
'''

INPUT = '''386'''

def main():
    steps = int(INPUT)  
    buffer = [0]
    actual_pos = 0
    for i in range(1, 2018):
        actual_pos = (actual_pos + steps % i) % i + 1
        buffer.insert(actual_pos, i)
    print(buffer[actual_pos+1]) # OUTPUT: 419

if __name__ == "__main__":
    main()