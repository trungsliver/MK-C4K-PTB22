# Hàm - chương trình con

# Hàm không có giá trị trả về 
def hello():
    print('Hello Bảo Sơn')
    print('Hello Đức Trung')
# Gọi tên hàm khi cần sử dụng
# hello()

# Truyền dữ liệu cho hàm
def hello2(name):
    print(f'Hello {name}')

# hello2('Sơn vipro')
# hello2('Sơn siêu cấp vipro')

# Hàm có giá trị trả về
def dtich_HCN(a, b):
    return a * b

# print('Diện tích HCN:', dtich_HCN(5,3))

# =========== LUYỆN TẬP ===========
# Bài 1: Viết hàm truyền vào 1 số nguyên dương n
# Yêu cầu: Trả về tổng các số chẵn từ 1 đến n
def sum_even(n):
    sum = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            sum = sum + i
    return sum
print('Tổng số chẵn từ 1 đến 10 =', sum_even(10))

# Bài 2: Viết hàm truyền vào 1 số nguyên âm n
# Yêu cầu: Trả về số lượng các số lẻ từ n đến 0
def count_odd(n):
    count = 0
    for i in range(n, 0):
        if i % 2 != 0:
            count = count + 1
    return count
print('Số lượng số lẻ từ -10 đến 0 =', count_odd(-10))

# Bài 3: Viết hàm truyền vào 1 danh sách học sinh và hiển thị toàn bộ các phần tử kèm chỉ số index
arrHS = ['Bảo Sơn', 'Quang Huy', 'Khôi Nguyên', 'Đức Huy']
def show_arr(arr):
    for i in range(len(arr)):
        print(f'Index {i}: {arr[i]}')
show_arr(arrHS)