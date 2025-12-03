
class IOString:
    def __init__(self):
        self.s = ""   
    def get_String(self):
        self.s = input("Nhập chuỗi: ")
    def print_String(self):
        print("Chuỗi in hoa:", self.s.upper())
if __name__ == "__main__":
    str1 = IOString()     
    str1.get_String()     
    str1.print_String()   
