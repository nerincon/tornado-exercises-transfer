def intToStr(i):
    digits = '0123456789'
    if i == 0:
        return '0'
    res = ''
    while i > 0:
        res = digits[i % 10] + res
        i = i // 10
    return res

# print(intToStr(445))


def genSubsets(L):
    if len(L) == 0:
        return [[]]
    smaller = genSubsets(L[:-1]) # all subsets without last element
    # print('smaller',smaller)

    extra = L[-1:] # create a list of just that last element
    # print('extra',extra)
    new = []
    for small in smaller:
        new.append(small+extra)
        # print('new', new)
    return smaller + new8

print(genSubsets([1,2,3,4]))
# genSubsets([1,2,3,4])


def fib_iter(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib_i = 0
        fib_ii = 1
        for i in range(n-1):
            tmp = fib_i
            fib_i = fib_ii
            fib_ii = tmp + fib_i
            # print(fib_ii)
        return fib_ii

print(fib_iter(20))

def fib_recur(n):
    if n == 0:
        return 0
    elif n ==1:
        return 1
    else:
        return fib_recur(n - 1) + fib_recur(n - 2)

print(fib_recur(6))

def isNum (n):
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    if n in numbers:
        return True
    else:
        return False

print(isNum('y'))

A = 'abc11'

B = '1a12'

C = '12hhgt13a20'

def findSum(mystring):
    temp = ''
    sum = 0
    for x in mystring:
        if isNum(x):
            temp += x
        elif isNum(x) == False and temp == '':
            pass
        else:
            sum += int(temp)
            temp = ''
    print(sum + int(temp))

findSum(A)
findSum(B)
findSum(C)



