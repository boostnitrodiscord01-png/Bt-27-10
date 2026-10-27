import numpy as np

# Tạo ma trận 100x100 với các số nguyên ngẫu nhiên từ 1 đến 9
matrix = np.random.randint(1, 10, size=(100, 100))

# Thêm viền số 0 bao quanh ma trận
# pad_width=1 nghĩa là thêm 1 lớp viền ở tất cả các cạnh (trên, dưới, trái, phải)
# constant_values=0 chỉ định giá trị của phần viền được thêm vào là 0
padded_matrix = np.pad(matrix, pad_width=1, mode='constant', constant_values=0)

print(f"Kích thước ma trận sau khi thêm viền: {padded_matrix.shape}") # Sẽ là (102, 102)

print("\nGóc 5x5 trên cùng bên trái của ma trận kết quả:")
print(padded_matrix[:5, :5])    
