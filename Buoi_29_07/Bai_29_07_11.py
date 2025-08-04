# Hàm tính tổng
def Tongab(a, b):
    return (a+b)

def Tongab1(a, b):
    print(f"{a}+{b}={a+b}")

def SN(n):
    s=0
    for i in range(1, n+1):
        s=s+1
    return s

# Tính n!
def GT(n):
    p=1
    if n==0 or n==1:
        return 1
    for i in range(2, n+1):
        p=p*i
    return p

def CKN(k, n):
    return GT(n)/(GT(k)*GT(n-k))

def SN1(n):
    s=0
    for i in range(1, n+1):
        s=s+SN(i)/GT(i)
    return s

def TongA(a):
    s=0
    for i in range(0, len(a)):
        s=s+a[i]
    return s

def TongA2(a):
    s=0
    for x in a:
        s=s+x
    return s
