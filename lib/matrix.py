import numpy as np




def smith_normal_form(matrix):
    A = np.array(matrix, dtype=int)
    m, n = A.shape
    
    def swap_rows(i, j):
        A[[i, j]] = A[[j, i]]
    
    def swap_columns(i, j):
        A[:, [i, j]] = A[:, [j, i]]

    def row_addition(i, j, k):
        A[i] += k * A[j]

    def column_addition(i, j, k):
        A[:, i] += k * A[:, j]
    
    def flip_column_sign(i):
        A[:, i] *= -1
    
    def flip_row_sign(i):
        A[i] *= -1

    for t in range(m):
        
        # Find the first non-zero element in the t-th row
        for i in range(t,n):
            if A[t][i] != 0:
                break
        
    return A



