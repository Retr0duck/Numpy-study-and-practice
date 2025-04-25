import numpy as np
"""
There are primarily five ways of rounding off decimals in NumPy:

1-truncation
2-fix
3-rounding
4-floor
5-ceil

"""
# 1. Truncation
a = np.array([1.2, 2.5, 3.7, 4.9])
truncated = np.trunc(a)
print("Truncated values:", truncated)

# 2. Fix
b = np.array([3.1599, 2.7182, 1.4142])
fixed = np.fix(b)
print("Fixed values:", fixed)

# 3. Rounding
c = np.array([1.9, 2.9, 3.5])
rounded = np.round(c)
print("Rounded values:", rounded)

# 4. Floor
d = np.array([1.7, 2.3, 3.9])
floored = np.floor(d)
print("Floored values:", floored)

# 5. Ceil
e = np.array([1.7, 2.3, 3.9])
ceiled = np.ceil(e)
print("Ceiled values:", ceiled)