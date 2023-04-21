# Метод секущих
def f(x):
    return x**3-2*x
a, b = 1, 2
t = 20
for i in range(t):
    mid = (a*f(b) - b*f(a))/(f(b)-f(a))
    if f(mid) > 0:
        b = mid
    else:
        a = mid
mid = (a*f(b) - b*f(a))/(f(b)-f(a))
print(mid, f(mid))

# Метод касательных
def f(x):
    return x**3-2*x
def der(x):
    return 3*x**2-2
a, b = 1, 2
t = 20
for i in range(t):
    mid = b - f(b)/der(b)
    if f(mid) > 0:
        b = mid
    else:
        a = mid
mid = b - f(b) / der(b)
print(mid, f(mid))

# Путь из одной точки в другую с помощью DFS
def dfs(G, start, finish, way, n, visited):
    visited[start] = True
    if start == finish:
        way.append(start)
        return True
    for i in range(n):
        if adj(G, start, i, n) and not visited[i]:
            if dfs(G, i, finish, way, n, visited):
                way.append(start)
                return True
    return False

def adj(G, v1, v2, n):
    if G[v1*n + v2] == 1:
        return True
    return False

n = int(input())
G = []
way = []
visited = [False]*n
for i in range(n):
    s = [int(h) for h in input().split()]
    for j in range(n):
        G.append(s[j])
start = int(input())
finish = int(input())
dfs(G, start, finish, way, n, visited)
print(way[::-1])

# Существует ли путь из одной точки в другую с помощью BFS
def bfs(G, start, finish, n, visited, line):
    while len(line) > 0:
        x = line.pop(0)
        visited[x] = True
        for i in range(n):
            if adj(G, x, i, n) and not visited[i]:
                if i == finish:
                    return True
                line.append(i)
    return False

def adj(G, v1, v2, n):
    return G[v1*n + v2]

n = int(input())
G = []
visited = [False]*n
for i in range(n):
    s = [int(h) for h in input().split()]
    for j in range(n):
        G.append(s[j])
start = int(input())
finish = int(input())
line = [start]
print(bfs(G, start, finish, n, visited, line))

# Алгоритм Дейкстра
def dijkstra(G, n, S):
    weight = [1000000]*n
    weight[S] = 0
    visited = [False]*n
    for i in range(n):
        min_weight = 1000001
        for j in range(n):
            if weight[j] < min_weight and not visited[j]:
                min_weight = weight[j]
                min_ind = j
        visited[min_ind] = True
        for k in range(n):
            if not visited[k] and weight[k] > G[min_ind][k] + weight[min_ind]:
                weight[k] = G[min_ind][k] + weight[min_ind]
    return weight

n = int(input())
G =[[1000000]*n for i in range(n)]
m = int(input())
for i in range(m):
    a, b, l = [int(s) for s  in input().split()]
    G[a][b] = l
    G[b][a] = l
print(dijkstra(G, n, 0))

# Алгоритм Бэлмана-Форда
def belford(M, n, m, s, f):
    weight = [[1000000]*m for i in range(n)]
    weight[s][0] = 0
    for j in range(1, m):
        for i in range(n):
            weight[i][j] = weight[i][j-1]
            for k in range(n):
                if M[k][i] + weight[k][j-1] < weight[i][j] and M[k][i] != 1000000:
                    weight[i][j] = M[k][i] + weight[k][j-1]
    return weight[f][m-1]

n, m = [int(s) for s in input().split()]
M = [[1000000]*n for i in range(n)]
for i in range(m):
    a, b, l = [int(s) for s in input().split()]
    if M[a-1][b-1] == 1000000:
        M[a-1][b-1] = l
    elif M[a-1][b-1] > l:
        M[a-1][b-1] = l
print(belford(M, n, m, 0, n-1))

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
