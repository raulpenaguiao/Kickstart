import numpy as np
import queue

pascal  = [[0 for j in range(450)] for i in range(450)]
pascal[0][0] = 1
for i in range(1, 420):
    pascal[i][0] = 1
    for j in range(1, i+1):
        pascal[i][j] = pascal[i-1][j] + pascal[i-1][j-1]

def inv_mod(a, p):
    #a ** p-2
    if a == 0:
        return a
    ans = 1
    power = a
    exp = p - 2
    while exp > 0:
        if exp % 2 == 1:
            ans *= power
            ans %= p
        exp //= 2
        power *= power
        power %= p
    return ans

"""
for i in range(10):
    print(pascal[i][:i+1])
"""

LIM = 420
prime = 1000000007
inv_pasc = [[inv_mod(pascal[i][j]%prime, prime) for j in range(LIM)] for i in range(LIM)]

"""
for i in range(10):
    print(inv_pasc[i][:i+1])
"""


def is_pal(s):
#    print("s = ", s)
    if len(s) <= 1:
        return True
    if s[0] == s[-1]:
        return is_pal(s[1:-1])
    return False


#is_pal("dasd")

"""
def perms(N):##Identify a permutation with a list (a0, a1, ..., an-1) st 0 <= ai <= i
    if N == 0:
        return [[]]
    ans = []
    for perm in perms(N-1):
        for i in range(N):
            ans += [perm + [[i]]]
    return ans
"""


T = int(input())
for turn in range(T):
    N = int(input())
    s = input()
    iterator = 0
    lim = 2 ** N
    acu = 0
    for iterator in range(lim-1):
        new_str = ""
        k = iterator
        i = 0
        while k > 0:
            if k%2 == 1:
                new_str += s[i]
            k //= 2
            i+= 1
        if is_pal(new_str):
#            print("str = ", new_str)
#            print(inv_pasc[N][len(new_str)])
            acu += inv_pasc[N][len(new_str)]
            acu %= prime
    print("Case #{}: {}".format(turn+1, acu))
