import math

class PhuongTrinhBac2:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def giai_pt(self):
        delta = self.b**2 - 4 * self.a * self.c

        if delta < 0:
            return "Phương trình vô nghiệm"
        elif delta == 0:
            x = -self.b / (2 * self.a)
            return f"Phương trình có nghiệm kép x = {x}"
        else:
            x1 = (-self.b + math.sqrt(delta)) / (2 * self.a)
            x2 = (-self.b - math.sqrt(delta)) / (2 * self.a)
            return f"Phương trình có hai nghiệm phân biệt: x1 = {x1}, x2 = {x2}"

# Sử dụng class
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

phuong_trinh = PhuongTrinhBac2(a, b, c)
ket_qua = phuong_trinh.giai_pt()

print(ket_qua)
