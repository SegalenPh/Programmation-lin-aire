import timeit
from modular_exponentiation import modexp_lr, modexp_rl


a = 153
b = 99999999
m = 147
setup_vars = "a = %d;b = %d;m = %d" % (a,b,m)

iterations = 100

print "first test -  LtoR"
t1 = timeit.Timer("modexp_lr(a, b, m)",setup_vars+"; from modular_exponentiation import modexp_lr")
print t1.repeat(repeat=5,number=100000)

print "second test -  RtoL"
t2 = timeit.Timer("modexp_rl(a, b, m)",setup_vars+"; from modular_exponentiation import modexp_rl")
print t2.repeat(repeat=5,number=100000)
