from math import sqrt
def primeList(n):
    plist = [2]
    num = [True]*n
    num[0] = False
    num[1] = False
    num[2] = True
    even = 4
    while even < n:
        num[even] = False
        even += 2
    i = 3
    while i < sqrt(n):
        if num[i] == True:
            f = i
            while f*i < n:
                num[f*i] = False
                f += 2
        i += 2

    i =  3
    while i < (len(num)):
        if num[i]:
            plist.append(i)
        i += 2
    return plist


plist = primeList(4000)
print(plist)
"""def factor(n):
    factor = []
    if n % 2 == 0:
        factor.append(2)
        while n % 2 == 0:
            n /= 2

    if n % 3 == 0:
        factor.append(3)
        ind = 0
        while n % 3 == 0:
            n /= 3

    k = 1
    while (6*k - 1) ** 2 <= n:
        p = 6*k -1
        if n % p == 0:
            factor.append(p)

            while n % p == 0:
                n /= p

        q = p+2
        if n % q == 0:
            factor.append(q)

            while n % q == 0:
                n /= q

        k += 1

    else:
        if n != 1:
            factor.append(n)
    return factor """


def pfactor(n):
    factor = []
    s = sqrt(n)
    for i in plist:
        if i <= s:
            if n % i == 0:
                factor.append(i)
                while n % i == 0:
                    n /= i
        elif n != 1:
            factor.append(n)
            break
    return factor



def quotient(n):
    fac = pfactor(n)
    temp = 1
    for i in range(0, len(fac)):
        temp *= (1 - (1 / fac[i]))
    return round(temp * n)


def isPermutation(x,y):
    x = list(str(x))
    x.sort()
    y = list(str(y))
    y.sort()
    return x == y


"""n = 87109

print('quotient for %i is %i' % (int(n), quotient(n)))
print(n)
print(int(quotient(n)))"""

print('stop')
temp = 100
n = 0
for i in range(2, 10**7):

    q = quotient(i)
    if isPermutation(i, q):
        print(i, q)
        d = i/q
        print(d)
        if d < temp:
            temp = d
            n = i

print("min is %f, n is %d" %(temp,n))
