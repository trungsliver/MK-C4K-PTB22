# Bài 1: Viết một hàm sum_odd(numbers) để tính tổng các số lẻ trong một danh sách numbers.
# 	YC1: Hàm nhận vào một danh sách các số nguyên.
# 	YC2: Hàm trả về tổng các số lẻ trong danh sách đó.
def sum_odd(numbers):
    sum = 0
    for num in numbers:
        if num % 2 != 0:
            sum = sum + num
    return sum
num_list = [1, 2, 3, 4, 5]
print('Tổng số lẻ danh sách =', sum_odd(num_list))

# Bài 2: Viết một hàm is_prime(n) để kiểm tra xem một số nguyên dương n có phải là số nguyên tố hay không.
# 	YC1: Hàm nhận vào một số nguyên dương n.
# 	YC2: Hàm trả về True nếu n là số nguyên tố, ngược lại trả về False.
def is_prime(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count = count + 1
    if count == 2: 
        return True
    else:
        return False
print('Số nguyên tố:', is_prime(12))

# Bài 3: Viết một hàm count_words(s) để đếm số lượng từ trong một chuỗi s.
# 	YC1: Hàm nhận vào một chuỗi ký tự s.
# 	YC2: Hàm trả về số lượng từ trong chuỗi đó.
def count_words(s):
    words = s.strip().split()
    return len(words)
s = "Nguyễn Ngọc Bảo Sơn siêu cấp vippro"
print(f'"{s}" có {count_words(s)} từ')

# Bài 4: Viết một hàm sum_of_digits(n) để tính tổng các chữ số của một số nguyên dương n.
# 	YC1: Hàm nhận vào một số nguyên dương n.
# 	YC2: Hàm trả về tổng các chữ số của n.
def sum_of_digits(n:int):
    sum = 0
    while n > 0:
        sum = sum + n%10
        n = n//10
    return sum
num = 12345
print(f'Tổng các chữ số của {num} là: {sum_of_digits(num)}')

# Bài 5: Viết một hàm find_max(numbers) để tìm vị trí số lớn nhất trong một danh sách numbers.
# 	YC1: Hàm nhận vào một danh sách các số nguyên.
# 	YC2: Hàm trả về vị trí số lớn nhất trong danh sách đó.
def find_max(numbers:list):
    for i in range(len(numbers)):
        if numbers[i] == max(numbers):
            max_index = i
            return max_index
num_list = [1, 2, 3, 4, 5, -5, -10, 9, -2, 8]
print('Vị trí phần tử lớn nhất:', find_max(num_list))

# Bài 6: Viết một hàm sum_to_n(n) để tính tổng các số từ 1 đến n.
# 	YC1: Hàm nhận vào một số nguyên dương n.
# 	Yc2: Hàm trả về tổng các số từ 1 đến n.
def sum_to_n(n):
    sum = 0
    for i in range(0, n+1):
        sum = sum + i
    return sum
num = 10
print(f'Tổng các số nguyên từ 1 đến {num} là: {sum_to_n(num)}')

