# logic building
# patterns
"""
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
"""
'''
def nForest(n:int) -> None:
    for i in range(n):
        print('* ' * n )

nForest(5)
'''

"""
* 
* * 
* * * 
* * * * 
* * * * * 
"""
"""
def nForest(n:int) -> None:
    for i in range(n):
        print('* ' * (i+1))

nForest(5)
"""

"""
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
"""
"""
def nTriangle(n:int) ->None:
    for i in range(n):
        for j in range(i+1):
            print(j+1, end=' ')
        print()

nTriangle(5)
"""

"""
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 
"""
"""
def Triangle(n:int) ->None:
    for i in range(n):
        print(f"{i+1} " * (i+1) )

Triangle(5)
"""
"""
def Triangle(n:int) ->None:
    for i in range(n):
        for j in range(i+1):
            print(i+1, end=' ')
        print()
Triangle(5)
"""

"""
* * * * * 
* * * * 
* * * 
* * 
* 
"""
"""
def seeding(n: int) -> None:
    for i in range(n):
        count = n - i
        print('* ' * count)

seeding(5)
"""

"""
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 
"""
"""
def nNumberTriangle(n: int) -> None:
    for i in range(n):
        for j in range(n-i):
            print(j+1, end=' ')
        print()
nNumberTriangle(5)
"""

"""
    *
   ***
  *****
 *******
*********
"""
"""
def nStarTriangle(n: int) -> None:
    for i in range(n):
        space = n - i-1
        star = 2*i +1
        print(' ' * space + '*' * star)

nStarTriangle(5)
"""
"""
def nStarDiamond(n: int) -> None:

    # Initialise 'gap' and 'stars'.
    gap = n-1
    stars = 1
    for i in range(n):
        for j in range(gap):
            print(' ', end="")
        for j in range(gap, gap+stars):
            print('*', end="")

        # End the current row of the pattern.
        print()

        gap -= 1
        stars += 2
nStarDiamond(5)
"""

"""
*********
 *******
  *****
   ***
    *
"""
"""
def nStarTriangle(n: int) -> None:
    for i in range(n):
        count = n - i-1
        space = n - count-1
        star = 2*count +1
        print(' ' * space + '*' * star)

nStarTriangle(5)
"""

"""
    *
   ***
  *****
 *******
*********
*********
 *******
  *****
   ***
    *
"""
"""
def nStarDiamond(n: int) -> None:
    for i in range(n):
        space = n - i-1
        star = 2*i+1
        print(' ' * space + '*' * star)
    for i in range(n):
        count = n - i-1
        space = n - count-1
        star = 2*count+1
        print(' ' * space + '*' * star)
nStarDiamond(5)
"""

"""
*
**
***
****
*****
****
***
**
*
"""
"""def nStarTriangle(n: int) -> None:
    for i in range(2*n-1):
        stars= i+1
        if i>n-1:
            stars = 2*n-i-1
        print('*' * stars)

nStarTriangle(5)
"""

"""
1 
0 1 
1 0 1 
0 1 0 1 
1 0 1 0 1 
"""
"""
def nBinaryTriangle(n: int) -> None:
    start = 1
    for i in range(n):
        if i%2 == 0:
            start= 1
        else:
            start= 0
        for j in range(i+1):
            print(start, end=' ')
            start = 1-start
        print()
nBinaryTriangle(5)
"""






















