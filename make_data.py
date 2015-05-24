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
m, b = -2.0, 8.0
norm = np.exp(b) * (np.exp(m * mx) - np.exp(m * mn)) / m
x = np.sort(np.random.uniform(mn, mx, np.random.poisson(norm)))
p = np.exp(m * x + b) / norm
x = x[np.random.rand(len(p)) < p]
np.savetxt("poisson.csv", x)
