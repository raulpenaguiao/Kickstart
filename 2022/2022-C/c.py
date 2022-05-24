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
    #This is the list with all the information of the ants, that we will use to sort.
    for i in range(N):
        s = input().split(" ")
        P[i] = [i, int(s[0])]
        D[i] = int(s[1])
        if D[i] == 0:
            l += [["L", P[i][1], i]]
            #the second entry denotes the distance to the edge of the rod
        else:
            l += [["R", L - P[i][1], i]]
            #in this case, the edge of the rod to consider is the right side
    l.sort(key = lambda x: [x[1], x[2]])
    #After sorting, this list has the label of each ant in the order in which some other ant fell.
    #Note how in in case of a tie, we use the third entry to deal with the tie break
    P.sort(key = lambda x: [x[1], x[0]])
    lef_lim = 0
    rig_lim = N-1
    ans = []
    #This is the vector that will have the indices, together with the time that the ants will take to fall
    for i in range(N):
        if l[i][0] == "L":
            ans += [[P[lef_lim][0] + 1, l[i][1]]]
            lef_lim += 1
        else:
            ans += [[P[rig_lim][0] + 1, l[i][1]]]
            rig_lim -= 1
    ans.sort(key = lambda x: [x[1], x[0]])
    print("Case #{}: {}".format(turn+1, " ".join([str(t[0]) for t in ans])))
