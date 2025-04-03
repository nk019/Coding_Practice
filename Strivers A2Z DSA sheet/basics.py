"""
def reverseTable(n:int) -> None:
    m=10
    while m>0:
        print(n*m, end=' ')
        m -=1
reverseTable(2)
"""   #code
"""
20 18 16 14 12 10 8 6 4 2 
"""   #output

###############................basic.....math.##########
"""
Input: n = 2446
Output: 1
Explanation: Here among 2, 4, 6 only 2 divides 2446 evenly while 4 and 6 do not.
"""
"""
def evenlyDivides(n):
    counter  = 0
    n =str(n)
    for i in range(len(n)):
        if int(n)%int(n[i])==0:
            counter+=1
    print(counter)

evenlyDivides(23)
"""












