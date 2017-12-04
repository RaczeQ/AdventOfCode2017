# -*- coding: utf-8 -*-
'''
Created on 03.12.2017

@author: RaczeQ
'''

INPUT = 325489

def main():
    x_pos = y_pos = 0
    max_right = max_up = max_left = max_down = 0
    last_move = "down"
    next_move = "right"
    grid_values = {}
    grid_values['0 0'] = 1

    while grid_values[str(x_pos) + " " + str(y_pos)] < INPUT:
        if next_move == "right":
            if last_move != "right":
                max_right += 1
            last_move = "right"
            x_pos += 1
            grid_values[str(x_pos) + " " + str(y_pos)] = getNeighboursSum(grid_values, x_pos, y_pos)
            if x_pos == max_right:
                next_move = "up"
        elif next_move == "up":
            if last_move != "up":
                max_up += 1
            last_move = "up"
            y_pos += 1
            grid_values[str(x_pos) + " " + str(y_pos)] = getNeighboursSum(grid_values, x_pos, y_pos)
            if y_pos == max_up:
                next_move = "left"
        elif next_move == "left":
            if last_move != "left":
                max_left -= 1
            last_move = "left"
            x_pos -= 1
            grid_values[str(x_pos) + " " + str(y_pos)] = getNeighboursSum(grid_values, x_pos, y_pos)
            if x_pos == max_left:
                next_move = "down"
        elif next_move == "down":
            if last_move != "down":
                max_down -= 1
            last_move = "down"
            y_pos -= 1
            grid_values[str(x_pos) + " " + str(y_pos)] = getNeighboursSum(grid_values, x_pos, y_pos)
            if y_pos == max_down:
                next_move = "right"
    
    print(grid_values[str(x_pos) + " " + str(y_pos)]) # OUTPUT: 330785

def getNeighboursSum(grid_values, x_pos, y_pos):
    result = 0
    for x in range(x_pos-1, x_pos+2):
        for y in range(y_pos-1, y_pos+2):
            if x != x_pos or y != y_pos:
                key = str(x) + " " + str(y)
                if key in grid_values:
                    result += grid_values[key]
    return result

if __name__ == "__main__":
    main()