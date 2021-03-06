# -*- coding: utf-8 -*-
'''
Created on 22.12.2017

@author: RaczeQ
'''

INPUT = '''......#.#....####.##.#...
##.##.#.####.##.#.#.##..#
.#.#######.#..###......#.
#####..###.##..####.#..##
.#..#.##...#.####.#....#.
#.#...#.#####.#.#####..##
..##.#..######....####.##
#.##.#....#.#.##........#
.#....#....###.#....####.
....#..##.#.#.##.#....#.#
.#.##.#.####..#..#.##..##
##.####.#..###...#.#...##
....#....#..#..####.##...
..#.#.#.#..#.###...#...##
.#..#..##..##.#.#..##.#..
####.#.#...##.#..##.###..
###.#....#...#..#..#...##
.##....##.......####.#.##
#.#.##.#.#..#.#..##..####
...#..##.#.####.....##.##
.#.##.#####.#.#....#####.
##......#..#.###..####.##
..#...#########.....#..##
##..###.##...###.#.#.#.#.
..###.###.##.#.###....#.#'''

def main():
    points = [[int(x) for x in row] for row in INPUT.replace('#', '1').replace('.', '0').split('\n')]
    grid = {}
    for y in range(len(points)):
        grid[y] = {}
        for x in range(len(points)):
            grid[y][x] = points[y][x]
    pos = [len(grid[0])/2, len(grid)/2]
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)] # U, R, D, L
    d = 0
    infections = 0
    for i in range(10000):
        if not pos[1] in grid:
            grid[pos[1]] = {}
        if not pos[0] in grid[pos[1]]:
            grid[pos[1]][pos[0]] = 0
        if grid[pos[1]][pos[0]] == 1:
            d = (d + 1) % 4
            grid[pos[1]][pos[0]] = 0
        elif grid[pos[1]][pos[0]] == 0:
            d = (d - 1) % 4
            grid[pos[1]][pos[0]] = 1
            infections += 1
        pos[0] += directions[d][0]
        pos[1] += directions[d][1]
    print(infections) # OUTPUT: 5259 
    
if __name__ == "__main__":
    main()