import numpy as np

# Khởi tạo ma trận 100x100 với toàn bộ các phần tử có giá trị là 1
matrix = np.ones((100, 100), dtype=int)

# Gán giá trị 0 cho toàn bộ các phần tử bên trong (trừ đường viền)
matrix[1:-1, 1:-1] = 0

# In thử góc 5x5 trên cùng bên trái của ma trận để quan sát kết quả
print("Góc 5x5 trên cùng bên trái của ma trận kết quả:")
print(matrix[:5, :5])