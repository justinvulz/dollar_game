from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form
from sympy import *
import lib.cube as cube
n =6
mm = cube.ncube_laplacian(n)
m = Matrix(mm)
m = smith_normal_form(m, domain=ZZ)
print(m)
for i in range(2**n):
    print(m[i,i],end=' ')


