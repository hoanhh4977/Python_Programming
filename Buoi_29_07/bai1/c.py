def tinhTongnghichDao(n):
    tongNghichDao = 0
    for i in range(1, n+1):
        tongNghichDao = 1/i + tongNghichDao
    return tongNghichDao
print(tinhTongnghichDao(2))