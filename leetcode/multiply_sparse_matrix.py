import numpy as np
from scipy.sparse import csr_matrix

# @ command allow us to multiply matrix, including sparse matrix
dense_1 = np.random.binomial(n=1, p=0.1, size=(10, 10))
sparse_1 = csr_matrix(dense_1)
dense_2 = np.random.binomial(n=1, p=0.2, size=(10, 10))
sparse_2 = csr_matrix(dense_2)
rand = np.random.random(size=(10, 1))
result = sparse_1 @ sparse_2
print(result.todense()) # if you want to get back the dense matrix for visual
print(sparse_1 @ sparse_2 @ rand) # can also multiply with a column matrix for result

# Example:
# https://machinelearningmastery.com/sparse-matrices-for-machine-learning/
# Dense:
# [[1 0 0 1 0 0]
#  [0 0 2 0 0 1]
#  [0 0 0 2 0 0]]
#
#   Compressed Sparse Row, CSR:
#   (0, 0)	1
#   (0, 3)	1
#   (1, 2)	2
#   (1, 5)	1
#   (2, 3)	2