import numpy as np

# Tạo ma trận 100x100 với các số nguyên ngẫu nhiên từ 1 đến 9
# Hàm randint(1, 10) sẽ lấy các giá trị ngẫu nhiên bao gồm 1 và dừng ở 9
matrix = np.random.randint(1, 10, size=(100, 100))

# Sắp xếp từng hàng của ma trận theo thứ tự tăng dần
# Tham số axis=1 chỉ định việc sắp xếp được thực hiện theo từng hàng (row-wise)
sorted_matrix = np.sort(matrix, axis=1)

print("Kích thước ma trận sau khi sắp xếp:", sorted_matrix.shape)

# In thử góc 3x3 trên cùng bên trái của ma trận để quan sát kết quả
print("\nMột phần ma trận ban đầu (góc 3x3):")
print(matrix[:3, :3])

print("\nMột phần ma trận sau khi sắp xếp từng hàng (góc 3x3):")
print(sorted_matrix[:3, :3])