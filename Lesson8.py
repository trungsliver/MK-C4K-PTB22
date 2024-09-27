# Danh sách - Array/List
# CRUD: Create - Read - Update - Delete

# Create - Khởi tạo danh sách
arr = []    # Danh sách rỗng - không có phần tử nào
arr2 = ['Bao Son', 'Quang Huy', 'Khoi Nguyen', 'Thanh Tung']
    # Hàm len() - trả về số lượng phần tử danh sách
print(len(arr))
print(len(arr2))

# Read - Duyệt, hiện phần tử danh sách
    # Hiện phần tử bằng chỉ số index (đếm từ 0)
print(arr2[2])
    # Hiện phần tử cuối cùng (index = -1)
print(arr2[-1])

    # Duyệt và hiện phần tử danh sách
        # Cách 1: dùng cả index và value
for i in range(len(arr2)):
    print(f'[{i}] {arr2[i]}')
        # Cách 2: chỉ dùng value
for item in arr2:
    print(item)
        # Cách 3: dùng hàm có sẵn
for index, item in enumerate(arr2):
    print(f'[{index}] {item}')
        # Cách 4: chỉ dùng để test
print(arr2)

# Update - chỉnh sửa danh sách
    # Thêm phần tử vào cuối danh sách - append(value)
arr2.append('Duc Trung')
    # Thêm phần tử vào vị trí chỉ định - insert(index, value)
arr2.insert(1, 'Imposter')
    # Chỉnh sửa value của phần tử danh sách
arr2[0] = 'Bao Son hihi'

# Delete - Xóa phần tử danh sách
    # Xóa phần tử bằng giá trị - remove(value)
arr2.remove('Duc Trung')
    # Xóa phần tử bằng chỉ số - pop(index)
arr2.pop(1)
    # Xóa toàn bộ phần tử danh sách - clear()
arr2.clear()

# Sắp xếp phần tử - sort()
num_list = [5, 2, 9, 7, 1, 6, 3, 8, 4]
    # Theo thứ tự từ nhỏ đến lớn
num_list.sort()
    # Theo thứ tự từ lớn đến nhỏ
num_list.sort(reverse=True)

# # Tìm phần tử lớn nhất & nhỏ nhất
print('Phần tử lớn nhất:', max(num_list))
print('Phần tử nhỏ nhất:', min(num_list))

# ================= Luyện tập ==================
# Bài 1: Nhập vào 1 số nguyên dương n
# Yêu cầu: Kiểm tra xem n có phải là số nguyên tố hay không
# Biết rằng: số nguyên tố là số chỉ chia hết cho 1 và chính nó
n = int(input('Nhập 1 số nguyên n: '))
count = 0
for i in range(1, n + 1):
    if n % i == 0:
        count = count + 1
if count == 2:
    print(n, 'là số nguyên tố')
else:
    print(n, 'không phải số nguyên tố')

# Bài 2: In ra các số nguyên tố trong khoảng [50, 100] và tính tổng các số đó
sum = 0
for i in range(50,101):
    count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count = count + 1
    if count == 2:
        print(i, end=' ')
        sum = sum + i
print('\n Tổng các số nguyên tố trong khoảng [50,100] là:', sum)