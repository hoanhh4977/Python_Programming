tien = int(input("Nhập số tiền: "))

to_500 = tien // 500000
tien = tien % 500000

to_200 = tien // 200000
tien = tien % 200000

to_100 = tien // 100000
tien = tien % 100000

to_50 = tien // 50000
tien = tien % 50000

print("Số tờ 500k:", to_500)
print("Số tờ 200k:", to_200)
print("Số tờ 100k:", to_100)
print("Số tờ 50k:", to_50)
print("Số tiền còn lại không đổi được:", tien)
 