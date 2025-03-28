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

"""
1                 1 
1 2             2 1 
1 2 3         3 2 1 
1 2 3 4     4 3 2 1 
1 2 3 4 5 5 4 3 2 1 
"""
"""
def numberCrown(n: int) -> None:
    space = 2 * (n - 1)
    for i in range(n):
        for j in range(i+1):
            print((j+1), end=' ')
        for j in range(space):
            print(' ', end=' ')
        for j in range(i,-1,-1):
            print((j+1), end=' ')
        print()
        space -= 2
numberCrown(5)
"""

"""
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 
"""
"""
def nNumberTriangle(n: int) -> None:
    num = 1
    for i in range(n):
        for j in range(i+1):
            print(num, end=' ')
            num += 1
        print()
nNumberTriangle(5)
"""

"""
A 
A B 
A B C 
A B C D 
A B C D E 
"""
"""
def nLetterTriangle(n: int) -> None:
    for i in range(n):
        for j in range(i+1):
            print(chr(65+j), end=' ')
        print()

nLetterTriangle(5)
"""
"""             #this code is better than previous code ---> why?????
def nLetterTriangle(n: int):
    num = 1
    for i in range(n):
        currentCharacter = 65
        for j in range(1, num+1):
            print(chr(currentCharacter), end=" ")
            currentCharacter += 1
        num += 1
        print()
nLetterTriangle(5)
"""

"""
A B C D E 
A B C D 
A B C 
A B 
A 
"""
"""
def nLetterTriangle(n: int):
    for i in range(n):
        count= n- i
        for j in range(count):
            print(chr(65+j), end=' ')
        print()

nLetterTriangle(5)
# this code is better than next one ---> why??????
"""
"""
def nLetterTriangle(n: int):
    num = n
    for i in range(n):
        currentCharacter = 65
        for j in range(1, num+1):
            print(chr(currentCharacter), end=" ")
            currentCharacter += 1
        print()
        num -= 1
nLetterTriangle(5)
"""

"""
A
B B
C C C
D D D D
E E E E E
"""
"""
def alphaRamp(n: int) -> None:
    for i in range(n):
        print(" ".join(chr(65+i)*(i+1)))  #" ".join() adds space between word.
alphaRamp(5)
"""

"""
    A
   ABC
  ABCDE
 ABCDEFG
ABCDEFGHI
"""
"""
def alphaHill(n: int):
    for i in range(n):
        for j in range(n- i-1):  
            print(' ', end='')
        for j in range(2*i+1):  # 2*i+1  give odd no series
            print(chr(65+j), end='')
        print()
alphaHill(5)
"""

"""
      A 
    A B A 
  A B C B A 
A B C D C B A
"""
"""
def alphaHill(n: int):
    for i in range(n):
        for j in range(n- i-1):
            print(' ', end=' ')  #this is printing double spaces i.e. 2*(n-i-1) because of end=' '

        breakPoint = (2*i+1)//2
        for k in range(2*i+1):  # 2*i+1  give odd no series
            if k<= breakPoint:
                print(chr(65+k), end=' ')
            else:
                print(chr(65+breakPoint - (k- breakPoint)), end=' ')
        print()
alphaHill(4)

#both the code does same thing but both approch are diffrent

def alphabet_pyramid(n: int) -> None:
    for i in range(n):
        spaces = " " * (2 * (n - i - 1))  # Leading spaces
        left_part = [chr(65 + j) for j in range(i + 1)]  # Increasing sequence
        right_part = left_part[-2::-1]  # Decreasing sequence (excluding last letter)
        print(spaces + " ".join(left_part + right_part))

# Example usage
alphabet_pyramid(4)
"""

"""
E 
D E 
C D E 
B C D E 
A B C D E 
"""
"""
def alphaTriangle(n: int):
    for i in range(n):
        for j in range(i+1):
            print(chr(65+n-1-i+j), end=' ')
        print()

alphaTriangle(5)
"""

"""
E 
E D 
E D C 
E D C B 
E D C B A
"""
"""
def alphaTriangle(n: int):
    for i in range(n):
        for j in range(i+1):
            print(chr(65+n-1-j), end=' ')
        print()

alphaTriangle(5)
"""

"""
* * * * * * 
* *     * * 
*         * 
*         * 
* *     * * 
* * * * * *
"""
"""
def symmetry(n: int):
    lStars = n
    space = 0
    rStars = n
    for i in range(n):
        print('* ' * lStars + '  ' * space + '* ' * rStars)
        lStars -= 1
        space += 2
        rStars -= 1

    lStars = 1
    space = 2*n-2
    rStars = 1
    for i in range(n):
        print('* ' * lStars + '  ' * space + '* ' * rStars)
        lStars += 1
        space -= 2
        rStars += 1
symmetry(3)
"""
"""
def symmetry(n: int):
    space = 0
    for i in range(n):
        for j in range(n-i):
            print('*', end=' ')
        for j in range(space):
            print(' ', end=' ')
        for j in range( n - i):
            print('*', end=' ')
        space += 2
        print()
    space = 2*n-2
    for i in range(n):
        for j in range(i+1):
            print('*', end=' ')
        for j in range(space):
            print(' ', end=' ')
        for j in range(i+1):
            print('*', end=' ')
        space -= 2
        print()

symmetry(3)
"""

"""
*         * 
* *     * * 
* * * * * * 
* *     * * 
*         * 
"""
"""
def symmetry(n: int):
    space = 2*n-2
    for i in range(n):
        for j in range(i+1):
            print('*', end=' ')
        for j in range(space):
            print(' ', end=' ')
        for j in range(i+1):
            print('*', end=' ')
        space -= 2
        print()

    space = 2
    for i in range(n-1):
        for j in range(n-1-i):
            print('*', end=' ')
        for j in range(space):
            print(' ', end=' ')
        for j in range(n-1-i):
            print('*', end=' ')
        space += 2
        print()

symmetry(3)
"""











