"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable

from typing import TypeVar

A = TypeVar('A')

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


# TODO: Implement for Task 0.1.

def mul(x: float, y: float) -> float:
    return x * y


def id(x: A) -> A:
    return x


def add(x: float, y: float) -> float:
    return x + y


def neg(x: float) -> float:
    return -x


def lt(x: float, y: float) -> bool:
    return x < y


def eq(x: float, y: float) -> bool:
    return x == y


def max(x: float, y: float) -> float:
    return math.max(x, y)


def is_close(x: float, y: float) -> bool:
    return math.abs(x - y) < 1e-2


def sigmoid(x: float) -> float:
    return 1 / (1 + math.e ** (-x))


def relu(x: float) -> float:
    return math.max(0, x) 


def log(x: float) -> float:
    return math.log(x)


def exp(x: float) -> float:
    return math.exp(x)


def inv(x: float) -> float:
    if x == 0:
        ValueError("Cannot take reciprocal of zero.")
    return 1 / x


def log_back(x: float, d_out: float) -> float:
    return inv(x) * d_out


def inv_back(x: float, d_out: float) -> float:
    return (-1 / x**2) * d_out


def relu_back(x: float, d_out: float) -> float:
    return d_out if x > 0 else 0


# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists


# TODO: Implement for Task 0.3.
