import numpy as np

def create_odd_magic_square(n):
    # Khởi tạo ma trận n x n với các giá trị 0
    magic_square = np.zeros((n, n), dtype=int)
    
    # Vị trí bắt đầu: hàng trên cùng, cột ở giữa
    i = 0
    j = n // 2
    
    # Điền các số từ 1 đến n^2
    for num in range(1, n**2 + 1):
        magic_square[i, j] = num
        # Di chuyển lên trên và sang phải
        next_i = (i - 1) % n
        next_j = (j + 1) % n
        # Nếu ô tiếp theo đã được điền, di chuyển xuống dưới ô hiện tại
        if magic_square[next_i, next_j] != 0:
            i = (i + 1) % n
        else:
            i, j = next_i, next_j
            
    return magic_square
# Tạo ma trận Magic Square 15x15
n = 15
matrix_15x15 = create_odd_magic_square(n)

# Tính Hằng số ma thuật (Magic Constant) để kiểm tra
magic_constant = n * (n**2 + 1) // 2

print(f"Ma trận Magic Square {n}x{n} đã được tạo thành công.")
print(f"Hằng số ma thuật (tổng mỗi hàng/cột/đường chéo) là: {magic_constant}")
print("\nKiểm tra chéo kết quả:")
print(f"Tổng hàng 0: {np.sum(matrix_15x15[0, :])}")
print(f"Tổng cột 0: {np.sum(matrix_15x15[:, 0])}")
print(f"Tổng đường chéo chính: {np.trace(matrix_15x15)}")

# In thử góc 5x5 trên cùng bên trái của ma trận để quan sát
print("\nMột phần của ma trận (góc trên bên trái 5x5):")
print(matrix_15x15[:5, :5])