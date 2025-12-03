data = ["Apple", "Banana", "Orange", "Mango"]

filename = "output.txt"

with open(filename, "w", encoding="utf-8") as f:
    for item in data:
        f.write(item + "\n")

print("Đã ghi danh sách vào tệp", filename)
