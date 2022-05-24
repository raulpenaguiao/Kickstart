import numpy as np
import queue


#Here we compute the pascal triangle up to the line 450
pascal  = [[0 for j in range(450)] for i in range(450)]
pascal[0][0] = 1
for i in range(1, 420):
    pascal[i][0] = 1
    for j in range(1, i+1):
        pascal[i][j] = pascal[i-1][j] + pascal[i-1][j-1]


#This function uses the little fermat theorem and fast exponentiation to compute modular inverses
#This function does not give the right answer if used with 0
def inv_mod(a, p):
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


#Because we will be using the inverse of pascal numbers, they are precomputed here up to the line 420
prime = 1000000007
inv_pasc = [[inv_mod(pascal[i][j]%prime, prime) for j in range(420)] for i in range(420)]



#Naive recursive function that checks if a word is a palindrome
def is_pal(s):
    if len(s) <= 1:
        return True
    if s[0] == s[-1]:
        return is_pal(s[1:-1])
    return False



T = int(input())
for turn in range(T):
    N = int(input())
    s = input()
    iterator = 0
    lim = 2 ** N
    acu = 0
    for iterator in range(lim-1):
        #iterator runs over 0 an a power of two, essentially running over subsets of a set of length lim
        #the substring will be recorded in new_str
        new_str = ""
        k = iterator
        i = 0
        while k > 0:
            if k%2 == 1:
                new_str += s[i]
            k //= 2
            i+= 1
        if is_pal(new_str):
            #the inverse pascal term is the term that we need to add to our expected value
            acu += inv_pasc[N][len(new_str)]
            acu %= prime
    print("Case #{}: {}".format(turn+1, acu))
