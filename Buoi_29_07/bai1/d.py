def tinhGiaiThua(n):
    giaiThua = 1
    for i in range(2, n + 1):
        giaiThua = giaiThua * i
    return giaiThua
print(tinhGiaiThua(1))