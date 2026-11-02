import numpy as np
import math
#task 1

A = np.random.randint(1,100, size=(10,10))
B = np.random.randint(1,30, size=(2,10))
C = np.random.randint(1,20, size=(10,2))

print("A",A)
print("B",B)
print("C",C)

#a
print('a)', A + A.T + (C @ B) + (B.T @ C.T))

#b
k = np.random.randint(1, 11)
J = np.random.choice(10, k, replace=False)

A_J = A[:, J]
C_J = C[J, :]
M = B @ A_J @ C_J

print('b)', M)

#c
v = A[A % 2 != 0]
v = np.unique(v)
v = v[::-1]

print('c)', v)

#d
def is_prime(n):
    if n <= 1: 
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

A_flat = A.flatten()
d = np.array([x for x in A_flat if is_prime(x)])
n = len(d)
i = np.arange(1, n + 1)
S = np.sum(i * d)

print('d)', S)
