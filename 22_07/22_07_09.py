a = [12, 3, 5, 8, 9]
s = 0
for x in a:
    s=s+x
print(s)
max = a[0]
for x in a:
    if x>max:
        max=x
print(f"Max trong List la:{max}")