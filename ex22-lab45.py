import numpy as np

# Tạo ma trận 100x100 với các số nguyên ngẫu nhiên từ 1 đến 100
# Lưu ý: randint(1, 101) sẽ lấy các giá trị từ 1 đến 100
matrix = np.random.randint(1, 101, size=(100, 100))

# Tạo điều kiện (boolean mask) để tìm các phần tử là bội số của 3 hoặc 5
# Sử dụng toán tử modulo (%) để kiểm tra chia hết và bitwise OR (|) cho điều kiện "hoặc"
condition = (matrix % 3 == 0) | (matrix % 5 == 0)

# Lọc các phần tử thỏa mãn điều kiện và tính tổng
total_sum = np.sum(matrix[condition])

print(f"Tổng các phần tử là bội số của 3 hoặc 5 trong ma trận 100x100 là: {total_sum}")

# Mô phỏng lại ví dụ 3x3 trong hình ảnh để kiểm chứng:
example_matrix = np.array([[15, 2, 9],
                           [8, 5, 3],
                           [4, 4, 7]])
example_condition = (example_matrix % 3 == 0) | (example_matrix % 5 == 0)
example_sum = np.sum(example_matrix[example_condition])
print(f"\nKiểm tra với ma trận ví dụ: Tổng = {example_sum}") # Kết quả sẽ in ra 32