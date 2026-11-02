import numpy as np
import math
#task 1

A = np.random.randint(1,101, size=(10,10))
B = np.random.randint(1,31, size=(2,10))
C = np.random.randint(1,21, size=(10,2))

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

print('b)', k)
print(J)
print(M)
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

print('d)', d)
print(S)

#e
def kqua_e(A):
    prime_counts = []
    for row in A:
        count = sum(1 for x in row if songuyento(x))
        prime_counts.append(count)
    
    max_primes = max(prime_counts)
    
    for i, count in enumerate(prime_counts):
        if count == max_primes:
            print(f"row {i + 1}: {A[i]},  {count}")
print('e)')
kqua_e(A)

#f
print('f)')
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
    print(f"row {idx + 1}: {A[idx]}, {run_lengths[idx]}.")
