# Các phép toán
    # Cơ bản: + - * /
    # Chia lấy dư: %
    # Chia lấy nguyên: //   
    # Lũy thừa: **

# Câu điều kiện
    # Câu điều kiện dạng thiếu:
# age = int(input('Hãy nhập tuổi của bạn: '))
# if age >= 18:
#     print('Bạn đã đủ 18 tuổi.')

    # Câu điều kiện dạng đủ
# n = int(input('Nhập 1 số nguyên: '))
# if n%2 == 0:
#     print(n, 'là số chẵn')
# else:
#     print(n, 'là số lẻ')

    # Câu điều kiện dạng đa nhánh
        # [8, 10] - Giỏi
        # [6.5, 8) - Khá
        # [5, 6.5) - Trung Bình
        # [0, 5) - Yếu
score = float(input('Hãy nhập điểm của bạn: '))

        # Cách 1:
# if score >= 8 and score <= 10:
#     print('Xếp loại: Giỏi')
# elif score >= 6.5 and score < 8:
#     print('Xếp loại: Khá')
# elif score >= 5 and score < 6.5:
#     print('Xếp loại: Trung Bình')
# elif score >= 0 and score < 5:
#     print('Xếp loại: Yếu')
# else:
#     print('Bạn đã nhập sai !!!')

        # Cách 2:
# if score < 0 or score > 10:
#     print('Bạn đã nhập sai !!!')
# else:
#     if score >= 8:
#         print('Xếp loại: Giỏi')
#     elif score >= 6.5:
#         print('Xếp loại: Khá')
#     elif score >= 5:
#         print('Xếp loại: Trung Bình')
#     else:
#         print('Xếp loại: Yếu')