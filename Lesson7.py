# # Vòng lặp vô hạn - vòng lặp while
# # Đề bài: Hiện ra màn hình số nguyên từ 1 đến 10
#     # Vòng lặp for
# for i in range(1,11):
#     print(i, end=' ')
#     # Vòng lặp while
# i = 1
# while i <= 10:
#     print(i, end=' ')
#     i = i + 1

# # Đề bài 1: Nhập số nguyên n trong khoảng (0,100)
# # nếu nhập sai (n<0 hoặc n>100) thì yêu cầu nhập lại
# n = int(input('Nhập 1 số nguyên trong khoảng [0,100]: '))
# while n < 0 or n > 100:
#     print('Bạn đã nhập sai, vui lòng nhập lại!')
#     n = int(input('\nNhập 1 số nguyên trong khoảng [0,100]: '))
# print('Nhập dữ liệu thành công')

# Đề bài 2: Tạo Mysterious Game
    # Yêu cầu: tạo ra 1 số đặc biệt để đoán (random)
    #  Người chơi cần nhập đến khi nào đoán đúng số đặc biệt thì dừng game
# import random
# number = random.randint(1,100)
# print('Số đặc biệt:', number)
# count = 1
# n = int(input('Nhập dự đoán của bạn: '))
# while n != number:
#     if n < number:
#         print(n, 'nhỏ hơn số cần tìm')
#     else:
#         print(n, 'lớn hơn số cần tìm')
#     n = int(input('\nNhập dự đoán của bạn: '))
#     count = count + 1
# print(f'Dự đoán thành công sau {count} lần đoán!')

# Đề bài 3: Nhập vào số nguyên dương n
# Tính tổng tất cả các chữ số của n
n = int(input('Nhập số nguyên dương n: '))
sum = 0

while n > 0:
    sum = sum + n%10
    n = n // 10
print('Tổng các chữ số của n là:', sum)