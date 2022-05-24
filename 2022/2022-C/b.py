import numpy as np
import queue
"""legacy functions that are not needed
def gcd(a, b):
    if a == 0:
        return b
    return gcd(b, a%b)

def prt(t, l, s):
    print("t = ", t)
    print("l = ", l , " and s = ", s)
    if s == 0:
        return t
    if l >= s:
        return t + [str(s)]
    return prt(t+ [str(l)], l-1, s - l)
"""

T = int(input())
for turn in range(T):
    s = input()
    t = s.split(" ")
    N = int(t[0])
    X = int(t[1])
    Y = int(t[2])
    T = N * (N+1)//2
    if T%(X + Y) > 0:
        print("Case #{}: IMPOSSIBLE".format(turn+1))
    else:
        print("Case #{}: POSSIBLE".format(turn+1))
        t = []
        l = N
        s = (T // (X + Y)) * X
        while s > 0:
            if l >= s:
                t += [str(s)]
                s = 0
            else:
                t += [str(l)]
                s -= l
                l -= 1
        print(len(t))
        print(" ".join(t))


