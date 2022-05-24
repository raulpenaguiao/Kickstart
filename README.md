### Kickstart programs ###


## Index ##

 - Common techniques
 - 2022 Round C



## Techniques ##

 - String manipulation
 - Dynamic programming
 - Graph theory

##2022 Round C ##

When: 22nd May
Where: SF California
How: Python 3.7


# Problem 1 - New Password after 11min # 

Attempts: 1
Result: Completed

Description:
Check if a string contains certain characters and has some length.
If not, alter the string to get it to satisfy these properties.

Limitations:
String may be up to 10 ** 4 in size

Techniques:
 - String manipulation


# Problem 2 - Range Partition after 54min #

Attempts: 3
Result: Completed

Description:
Given integers N, X, Y, find and print a subset of {1, ..., N} whose sum is X/Y of the complement sum.

Limitations:
N up to 5000, X and Y up to 10 ** 8
gcd(X, Y) = 1

Techniques:
 - Greatest common divisor
 - Modular arithmetic
 - Algebraic manipulation
 - Greedy algorithm

Development:

After some algebraic manipulation, it was shown that the task is possible if the total sum of 1 up to N is a multiple of X + Y

The target sum value is N * (N+1) * X * (X + Y) / 2

To find a subset of {1, ..., N} that sums up to a given value one can use a greedy algorithm, by adding to the set the highest possible value.

Possible extentions:

If the problem did not require for one to print the solution, one can find the given subset more efficiently as a form of {a} u {b, b+1, ..., N-1, N} for suitable a, b.

# Problem 3 - Ants on a stick #

Attempts: 1
Result: Completed after 1h20

Description:
Ants on a rod walk at the same speed but not same direction. They do not cross, bumping onto eachother and reflecting back.
Given the initial position of the ants, what is the order in which the ants will fall off the rod.

Techniques:
 - Sorting algorithms

Limitations:
All positions of the ants are distinct, but the time that the ants fall off may be the same.
In this case, one should print first the ant with the smallest index
N up to 10 ** 5, L up to 10 ** 9

Development:
The order in which the ants are in the rod never changes, as they never cross only reflect. Therefore, only the ants on the sides of the rod are the ones that may fall.

The path that the ants take when labels are dropped is constant speed and direction, so we can compute the order in which the ants fall from the right or the left side of the rod.
This gives us the order in which they fall.


# Problem 4 - Palindromid Deletions #

Attempts: 2
Result: TLE on the largest dataset, done in 2h39min

Description:
Given a word, iteratively remove a letter from it at random uniformly.
Count how many times one ends up with a palindromic word after a removal.
The total, X, is a random variable. Compute its expected value as a fraction p/q and compute the number p * q^(-1) module a big prime.

Techniques:
 - Palindromic words
 - Inverse module
 - Pascal triangle
 - Dynamic programming
 - Random processes

Limitations:
The size of the string is up to 8 for the small set size, and 400 for the large set size.

Development:
The greedy algorithm works for the small set size, where one runs over all possible runs of the deletion process.
The way I chose to implement is to run all subwords and, when a palindrom is found, count all the processes that go through this word, which turns out to be a binomial coefficient, and add it all up, getting:

$$ \mathbb{E}[X] = \sum_{k = 0}^{N-1} \#{\text{ palindromic words of size } k\} \binom{N}{k}^{-1} $$

This algorithm runs over all subsets of size N, so it is too big for the large set.
This was not overcome before the end of the competition.


# Problem 4 ARS - 
After revealing solution, it became clear that dynammic programing can be used



