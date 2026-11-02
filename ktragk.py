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
def songuyento(n):
    if n <= 1: 
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

A_flat = A.flatten()
d = np.array([x for x in A_flat if songuyento(x)])
n = len(d)
i = np.arange(1, n + 1)
S = np.sum(i * d)

print('d)', S)

#e
g = np.vectorize(songuyento)
prime_mask = g(A)
prime_counts_per_row = np.sum(prime_mask, axis=1)
max_primes = np.max(prime_counts_per_row)
kqua_e = np.where(prime_counts_per_row == max_primes)[0]

print('e)', kqua_e)

#f
def longest_odd(row):
    max_run = 0
    current_run = 0
    for num in row:
        if num % 2 != 0:
            current_run += 1
            if current_run > max_run:
                max_run = current_run
        else:
            current_run = 0
    return max_run

run_lengths = np.array([longest_odd(row) for row in A])
max_ovr = np.max(run_lengths)
kqua_f = np.where(run_lengths == max_ovr)[0]
for idx in kqua_f:
    print("f")
    print(f'hang: {idx}')
    print(f'du lieu: {A[idx]}')
