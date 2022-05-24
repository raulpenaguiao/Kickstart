import numpy as np
import queue

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digs = "1234567890"
spec = "#@*&"

def has_no_common_char(s1, s2):
    for ch1 in s1:
        for ch2 in s2:
            if ch1 == ch2:
                return False
    return True

T = int(input())
for turn in range(T):
    n = int(input())
    s = input()
    """
    for i in range(n):
        s+= str(input())
    """
    if has_no_common_char(s, lower):
        s+="a"
    if has_no_common_char(s, upper):
        s+= "A"
    if has_no_common_char(s, digs):
        s+= "1"
    if has_no_common_char(s, spec):
        s += "#"
    while len(s) < 7:
        s+= "a"
    print("Case #{}: {}".format(turn+1, s))
