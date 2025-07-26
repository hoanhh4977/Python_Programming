lst = [0,1]

#2.Tích các vị trí của list 
product = 1
for i in range(len(a)):
    product *= i
print("Tích các vị trí:", product)

#3. Tìm phần tử nhỏ nhất của list

min_val = lst[0]
for num in lst:
    if num < min_val:
        min_val = num
print("Phần tử nhỏ nhất:", min_val)

#4. Tìm giá trị chẵn nhỏ nhất
min_even = None
for num in lst:
    if num % 2 == 0:
        if min_even is None or num < min_even:
            min_even = num
print("Giá trị chẵn nhỏ nhất:", min_even)


