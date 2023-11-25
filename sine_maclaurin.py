from mpmath import mp

def factorial_generator(numtype_ = int):
    value = numtype_(1)
    n = 1
    while True:
        value *= n
        yield value
        n += 1

def calculate_terms(monomials = 50):
    terms = []
    factorial = factorial_generator(float)
    fac = next(factorial)
    for n in range(monomials):
        if n != 0:
            next(factorial)
            fac = next(factorial)
        term = lambda x, n=mp.mpf(n), fac=mp.mpf(fac): \
            ((-1)**n) * x**(2*n+1) / fac
        terms.append(term)
    taylor = lambda x, terms=terms: sum([term(x) for term in terms])
    return taylor


monomials = 50
taylor = calculate_terms(monomials)

x = 0.4
mp.dps = 100  # Precision
y = taylor(mp.fmod(mp.mpf(x), 2*mp.pi))

from math import sin
print(f'Value: {y}\nExact error: {abs(sin(x) - y)}')
