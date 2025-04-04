# A Test Sheet for GitHub


import sympy
A = sympy.Matrix([[3,2],
                  [4,5]])
print(A)

b = sympy.Matrix([1,1])

aug_matrix = A.row_join(b)
rref, pivot = aug_matrix.rref()
print(rref)
print(pivot)