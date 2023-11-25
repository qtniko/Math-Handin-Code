import numpy as np

# Simpson's Rule
def simpson(f, a, b, n):
    dx = (b - a) / n
    
    x = np.linspace(a, b, n+1)
    fx = f(x)

    integral = dx/3 * (fx[0] + 4*np.sum(fx[1:-1:2]) + 2*np.sum(fx[2:-1:2]) + fx[-1])
    
    return integral



f = lambda x: \
    x * np.exp(3*x)

integral = simpson(f, a=0, b=1, n=1000)

print(integral)
