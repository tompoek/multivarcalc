from scipy import optimize
import numpy as np

f = lambda x, y: -np.exp(x - y*y + x*y)
g = lambda x, y: np.cosh(y) + x - 2
dfdx = lambda x, y: (1 + y) * f(x,y)
dfdy = lambda x, y: (-2*y + x) * f(x,y)
dgdx = lambda x, y: 1
dgdy = lambda x, y: np.sinh(y)

def DL(xyl):
	x, y, l = xyl
	return np.array([dfdx(x,y) - l*dgdx(x,y), dfdy(x,y) - l*dgdy(x,y), -g(x,y)])

y0 = 0
x0 = -np.cosh(y0) + 2
l0 = 1
root = optimize.root(DL, [x0, y0, l0])
if root.success:
	x, y, _ = root.x
	print('x = %g' % x)
	print('y = %g' % y)
	print('f(x, y) = %g' % f(x,y))
	print('g(x, y) = %g' % g(x,y))
else:
	print(root.message)
