#!/usr/bin/env python3

import math
import numpy as np
import matplotlib.pyplot as plt

import src.graph
from src.engine import Value

a = Value(-4.0)
b = Value(2.0)
c = a + b
d = a * b + b**3
c += c + 1
c += 1 + c + (-a)
d += d * 2 + (b + a).relu()
d += 3 * d + (b - a).relu()
e = c - d
f = e**2
g = f / 2.0
g += 10.0 / f

# print(f'{g.data:.4f}') # prints 24.7041, the outcome of this forward pass

# g.backward()

# print(f'{a.grad:.4f}') # prints 138.8338, i.e. the numerical value of dg/da
# print(f'{b.grad:.4f}') # prints 645.5773, i.e. the numerical value of dg/db


def f(x):
  return 3*x**2 - 4*x + 5

xs = np.arange(-5, 5, 0.25)
ys = f(xs)

#plt.plot(xs, ys)
#plt.show()

h = 0.001
x = 3.0

# df(x) = (f(x + h) - f(x)) / h
# print((f(x+h) - f(x))/h)

a = Value(2.0, label = 'a')
b = Value(-3.0, label = 'b')
c = a*b ; c.label = 'c'
d = Value(10.0, label = 'd')
L = d + c ; L.label = 'L'

L.backward()

src.graph.draw(L).view()
