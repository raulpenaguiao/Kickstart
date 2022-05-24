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


#print("pascal inverse done")
matrix = [[[0 for k in range(402)] for i in range(402)] for j in range(402)]

#set matrix entries at level k = 0 and k = 1
for i in range(400):
    for j in range(i+2):
        matrix[i][j][0] = 1
        matrix[i][j][1] = i - j + 1
#print("memory done")


T = int(input())
for turn in range(T):
    N = int(input())
    s = input()
    
    #Set all entries above k = 0 back to 0
    for i in range(N):
        for j in range(i):
            for k in range(2, N):
                matrix[i][j][k] = 0
    for i in range(1, N):
        for j in range(i-1, -1, -1):
            for k in range(2, N):
                matrix[i][j][k] = matrix[i-1][j][k] + matrix[i][j+1][k] - matrix[i-1][j+1][k]
            if s[i] == s[j]:
                for k in range(2, N):
                    matrix[i][j][k] += matrix[i-1][j+1][k-2]



    acc = 0
    for k in range(N):
        acc += matrix[N-1][0][k] * inv_pasc[N][k]
        acc %= prime
    print("Case #{}: {}".format(turn+1, acc))
