# -*- coding: utf-8 -*-
'''
Created on 03.12.2017

@author: RaczeQ
'''

INPUT = 325489

def main():
    remaining_steps = INPUT - 1
    distance = 0
    x_pos = y_pos = 0
    max_right = max_up = max_left = max_down = 0
    last_move = "down"

    while remaining_steps > 0 :
        if last_move == "down":
            max_right += 1
            x_pos, remaining_steps = evaluateSteps(x_pos, remaining_steps, max_right)
            last_move = "right"
        elif last_move == "right":
            max_up += 1
            y_pos, remaining_steps = evaluateSteps(y_pos, remaining_steps, max_up)
            last_move = "up"
        elif last_move == "up":
            max_left -= 1
            x_pos, remaining_steps = evaluateSteps(x_pos, -remaining_steps, max_left)
            last_move = "left"
        elif last_move == "left":
            max_down -= 1
            y_pos, remaining_steps = evaluateSteps(y_pos, -remaining_steps, max_down)
            last_move = "down"
    
    distance = abs(x_pos) + abs(y_pos)
    print(distance) # OUTPUT: 552

def evaluateSteps(pos, remaining_steps, max_pos):
    if abs(pos - max_pos) > abs(remaining_steps):
        pos = pos + remaining_steps
        remaining_steps = 0
    else:
        remaining_steps = abs(remaining_steps) - abs(pos - max_pos)
        pos = max_pos
    return pos, remaining_steps

if __name__ == "__main__":
    main()