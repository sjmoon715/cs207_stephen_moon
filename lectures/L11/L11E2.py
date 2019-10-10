# Defining variables
a = 3
r = 4
x = [a,1]

f = [0.0,0.0]
# Evaluating function
f[0] = x[0]**r
# Evaluating derivative
f[1] = r*x[0]**(r-1)*x[0]
print (f)