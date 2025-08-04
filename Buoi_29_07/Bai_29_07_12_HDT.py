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
