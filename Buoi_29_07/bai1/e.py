def tinhTongGiaiThua(n):
    tongGiaiThua = 0
    for i in range(1, n + 1):
        giaiThua = 1
        for j in range(2, i+1):
            giaiThua = giaiThua * j
        tongGiaiThua = giaiThua + tongGiaiThua
    return tongGiaiThua
print(tinhTongGiaiThua(3))
