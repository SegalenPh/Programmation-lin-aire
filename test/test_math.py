import timeit
from modular_exponentiation import modexp_lr, modexp_rl


a = 153
b = 99999999
m = 147
setup_vars = "a = %d;b = %d;m = %d" % (a,b,m)

iterations = 100

print "first test"
t1 = timeit.Timer("modexp_lr(a, b, m)",setup_vars+"; from modular_exponentiation import modexp_lr")
print t1.timeit(iterations)

print "second test"
t2 = timeit.Timer("modexp_rl(a, b, m)",setup_vars+"; from modular_exponentiation import modexp_rl")
print t2.timeit(iterations)
