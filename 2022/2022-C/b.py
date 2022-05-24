import numpy as np
import queue

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
        #This is the list where we will record the subset with the given sum
        l = N
        s = (T // (X + Y)) * X
        #Run greedy algorithm to find next term in the set {1, ..., l} to add in order to obtain the sum s
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


