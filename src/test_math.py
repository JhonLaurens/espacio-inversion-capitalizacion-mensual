
import math

p0 = 8000000.0
r = 0.012
n = 36

res = p0 * math.pow(1 + r, n)
print(f"Raw calculation: {res}")
print(f"Formatted: {res:,.2f}")
