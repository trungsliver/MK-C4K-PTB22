# # Bài 1: Quy đổi thời gian
#     # Yêu cầu: Nhập thời gian (tính bằng giây)
#     # Trả về thời gian định dạng: giờ - phút - giây
#     # Ví dụ: 3661s = 1h 1m 1s
# time = int(input('Nhập thời gian muốn chuyển đổi: '))
# hour = time // 3600
# minute = (time % 3600) // 60
# second = time % 60
# print(f'{time}s = {hour}h {minute}m {second}s')

# Bài 2: Tính tiền điện
    # Yêu cầu: Nhập số điện (tính bằng kWh)
    # Trả về tiền điện (tính bằng VND)    
    # Bảng giá:
        # 0 - 100 kWh: 1.5k VND/kWh
        # 101 - 250 kWh: 2k VND/kWh
        # 251 - 400 kWh: 2.5k VND/kWh
        # > 400 kWh: 3k VND/kWh
kWh = float(input('Nhập số điện (kWh): '))
money = 0

if kWh < 0:
    print('Bạn đã nhập sai !!!')
elif 0 <= kWh <= 100:
    money = kWh * 1.5
elif 100 < kWh <= 250:
    money = 100*1.5 +(kWh-100)*2
elif 250 < kWh <= 400:
    money = 100*1.5 + 150*2 + (kWh-250)*2.5
else:
    money = 100*1.5 + 150*2 + 150*2.5 + (kWh-400)*3

print(f'Số tiền phải trả là: {money}k VND')
