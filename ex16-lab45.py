import numpy as np

# Tạo ma trận 100x100 với các số nguyên ngẫu nhiên từ 1 đến 9
# Lưu ý: randint(1, 10) sẽ lấy các giá trị từ 1 đến 9
matrix = np.random.randint(1, 10, size=(100, 100))

# Áp dụng các điều kiện thay đổi giá trị bằng np.where
# Cú pháp: np.where(điều_kiện, giá_trị_nếu_đúng, giá_trị_nếu_sai)
output_matrix = np.where(matrix > 5, 1, np.where(matrix < 5, 0, matrix))

# In thử ma trận đầu vào và kết quả (kích thước 3x3 như ví dụ trong hình)
print("Ma trận ban đầu (ví dụ góc 3x3):")
print(matrix[:3, :3])

print("\nMa trận kết quả (ví dụ góc 3x3):")
print(output_matrix[:3, :3])