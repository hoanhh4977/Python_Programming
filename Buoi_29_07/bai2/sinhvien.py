# viết 1 hàm nhập danh sách sinh viên
# viết 1 hàm  xuất danh sách sinh viên
# viết 1 tìm điểm môn python lớn nhất
# viết 1 hàm xuất thông tin mà sinh viên có điểm lớn nhất
# gọi ra bên main
 
#         self.ma_sv = ma_sv
#         self.ten_sv = ten_sv
#         self.sdt = sdt
#         self.diempy_thon = diempy_thon

class SinhVien:
    def __init__(self, ma_sv, ten_sv, sdt, diempy_thon):
        self.ma_sv = ma_sv
        self.ten_sv = ten_sv
        self.sdt = sdt
        self.diempy_thon = diempy_thon
        
    def hien_thi_thong_tin(self):
        print("Mã SV:", self.ma_sv)
        print("Tên SV:", self.ten_sv)
        print("SĐT:", self.sdt)
        print("Điểm:", self.diempy_thon)
        
def nhap(n: int = 5) -> list[SinhVien]:
    ds = []
    for i in range(n):
        sv = SinhVien(
            ma_sv=input("Nhap ma sinh vien: "),
            ten_sv=input("Nhap ten sinh vien: "),
            sdt=input("Nhap so dien thoai: "),
            diempy_thon=float(input("Nhap diem python: "))
        )
        ds.append(sv)
    
def xuat(ds: list[SinhVien]):
    for sv in ds:
        sv.hien_thi_thong_tin()

def timDiemLonNhat(ds: list[SinhVien]):
    max = 0
    viTri = -1
    for idx, sv in enumerate(ds):
        if sv.diempy_thon > max:
            viTri = idx
            max = sv.diempy_thon
    
    return ds[viTri]

def xuatSinhVienDiemCaoNhat(ds: list[SinhVien]):
    sv = timDiemLonNhat(ds)
    

