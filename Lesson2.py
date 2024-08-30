# Biến số - Phép gán
    # Biến số: dùng để lưu trữ dữ liệu, có thể thay đổi trong khi lập trình
    # Phép gán: dùng để gán giá trị cho biến số: [Tên biến] = [Giá trị]
x = 10
a, b, c = 1, 2, 3
# print(x, a, b, c)

# Data Types - Kiểu dữ liệu
    # String - Chuỗi ký tự / Xâu ký tự
name = 'Duc Trung'
    # Interger - Int: Số nguyên
age = 25
    # Float: Số thực, số có phần thập phân
score = 9.5
    # Boolean: True / False (đúng / sai)
male = True

# Kiểm tra kiểu dữ liệu - type()
print(type(name), type(age), type(score), type(male))

# Xác định kiểu dữ liệu khi nhập
teacher = str(input('Nhập tên giáo viên của bạn: '))
year = int(input('Nhập năm sinh của bạn: '))
weight = float(input('Nhập cân nặng của bạn: '))
female = bool(input('Bạn có phải là nữ không: '))

# ========== Bài tập ==========
# Bài 1: Chuyển đổi từ USD sang VND
    # Nhập USD muốn chuyển (Int)
usd = int(input('Nhập số tiền muốn chuyển đổi: $'))
    # Chuyển đổi: 1 USD = 25000 VND
vnd = usd * 25000
    # Hiển thị số tiền sau khi đổi
print(f'{usd} USD = {vnd} VND')

# Bài 2: Nhập chiều dài, chiều rộng HCN. Tính chu vi, diện tích HCN.
    # Nhập chiều dài, chiều rộng (float)
a = float(input("Nhập chiều dài HCN: ")) 
b = float(input("Nhập chiều rộng HCN: ")) 
    # Tính chu vi, diện tích HCN
cvi = 2 * (a + b)
dtich = a * b
    # Hiển thị chu vi, diện tích HCN
print('Chu vi HCN:', cvi)
print('Diện tích HCN:', dtich)

# Bài 3: Nhập chiều dài 1 cạnh hình vuông. Tính chu vi, diện tích hình vuông.
    # Nhập chiều dài cạnh hình vuônh (float)
a = float(input("Nhập chiều dài cạnh hình vuông: "))  
    # Tính chu vi, diện tích hình vuông
cvi = a * 4
dtich = a * a
    # Hiển thị chu vi, diện tích HCN
print('Chu vi hình vuông:', cvi)
print('Diện tích hình vuông:', dtich)