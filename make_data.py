#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, print_function

import numpy as np
np.random.seed(1234)

m, b = 0.5, 3.0
mn, mx = 0., 5.

# Generate the dataset for the line fit.
x = np.sort(np.random.uniform(mn, mx, 50))
y = m * x + b
yerr = np.random.uniform(0.1, 0.15, len(x))
y += yerr * np.random.randn(len(yerr))
np.savetxt("linear.csv", np.vstack((x, y, yerr)).T, delimiter=",",
           header="x,y,z")


# Generate Poisson dataset.
alpha, beta = 500.0, -2.0
mn, mx = 1., 5.
bins = np.linspace(mn, mx, 20)
samps = []
for i in range(len(bins) - 1):
    k = alpha * (0.5*(bins[i+1] + bins[i])) ** beta * (bins[i+1] - bins[i])
    samps.append(np.random.uniform(bins[i], bins[i+1], np.random.poisson(k)))
x = np.sort(np.concatenate(samps))
print(len(x))
np.savetxt("poisson.csv", x)
