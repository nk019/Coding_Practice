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
        try:
            if int(n)%int(n[i])==0:
                counter+=1
        except ZeroDivisionError as e:
            counter += 0

    print(counter)

evenlyDivides(20)
"""

"""
Reverse a 32 bit signed number 
"""
"""
def reverse(x: int) -> int:
    sign = [1, -1][x < 0]
    rev, x = 0, abs(x)
    while x:
        x, mod = divmod(x, 10)
        rev = rev * 10 + mod
        if rev > 2 ** 31 - 1:
            return 0
    return sign * rev

print(reverse(-12305))
"""    ### use of list  samajh nhi aaya
"""
def reverse(self, x):
    s = str(x)
    if "-" in s:
        p = s[-1:0:-1]
        y = int(p)
        x = -y
    else:
        p = s[::-1]
        x = int(p)

    if x > -(2 ** 31) and x < 2 ** 31 - 1:
        return x
    else:
        return 0
        
print(reverse(-123))
"""







