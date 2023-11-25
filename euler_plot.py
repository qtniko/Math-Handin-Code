def euler(x0, y0, x, h, df):
    xn = [x0]
    yn = [y0]
    while xn[-1] < x:
        xn.append(xn[-1] + h)
        yn.append(yn[-1] + h * df(yn[-1]))
    return xn, yn


r = 2
K = 10000
N0 = 100

df = lambda nt: \
    r * nt * (1 - nt/K)

t = 1
h = 0.1

x, y = euler(0, N0, t, h, df)

analytic = lambda t: \
    (N0 * K) / ((K - N0) * np.exp(-r*t) + N0)

import numpy as np
import matplotlib.pyplot as plt

xs = np.linspace(0, 1, 100000)
ys = analytic(xs)

plt.plot(xs, ys, color='red')
plt.plot(x, y, color='blue')
plt.show()
