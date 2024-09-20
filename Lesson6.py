# Vòng lặp hữu hạn - biết trước số lần lặp - vòng lặp for

# Hàm range(start, end, step):
    # start: số bắt đầu (không bắt buộc, mặc định = 0)
    # end: số kết thúc (bắt buộc)
    # step: số bước nhảy (không bắt buộc, mặc định = 1)  
# for i in range(1,10,3):
#     print(i, end = ' ')  

# Hàm range(start, end):
# for i in range(5,12):       # range(5,12,1)
#     print(i, end = ' ') 

# Hàm range(end):
# for i in range(10):         # range(0,10,1)
#     print(i, end = ' ') 

# ============== LUYỆN TẬP ==============
#  Đề bài 1: Nhập 2 số nguyên a và b từ bàn phím. 
#  In ra tất cả các số trong khoảng từ a đến b (tính cả a và b) hoặc ngược lại.
# a = int(input("Nhập số a: "))
# b = int(input("Nhập số b: "))
# if a <= b:
#     for i in range(a, b + 1):
#         print(i, end = ' ')
# else:
#     for i in range(b, a + 1):
#         print(i, end = ' ')

#  Đề bài 2: Nhập 2 số nguyên a và b từ bàn phím. 
#  Yêu cầu: Tính tổng tất cả các số chẵn trong khoảng từ a đến b (tính cả a và b) hoặc ngược lại.
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
sum = 0
if a <= b:
    for i in range(a, b + 1):
        if i%2 == 0:
            sum = sum + i
else:
    for i in range(b, a + 1):
        if i%2 == 0:
            sum = sum + i
print('Tổng các số chẵn là:', sum)

#  Đề bài 3: Nhập 2 số nguyên a và b từ bàn phím. 
#  Yêu cầu: Đếm số lượng số lẻ trong khoảng từ a đến b (tính cả a và b) hoặc ngược lại.
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
count = 0
if a <= b:
    for i in range(a, b + 1):
        if i%2 != 0:
            count = count + 1
else:
    for i in range(b, a + 1):
        if i%2 != 0:
            count = count + 1
print('Số lượng số lẻ là:', count)

# Bài tập 4: In ra bảng cửu chương 1 - 9
for i in range(1,10):
    print('\nBảng cửu chương', i)
    for j in range(1,11):
        print(f'{i} x {j} = {i*j}')
        