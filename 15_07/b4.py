a = float (input ("Nhap vao gia tri a: "))
b = float (input ("Nhap vao gia tri b: "))
if a==0:
    if b==0:
        print("Phuong trinh vo so nghiem")
    else:
        print("Phuong trinh vo nghiem")
else:
    x=-b/a;
    print(f"x={x}")