import numpy as np

# Tạo ma trận 100x100 với các số nguyên ngẫu nhiên từ 1 đến 1000
# Lưu ý: randint(1, 1001) sẽ tạo các giá trị bao gồm cả 1 và 1000
matrix = np.random.randint(1, 1001, size=(100, 100))

# Chuyển ma trận 2 chiều thành mảng 1 chiều (flatten)
flattened_matrix = matrix.flatten()

# Sắp xếp mảng 1 chiều theo thứ tự tăng dần
sorted_array = np.sort(flattened_matrix)

# Lấy 5 phần tử đầu tiên (nhỏ nhất)
five_smallest = sorted_array[:5]

print("5 phần tử nhỏ nhất trong ma trận 100x100 là:", five_smallest)

# Mô phỏng lại ví dụ trong hình ảnh để kiểm chứng:
example_matrix = np.array([[15, 2, 9],
                           [8, 5, 3],
                           [4, 4, 7]])
example_result = np.sort(example_matrix.flatten())[:5]
print("\nKiểm tra với ma trận ví dụ, kết quả là:", example_result.tolist())