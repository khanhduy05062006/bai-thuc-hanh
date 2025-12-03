
n = int(input("Nhập số phần tử của dãy Fibonacci: "))
fibo = [0, 1]
if n <= 0:
    print("Vui lòng nhập số nguyên dương!")
elif n == 1:
    print("Dãy Fibonacci:", [0])
else:
    for i in range(2, n):
        fibo.append(fibo[i-1] + fibo[i-2])
    print("Dãy Fibonacci gồm", n, "phần tử đầu tiên là:")
    print(fibo)
