import numpy as np
import pandas as pd


# Strassen Portion
def quarter(A):
    size = len(A)
    half_size = int(size / 2)

    A11 = A[0:half_size, 0:half_size].copy()
    A12 = A[0:half_size, half_size:size].copy()
    A21 = A[half_size:size, 0:half_size].copy()
    A22 = A[half_size:size, half_size:size].copy()

    return A11, A12, A21, A22


def reassemble(A11, A12, A21, A22):
    left_side = np.vstack((A11, A21))
    right_side = np.vstack((A12, A22))

    return np.hstack((left_side, right_side))


def strassen(A, B):
    if len(A) == 128:
        return np.matmul(A, B)
    else:
        A11, A12, A21, A22 = quarter(A)
        B11, B12, B21, B22 = quarter(B)

        M1 = strassen((A11 + A22), (B11 + B22))
        M2 = strassen((A21 + A22), B11)
        M3 = strassen(A11, (B12 - B22))
        M4 = strassen(A22, (B21 - B11))
        M5 = strassen((A11 + A12), B22)
        M6 = strassen((A21 - A11), (B11 + B12))
        M7 = strassen((A12 - A22), (B21 + B22))

        C11 = M1 + M4 - M5 + M7
        C12 = M3 + M5
        C21 = M2 + M4
        C22 = M1 - M2 + M3 + M6

        return reassemble(C11, C12, C21, C22)


part_a = 2**10

X = (1 - (-1)) * np.random.random_sample((part_a, part_a)) - 1
Y = (1 - (-1)) * np.random.random_sample((part_a, part_a)) - 1

# Strassen Result:
strassen_result = strassen(X, Y)
# Regular Result:
regular_result = np.matmul(X, Y)

pd.DataFrame(strassen_result).to_csv('strassen-10.csv')
pd.DataFrame(regular_result).to_csv('default-10.csv')

part_b = 2**12

X = (1 - (-1)) * np.random.random_sample((part_b, part_b)) - 1
Y = (1 - (-1)) * np.random.random_sample((part_b, part_b)) - 1

# Strassen Result:
strassen_result = strassen(X, Y)
# Numpy Result:
regular_result = np.matmul(X, Y)

pd.DataFrame(strassen_result).to_csv('strassen-12.csv')
pd.DataFrame(regular_result).to_csv('default-12.csv')
