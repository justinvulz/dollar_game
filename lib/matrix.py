import numpy as np


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def gcdext(a, b):
    if b == 0:
        return (a, 1, 0)
    else:
        d, x, y = gcdext(b, a % b)
        return (d, y, x - y * (a // b))


def swap_rows(A, i, j):
    A[[i, j]] = A[[j, i]]


def swap_cols(A, i, j):
    A[:, [i, j]] = A[:, [j, i]]


def add_row(A, i, j, c1: tuple, c2: tuple):
    temp = c1[0]*A[i, :] + c1[1]*A[j, :]
    A[j, :] = c2[0]*A[i, :] + c2[1]*A[j, :]
    A[i, :] = temp


def add_col(A, i, j, c1: tuple, c2: tuple):
    temp = c1[0]*A[:, i] + c1[1]*A[:, j]
    A[:, j] = c2[0]*A[:, i] + c2[1]*A[:, j]
    A[:, i] = temp


def clear_row(A, t,n):
    pivot = A[t, t]
    if pivot == 0:
        return
    for j in range(t+1, n):
        if A[t, j] == 0:
            continue
        d, r = divmod(A[t, j], pivot)
        if r == 0:
            add_col(A, t, j, (1, 0), (-d, 1))
        else:
            g, a, b = gcdext(pivot, A[t, j])
            d_0 = A[t, j]//g
            d_j = pivot//g
            add_col(A, t, j, (a, b), (d_0, -d_j))
            pivot = g


def clear_col(A, t,m):
    pivot = A[t, t]
    if pivot == 0:
        return
    for i in range(t+1, m):
        if A[i, t] == 0:
            continue
        d, r = divmod(A[i, t], pivot)
        if r == 0:
            add_row(A, t, i, (1, 0), (-d, 1))
        else:
            g, a, b = gcdext(pivot, A[i, t])
            d_0 = A[i, t]//g
            d_i = pivot//g
            add_row(A, t, i, (a, b), (d_0, -d_i))
            pivot = g


def invariant_factors(mt: np.ndarray):

    A = np.matrix(mt).astype(object)
    m, n = A.shape
    for t in range(min(m, n)):

        # If the first element is zero, swap rows and columns to make it non-zero
        if A[t, t] == 0:
            non_zero = np.nonzero(A[:t, t:])
            non_zero = (non_zero[0] + t, non_zero[1] + t)
            if non_zero[0].size == 0:
                break
            swap_rows(A, t, non_zero[0][0])
            swap_cols(A, t, non_zero[1][0])

        # Clear the first row and column
        while (any(A[t, i] != 0 for i in range(t+1, n)) or
               any(A[i, t] != 0 for i in range(t+1, m))):
            clear_col(A, t, m)
            clear_row(A, t, n)
    inv = [abs(int(A[i, i])) for i in range(min(m, n))]  # if A[i,i] != 0]
    inv.sort()
    return inv
