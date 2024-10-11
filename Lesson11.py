# # Cấu trúc xâu / chuỗi ký tự
# name = "Bao Son"   

# print(len(name))    # Độ dài string
# print(name[0])      # Lấy ký tự đầu tiên
# print(name[-1])     # Lấy ký tự cuối cùng

# # Duyệt xâu ký tự
#     # Cách 1
# for i in range(len(name)):
#     print(name[i], end=' ')
#     # Cách 2
# for s in name:
#     print(s, end=' ')

# Xâu con
str1 = 'BaoSonDepTrai'
str2 = 'BaoSon'
str3 = 'XauTrai'
    # Kiểm tra xâu con: hàm in => True/False
print(str2 in str1)     # Output: True
print(str3 in str1)     # Output: False

    # Tìm vị trí xâu con: hàm find() => index
print(str1.find(str2))          # Output: 0
print(str1.find('DepTrai'))     # Output: 6
print(str1.find(str3))          # Output: -1

# Slicing - cắt chuỗi
    # Cắt từ vị trí ngẫu nhiên trong chuỗi
print(str1[3:9])        # Output: SonDep
    # Cắt đến cuối chuỗi
print(str1[3:])         # Output: SonDepTrai
    # Cắt từ đầu chuỗi
print(str1[:6])         # Output: BaoSon

# Xóa khoảng trắng ở đầu và cuối string - strip()
str4 = '     Sơn cute      '
str5 = str4.strip()
print(str4)
print(str5)

# Thay thế string - replace()
song = 'baby shark doo doo doo doo doo'
    # Thay thế toàn bộ
song2 = song.replace('doo', 'hihi') 
print(song2)
    # Thay thế với số lượng chỉ định
song3 = song.replace('doo', 'haha', 2) 
print(song3)

# Kết hợp chuỗi - join()
arr = ['r','o','n','a','l','d','o']
print(' '.join(arr))

# Tách chuỗi - split()
a = '1 2 3 4 5 6 7 8 9'
arr = a.split()
print(arr)

b = 'a,s,d,f,g,h,j,k,l'
arr2 = b.split(',')  # split theo dấu phẩy
print(arr2)

# Chuyển đổi kiểu dữ liệu trong danh sách
    # Cách 1:
arr2 = []
for item in arr:
    x = int(item)
    arr2.append(x)
print(arr2)
    # Cách 2:
arr3 = [int(item) for item in arr]
print(arr3)

# Tính tổng phần tử danh sách
    # Cách cũ:
tong = 0
for item in arr2:
    tong = tong + item
print(tong)
    # Cách mới
tong2 = sum(item for item in arr2)
print(tong2)

# Tính tổng phần tử chẵn danh sách
    # Cách cũ:
tong = 0
for item in arr2:
    if item % 2 == 0:
        tong = tong + item
print(tong)
    # Cách mới
tong2 = sum(item for item in arr2 if item%2==0)
print(tong2)