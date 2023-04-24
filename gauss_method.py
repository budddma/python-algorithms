# Метод Гаусса
def gauss(a, n):
    for i in range(n):
        if abs(a[i][i]) < 0.00000000000000000000001:
            k = -1
            for l in range(i+1, n):
                if a[l][i] >= 0.00000000000000000000001:
                    k = l
            if k == -1:
                return False
            a[i], a[k] = a[k], a[i]
        t = a[i][i]
        for j in range(i, n+1):
            a[i][j] /= t
        for l in range(i+1, n):
            coef = a[l][i]
            for j in range(i, n+1):
                a[l][j] -= a[i][j]*coef
    for i in reversed(range(n)):
        for l in range(i):
            a[l][n] -= a[i][n]*a[l][i]
            a[l][i] = 0
    return a

a = []
n = int(input())
for i in range(n):
    a.append([float(s) for s in input().split()])
a = gauss(a, n)
if not a:
    print('BAD MATRIX')
else:
    for i in range(n):
        print(a[i][n], sep=' ')
