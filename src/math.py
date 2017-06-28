import ctypes, os
path = os.getcwd() + "/lib/modular_exponentiation.so"
c = ctypes.CDLL(path)

""" LtoR dichotomic exponentiation
"""
def mod_expo(b,e,m):
    c = 1
    f = 0
    while(f < e):
        f += 1
        c = (b * c) % m
return c

def mod_expo_b(b,e,m)

result = 1
while e > 0:
    if e & 1 > 0:
	result = (result * b) % m
    e >>= 1
    b = (b * b) % m
return result
