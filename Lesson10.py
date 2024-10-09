# ========= LUYỆN TẬP DANH SÁCH =========
# Bài 1: Cho danh sách gồm các số nguyên liên tiếp từ 1 đến 15
arr = []                    # Tạo danh sách rỗng
for i in range(1, 16):      # Duyệt vòng lặp chạy từ 1 đến 15
    arr.append(i)           # Thêm giá trị của i vào cuối danh sách (từ 1 đến 15)
arr1 = [i for i in range(1,16)]     # Cách 2

    # YC1: In ra toàn bộ các phần tử của danh sách (hiện bằng 3 cách)
        # Cách 1: Cách để test 
print(arr)
        # Cách 2: Duyệt danh sách, hiện cả index (chỉ số) và value (giá trị)
for i in range(len(arr)):
    print(f'index = {i}, value = {arr[i]}')
        # Cách 3: Duyệt danh sách, chỉ hiện value - giá trị của mỗi phần tử
for item in arr:
    print(item, end = ' ')

    # YC2: In ra màn hình tổng các số chẵn
sum = 0                             # Khai báo biến sum để lưu tổng giá trị
for item in arr:                    # Cách duyệt số 2: chỉ lấy value
    if item % 2 == 0:               # Kiểm tra phần tử chẵn
        sum = sum + item            # Nếu phần tử chẵn, cộng vào biến sum
print('Tổng các số chẵn:', sum)     # Hiển thị kết quả ra màn hình

    # YC3: In ra màn hình số lượng số lẻ
count = 0                           # Khai báo biến count để lưu số lượng
for item in arr:                    # Cách duyệt số 2: chỉ lấy value
    if item % 2 != 0:               # Kiểm tra phần tử lẻ
        count = count + 1           # Nếu phần tử lẻ, tăng count thêm 1
print('Số lượng số lẻ:', count)     # Hiển thị kết quả ra màn hình

    # YC4: In ra màn hình vị trí và giá trị của phần tử lớn nhất
max_item = max(arr)                 # Lưu giá trị phần tử lớn nhất
for i in range(len(arr)):           # Cách duyệt số 1: lấy cả index, value
    if arr[i] == max_item:          # Kiểm tra phần tử có giá trị bằng max
        max_index = i               # Lưu vị trí của phần tử lớn nhất
print('Giá trị phần tử lớn nhất:', max_item)
print('Vị trí phần tử lớn nhất:', max_index)

    # YC5: In ra màn hình vị trí và giá trị của phần tử nhỏ nhất
min_item = min(arr)                 # Lưu giá trị phần tử nhỏ nhất
for i in range(len(arr)):           # Cách duyệt số 1: lấy cả index, value
    if arr[i] == min_item:          # Kiểm tra phần tử có giá trị bằng min
        min_index = i               # Lưu vị trí của phần tử nhỏ nhất
print('Giá trị phần tử nhỏ nhất:', min_item)
print('Vị trí phần tử nhỏ nhất:', min_index)

    # YC6: Sắp xếp danh sách theo thứ tự giảm dần
arr.sort(reverse=True)
print(arr)

# Bài 2: Ôn tập danh sách (BTVN)
    # YC1: Nhập vào từ bàn phím 1 danh sách bao gồm 10 số nguyên
arr = [10, 2, 6, 8, 12, 9, 25, 17, 3, 21]
    # YC2: Thêm số '-5' vào vị trí thứ 2 (index=2) trong danh sách
    # YC3: Tính tổng các số lẻ trong danh sách
    # YC4: Đếm số lượng số chẵn có trong danh sách
    # YC5: Tìm giá trị phần tử lớn nhất của danh sách
    # YC6: Tìm vị trí phần tử nhỏ nhất của danh sách
    # YC7: Dùng hàm tính giá trị trung bình của các phần tử trong danh sách