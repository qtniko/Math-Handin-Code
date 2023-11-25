def euler(x0, y0, x, h, df):
    xn = x0
    yn = y0
    while xn < x:
        xn += h
        yn += h * df(yn)
    return yn


r = 2
K = 10000
N0 = 100

df = lambda nt: \
    r * nt * (1 - nt/K)

t = 1
h = 0.01

y = euler(0, N0, t, h, df)
print(y)
