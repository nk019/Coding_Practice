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





