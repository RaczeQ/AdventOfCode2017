# Day 19th: Particle Swarm

Part 1 (copied from [AoC page](http://adventofcode.com/2017/day/20))
------
Suddenly, the GPU contacts you, asking for help. Someone has asked it to simulate too many particles, and it won't be able to finish them all in time to render the next frame at this rate.

It transmits to you a buffer (your puzzle input) listing each particle in order (starting with particle 0, then particle 1, particle 2, and so on). For each particle, it provides the X, Y, and Z coordinates for the particle's position (p), velocity (v), and acceleration (a), each in the format <X,Y,Z>.

Each tick, all particles are updated simultaneously. A particle's properties are updated in the following order:

- Increase the X velocity by the X acceleration.
- Increase the Y velocity by the Y acceleration.
- Increase the Z velocity by the Z acceleration.
- Increase the X position by the X velocity.
- Increase the Y position by the Y velocity.
- Increase the Z position by the Z velocity.

Because of seemingly tenuous rationale involving z-buffering, the GPU would like to know which particle will stay closest to position <0,0,0> in the long term. Measure this using the Manhattan distance, which in this situation is simply the sum of the absolute values of a particle's X, Y, and Z position.

For example, suppose you are only given two particles, both of which stay entirely on the X-axis (for simplicity). Drawing the current states of particles 0 and 1 (in that order) with an adjacent a number line and diagram of current X positions (marked in parenthesis), the following would take place:

    p=< 3,0,0>, v=< 2,0,0>, a=<-1,0,0>    -4 -3 -2 -1  0  1  2  3  4
    p=< 4,0,0>, v=< 0,0,0>, a=<-2,0,0>                         (0)(1)

    p=< 4,0,0>, v=< 1,0,0>, a=<-1,0,0>    -4 -3 -2 -1  0  1  2  3  4
    p=< 2,0,0>, v=<-2,0,0>, a=<-2,0,0>                      (1)   (0)

    p=< 4,0,0>, v=< 0,0,0>, a=<-1,0,0>    -4 -3 -2 -1  0  1  2  3  4
    p=<-2,0,0>, v=<-4,0,0>, a=<-2,0,0>          (1)               (0)

    p=< 3,0,0>, v=<-1,0,0>, a=<-1,0,0>    -4 -3 -2 -1  0  1  2  3  4
    p=<-8,0,0>, v=<-6,0,0>, a=<-2,0,0>                         (0)   

At this point, particle 1 will never be closer to <0,0,0> than particle 0, and so, in the long run, particle 0 will stay closest.

Which particle will stay closest to position <0,0,0> in the long term?

My code:

    import numpy as np

    def main():
        rows = INPUT.split('\n')
        accelerations = []
        velocities = []
        distances = []
        for i in range(len(rows)):
            values = rows[i].split(', ')
            accelerations.append(sum([abs(int(x)) for x in values[2][3:-1].split(',')]))
            velocities.append(sum([abs(int(x)) for x in values[1][3:-1].split(',')]))
            distances.append(sum([abs(int(x)) for x in values[0][3:-1].split(',')]))
        dtype = [('idx', int), ('acc', int), ('vel', int), ('dst', int)]
        zipped_list = np.array(zip(range(len(rows)), accelerations, velocities, distances), dtype=dtype)
        values = np.sort(zipped_list, order=['acc', 'vel', 'dst'])
        print(values[0][0])

Part 2 (copied from [AoC page](http://adventofcode.com/2017/day/20))
------
To simplify the problem further, the GPU would like to remove any particles that collide. Particles collide if their positions ever exactly match. Because particles are updated simultaneously, more than two particles can collide at the same time and place. Once particles collide, they are removed and cannot collide with anything else after that tick.

For example:

    p=<-6,0,0>, v=< 3,0,0>, a=< 0,0,0>    
    p=<-4,0,0>, v=< 2,0,0>, a=< 0,0,0>    -6 -5 -4 -3 -2 -1  0  1  2  3
    p=<-2,0,0>, v=< 1,0,0>, a=< 0,0,0>    (0)   (1)   (2)            (3)
    p=< 3,0,0>, v=<-1,0,0>, a=< 0,0,0>

    p=<-3,0,0>, v=< 3,0,0>, a=< 0,0,0>    
    p=<-2,0,0>, v=< 2,0,0>, a=< 0,0,0>    -6 -5 -4 -3 -2 -1  0  1  2  3
    p=<-1,0,0>, v=< 1,0,0>, a=< 0,0,0>             (0)(1)(2)      (3)   
    p=< 2,0,0>, v=<-1,0,0>, a=< 0,0,0>

    p=< 0,0,0>, v=< 3,0,0>, a=< 0,0,0>    
    p=< 0,0,0>, v=< 2,0,0>, a=< 0,0,0>    -6 -5 -4 -3 -2 -1  0  1  2  3
    p=< 0,0,0>, v=< 1,0,0>, a=< 0,0,0>                       X (3)      
    p=< 1,0,0>, v=<-1,0,0>, a=< 0,0,0>

    ------destroyed by collision------    
    ------destroyed by collision------    -6 -5 -4 -3 -2 -1  0  1  2  3
    ------destroyed by collision------                      (3)         
    p=< 0,0,0>, v=<-1,0,0>, a=< 0,0,0>

In this example, particles 0, 1, and 2 are simultaneously destroyed at the time and place marked X. On the next tick, particle 3 passes through unharmed.

How many particles are left after all collisions are resolved?

My code

    from sympy import *

    def main():
        rows = INPUT.split('\n')
        pts = {}
        for i in range(len(rows)):
            values = rows[i].split(', ')
            pts[i] = {}
            pts[i]['p'] = [int(x) for x in values[0][3:-1].split(',')]
            pts[i]['v'] = [int(x) for x in values[1][3:-1].split(',')]
            pts[i]['a'] = [int(x) for x in values[2][3:-1].split(',')]
        finished = False
        while not finished:
            pos = {}
            for i, p in pts.iteritems():
                if str(p['p']) in pos:
                    pos[str(p['p'])].append(i)
                else:
                    pos[str(p['p'])] = [i]
            for l in pos.itervalues():
                if len(l) > 1:
                    for ind in l:
                        del pts[ind]
            for i, p in pts.iteritems():
                p['v'] = [x + y for x, y in zip(p['v'], p['a'])]
                p['p'] = [x + y for x, y in zip(p['p'], p['v'])]
            finished = True
            for i in range(len(pts)):
                for j in range(i+1, len(pts)):
                    if finished:
                        p0 = pts[pts.keys()[i]]
                        p1 = pts[pts.keys()[j]]
                        t = Symbol('t')
                        eq0_x = p0['p'][0] + t*p0['v'][0] + t**2*p0['a'][0]
                        eq0_y = p0['p'][1] + t*p0['v'][1] + t**2*p0['a'][1]
                        eq0_z = p0['p'][2] + t*p0['v'][2] + t**2*p0['a'][2]
                        eq1_x = p1['p'][0] + t*p1['v'][0] + t**2*p1['a'][0]
                        eq1_y = p1['p'][1] + t*p1['v'][1] + t**2*p1['a'][1]
                        eq1_z = p1['p'][2] + t*p1['v'][2] + t**2*p1['a'][2]
                        s = solve([eq0_x - eq1_x, eq0_y - eq1_y, eq0_z - eq1_z], t)
                        if len(s) > 0:
                            finished = False
        print(len(pts))
 