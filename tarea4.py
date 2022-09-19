# ecuaciones algebraicas

from random import paretovariate


a = int(input("write you 'a' valor"))
b = int(input("write you 'b' valor"))
c = int(input("write you 'c' valor"))


x = -b + pow( pow(b, 1/2) - a**4 * c, 1/2) / a**2
x2 = b + pow(pow(b, 1/2) - a**4 * c, 1/2) / a**2

print(x)
print(x2)
