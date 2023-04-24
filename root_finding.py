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
