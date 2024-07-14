import math


class complex_number:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def cong(self, sophuckhac):
        return self.a + sophuckhac.a, self.b + sophuckhac.b

    def tru(self, sophuckhac):
        return self.a - sophuckhac.a, self.b - sophuckhac.b

    def phanthuc(self):
        return self.a

    def phanao(self):
        return self.b

    def dolon(self):
        return math.sqrt(self.a * self.a + self.b * self.b)

    def nhan(self, sophuckhac):
        return complex_number(self.a * sophuckhac.a - self.b * sophuckhac.b, self.a * sophuckhac.b + self.b * sophuckhac.a)

    def chia(self, sophuckhac):
        dolonn = math.pow(sophuckhac.dolon(), 2)
        b1 = complex_number(sophuckhac.phanthuc(), -sophuckhac.phanao())
        a1 = self.nhan(b1)
        return complex_number(a1.a / dolonn, a1.b / dolonn)

    def __str__(self):
        return(f"{self.a}+{self.b}i")

# Sử dụng class số phức
a1=float(input("Phan thuc cua so phuc 1:"))
b1=float(input("Phan ao cua so phuc 1:"))

a2=float(input("Phan thuc cua so phuc 2:"))
b2=float(input("Phan ao cua so phuc 2:"))

c = complex_number(a1, b1)
c1 = complex_number(a2, b2)
print(f"Số phức thu nhat: {c}")
print(f"Số phức thu hai: {c1}")
nhan1 = c.nhan(c1)
print(f"ket qua phep nhan: {nhan1}")
print(f"ket qua phep cong: {c.cong(c1)}")
print(f"ket qua phep tru: {c.tru(c1)}")
print(f"ket qua phep chia: {c.chia(c1)}")
do_lon_a = c.dolon()
print(f"Độ lớn của so phuc thu nhat: {do_lon_a}")
do_lon_a1 = c1.dolon()
print(f"Độ lớn của so phuc thu hai: {do_lon_a1}")



