# Hiển thị / In ra màn hình
print('Hello world')

# Variables - Biến số
    # Dùng để lưu trữ dữ liệu
    # Có thể thay đổi được trong khi lập trình

# Data Types - Kiểu dữ liệu
    # String - Chuỗi ký tự / Xâu ký tự
name = 'Duc Trung'
    # Interger - Số nguyên
age = 25
    # Float - Số thực (số có phần thập phân)
score = 8.5
    # Bool / Boolean - Logic (True/False) - Đúng/Sai
male = True

# Các cách hiển thị ra màn hình
    # Cách 1: Dùng dấu cộng (ghép chuỗi, áp dụng khi data type = string)
print('Name: ' + name)
    # Cách 2: Dùng dấu phẩy
print("Age:", age)
    # Cách 3: Dùng f (truyền dữ liệu vào string thông qua ngoặc nhọn {})
print(f'Họ tên: {name}. Tuổi: {age}. Điểm: {score}.')
    # Cách 4: In trên nhiều dòng
print('''
Tôi
là 
Trung''')

# Nhập dữ liệu từ bàn phím
game = input('Nhập game mà bạn muốn chơi: ')
print('Game bạn muốn chơi là:', game)

# Các phép toán cơ bản: + - * /
print(1+1)
print(5-2)
print(3*4)
print(10/5)