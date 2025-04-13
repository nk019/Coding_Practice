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

###############              *****    basic math    *****             ##########
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

"""
check if string is palindrome
"""
"""
def isPalindrome(x):
    x = str(x)
    a = x[-1::-1]
    if a == x:
        return True
    else:
        return False
        

print(isPalindrome(121))
"""

"""
lcm and gcd of two numbers 
euclidian method:
gcd(a,b) = subtract two nums from each other until one of them is = 0 , the other one in gcd   
Lcm(a,b)= (a times b) divide by gcd(a,b)
"""
"""
def lcmAndGcd( a: int, b: int):
    gcd = 0
    lcm = 0
    A= a
    B = b
    while a>0 and b>0:
        if a>b:
            a= a%b
        else:
            b= b%a
    if a == 0:
        gcd = b
    else :
        gcd= a
    lcm = abs(A*B)//gcd
    l= [lcm,gcd]
    return l

print(lcmAndGcd(5, 10))
"""

"""
check if the number is armstrong number.
armstrong number is a number which is equal to sum of all digits raised to the 
total number of digits eg-number of digits: 3, 153 = 13+53+33
"""
"""
def armstrongNum(n):
    num = str(n)
    j=[]
    arm_num = 0
    while n>0:
        j.append(n%10)
        n=n//10
    k=j[::-1]
    for i in range(len(k)):
        arm_num += k[i]**len(num)
    if arm_num == int(num):
        return True
    else:
        return False

print(armstrongNum(9474))
"""
"""
def armstrongNum(n):
    digits = [int(d) for d in str(n)]
    power = len(digits)
    arm_num = sum(d ** power for d in digits)
    return arm_num == n

print(armstrongNum(9474))
print(armstrongNum(774))
print(armstrongNum(153))
"""  #more sophisticated version of code. this is more tightly packed and COOL.

'''
sum of 1 to n divisors  
eg:     Input: n = 4     Output: 15
Explanation:  F(1) = 1,   F(2) = 1 + 2 = 3,   F(3) = 1 + 3 = 4,   F(4) = 1 + 2 + 4 = 7
So, F(1) + F(2) + F(3) + F(4)
    = 1 + 3 + 4 + 7 = 15
'''
'''
import math
def Divisors(m):
    divisors = []
    for n in range(1, m+1):
        sqrt = math.sqrt(n)
        for i in range(1, int(sqrt+1)):
            if n%i == 0:
                divisors.append(i)
                if i!= n//i:
                    divisors.append(n//i)
    S = sum(divisors)
    return S

print(Divisors(5))
'''
'''
def sumOfDivisors(n):
    sum = 0
    # Iterating from 1 to N.
    for i in range(1, n + 1):
        # Calculating and accumulating the sum of divisors.
        sum += (n // i) * i
    # Returning the sum of divisors.
    return sum
'''

'''
check if the number is prime
'''
'''
import math
def isPrime(n):
    factors = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            factors += 1
            if i != n//i:
                factors += 1
    if factors == 2:
        return True
    else:
        return False
print(isPrime(59))
'''

########################       ****       basic recursion      *****           #####################

""" 
print up to n number using recursion
"""
"""
def printNos(n):
    if n<=0:
        return
    printNos(n-1)
    print(n, end=' ')
       
printNos(10)
"""   # print nos in a single line
"""
def printNos(initial, last):
        if(initial<=last):
            print(initial)
            printNos(initial+1,last)

printNos(1, 10)
"""   # print each no in new line

'''
print a name   n number of time 
'''
'''
def printGfg(n):
    if n <= 0:
        return
    printGfg(n - 1)
    print("GFG", end=" ")
printGfg(5)
'''

'''
print from N to 1 no.
'''
'''
def printNos( n):
    if n <= 0:
        return
    print(n, end=' ')
    printNos(n - 1)
printNos(10)
'''

'''
Given an integer n, calculate the sum of series 13 + 23 + 33 + 43 + … till n-th term.
'''
'''
def sumOfSeries(n):
    sum = ((n**2)*(n+1)**2)/4
    return sum

print(sumOfSeries(5))
'''    # mathematical
'''
def sumOfSeries(n):
    if n==1:
        return 1
    return n**3 + sumOfSeries(n-1)
print(sumOfSeries(5))
'''    # recursion

'''
A number n is called a factorial number if it is the factorial of a positive integer.
For example, the first few factorial numbers are 1, 2, 6, 24, 120,
Given a number n, the task is to return the list/vector of the factorial numbers smaller than or equal to n.
'''
# at fist position-> 1*1 =>    1      at second-> 1*2 =>    2      at third -> 2*3 =>    6       at fourth 6*4 =>24 and so on
#                 res*i => new res         new res*i    new res         new res*i    new res
# where position is i and previous result is res
'''
def factorialNumbers(n):
    # code here
    factorials = []
    number = 1
    i = 1
    while number <= n:
        factorials.append(number)
        i += 1
        number *= i
    return factorials
print(factorialNumbers(50))
'''

'''
reverse an array     "inplace" i.e. no extra space should be taken
'''
'''
def reverse(arr):
    left, right = 0, len(arr)-1
    while left < right:
        arr[left], arr[right]= arr[right], arr[left]
        left += 1
        right -= 1
    return arr
print(reverse([1,4,3,2,6,5]))
'''

'''
valid panlindrome
'''
'''
def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    s = ''.join(i.lower() for i in s if i.isalnum())  # isalnum removes all non alphanumeric characters
    newS = s[::-1]
    if s == newS:
        return True
    else:
        return False
print(isPalindrome("A man, a plan, a canal: Panama"))
'''

'''
fibonacci series
'''
'''
def fib(n):
    """
    :type n: int
    :rtype: int
    """
    if n == 0: return 0
    if n == 1: return 1
    return fib(n - 1) + fib(n - 2)
print(fib(10))
'''    # with recursion
'''
def fib(n):
    """
    :type n: int
    :rtype: int
    """
    if n < 2: return n
    prev1 = 1
    prev2 = 1
    current = prev1
    for _ in range(2, n):
        current = prev1 + prev2
        prev1 = prev2
        prev2 = current
    return current
print(fib(10))
'''  # without recursion

####################         *****    HASHING   *****     ###################################
'''
count the frequency of each digit in an arry   ---> inplace 
'''

def frequencyCount(arr):
    hash = [0] * len(arr)
    for i in arr:
        if 1 <= i <= len(arr):
            hash[i - 1] += 1
    return hash

print(frequencyCount([1,2,3,3,3,6,4]))












