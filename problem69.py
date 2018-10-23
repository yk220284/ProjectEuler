



def pfactor(n):
    factor = []
    index = []
    if n % 2 == 0:
        factor.append(2)
        ind = 0
        while n % 2 == 0:
            n /= 2
            ind += 1
        index.append(ind)
    if n % 3 == 0:
        factor.append(3)
        ind = 0
        while n % 3 == 0:
            n /= 3
            ind += 1
        index.append(ind)

    k = 1
    while (6*k - 1) ** 2 <= n:
        p = 6*k -1
        if n % p == 0:
            factor.append(p)
            ind = 0
            while n % p == 0:
                n /= p
                ind += 1
            index.append(ind)
        q = p+2
        if n % q == 0:
            factor.append(q)
            ind = 0
            while n % q == 0:
                n /= q
                ind += 1
            index.append(ind)
        k += 1

    else:
        if n != 1:
            factor.append(n)
            index.append(1)

    return factor, index





def quotient(n):
    fac = factor(n)
    temp = 1
    for i in range(0,len(fac)):
        temp *= (1-(1/fac[i]))
    return int(temp*n)

'''temp = 0
n = 0
for i in range(400000,1000000):
    val = i/quotient(i)
    temp = max(temp, val)
    if  temp == val:
        n = i'''



def quotient2(n):
    factor, index = pfactor(n)
    temp = 1
    for i in range(0,len(factor)):
        temp *= (factor[i]/(factor[i]-1))
        #print(temp)
    return temp

'''for i in range(2,1000000):
    val = quotient2(i)
    temp = max(temp, val)
    if  temp == val:
        n = i

print(temp,n)'''

def factor(n):
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


    return factor