def derivative(f, x, h=1e-10):
    """An approximation of `f'(x)`"""
    return (f(x + h) - f(x)) / h

def newtonsMethod(f, x, n):
    """(*attempt to) Find a (single) root of `f` (x : f(x) = 0)"""
    for _ in range(n):
        x -= f(x) / derivative(f, x)
    return x


if __name__ == '__main__':
    M_1 = 1.9891e30   # Sun mass [kg]
    M_2 = 5.9736e24   # Earth mass [kg]
    R = 149597870.7   # Distance (Earth, Sun) ~1AU [km]

    µ = M_2 / (M_1 + M_2)

    f = lambda x: \
        x**5 + (µ - 3)*x**4 + (3 - 2*µ)*x**3 - (µ)*x**2 + (2*µ)*x - µ

    x0 = 0
    n = 100
    
    x = newtonsMethod(f, x0, n)
    print(f'Root of quintic: {x}')
    print(f'Distance to L_1 from Earth: {x * R} km')
