import math
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0.2,0.401,0.01)

def numerical_diff(f,h):
    f = str(f)
    h = float(h)
    def func(x):
        x_h = x+h
        fx = eval(f,{'x':x, 'np':np})
        fxh = eval(f,{'x':x_h, 'np':np})
        deriv = (fxh - fx)/h
        print(deriv)
        return deriv
    return func(x)

f1 = numerical_diff('np.log(x)',1E-1)
f2 = numerical_diff('np.log(x)',1E-7)
f3 = numerical_diff('np.log(x)',1E-15)
f4 = 1/x

plt.plot(x, f1, label="1E-1", color='b', linestyle='-.', linewidth=2.25, marker='<')
plt.plot(x, f2, label="1E-7", color='k', linestyle='-', linewidth=3.25, marker='o')
plt.plot(x, f3, label="1E-15",color='r', linewidth=2.25, marker='D')
plt.plot(x, f4, label="Analytical Derivative", linestyle='--', color='y',linewidth=2.25, marker='.')
plt.legend()

print("Answer to Q-a: Stepsize h = 1E-7 most closely approximates the true derivative. For values of h that are too large, the approximation becomes inaccurate very quickly as the value of the function changes too much between steps. For values of h that are too small, there seem to be floating point rounding errors which is reflected by the jagged nature of the line in the graph.")
print("Answer to Q-b: By keeping track of the derivative at each elementary operation of the function, automatic differentiation allows you to get much closer to the analytical derivative than the limit form would due to computational restrictions such as floating point rounding errors.")

plt.show()

