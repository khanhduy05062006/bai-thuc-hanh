
class Hinhchunhat:
    def __init__(self, dai, rong):
        self.dai = dai
        self.rong = rong
    def dientich(self):
        return self.dai * self.rong
hcn = Hinhchunhat(8, 5)
print("Diện tích hình chữ nhật là:", hcn.dientich())

