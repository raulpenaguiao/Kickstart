import numpy as np
import queue
T = int(input())
for turn in range(T):
    s = input().split(" ")
    N = int(s[0])
    L = int(s[1])
    P = [0 for i in range(N)]
    D = [0 for i in range(N)]
    l = []
    for i in range(N):
        s = input().split(" ")
        P[i] = [i, int(s[0])]
        D[i] = int(s[1])
        if D[i] == 0:
            l += [["L", P[i][1], i]]
        else:
            l += [["R", L - P[i][1], i]]
    l.sort(key = lambda x: [x[1], x[2]])
    P.sort(key = lambda x: [x[1], x[0]])
    lef_lim = 0
    rig_lim = N-1
    ans = []
    for i in range(N):
        if l[i][0] == "L":
            ans += [[P[lef_lim][0] + 1, l[i][1]]]
            lef_lim += 1
        else:
            ans += [[P[rig_lim][0] + 1, l[i][1]]]
            rig_lim -= 1
    ans.sort(key = lambda x: [x[1], x[0]])
    #print("l = ", l)
    #print("P = ", P)
    #print("ans = ", ans)
    print("Case #{}: {}".format(turn+1, " ".join([str(t[0]) for t in ans])))
