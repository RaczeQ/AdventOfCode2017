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
    points = [[x for x in row] for row in INPUT.replace('#', 'I').replace('.', 'C').split('\n')]
    grid = {}
    for y in range(len(points)):
        grid[y] = {}
        for x in range(len(points)):
            grid[y][x] = points[y][x]
    pos = [len(grid[0])/2, len(grid)/2]
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)] # U, R, D, L
    d = 0
    infections = 0
    for i in range(10000000):
        if not pos[1] in grid:
            grid[pos[1]] = {}
        if not pos[0] in grid[pos[1]]:
            grid[pos[1]][pos[0]] = 'C'
        if grid[pos[1]][pos[0]] == 'I':
            d = (d + 1) % 4
            grid[pos[1]][pos[0]] = 'F'
        elif grid[pos[1]][pos[0]] == 'C':
            d = (d - 1) % 4
            grid[pos[1]][pos[0]] = 'W'
        elif grid[pos[1]][pos[0]] == 'W':
            infections += 1
            grid[pos[1]][pos[0]] = 'I'
        elif grid[pos[1]][pos[0]] == 'F':
            d = (d + 2) % 4
            grid[pos[1]][pos[0]] = 'C'
        pos[0] += directions[d][0]
        pos[1] += directions[d][1]
    print(infections) # OUTPUT: 2511722 

if __name__ == "__main__":
    main()