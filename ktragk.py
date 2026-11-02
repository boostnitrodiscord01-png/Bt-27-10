import numpy as np

#task 1

A = np.random.randint(1,100, size=(10,10))
B = np.random.randint(1,30, size=(2,10))
C = np.random.randint(1,20, size=(10,2))

print("A",A)
print("B",B)
print("C",C)

#a
a = A + A.T + (C @ B) + (B.T @ C.T)

#b
k = np.random.randint(1, 11)
J = np.random.choice(10, k, replace=False)

A_J = A[:, J]
C_J = C[J, :]
M = B @ A_J @ C_J