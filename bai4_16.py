def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True
primes = tuple(i for i in range(2, 1_000_000) if is_prime(i))
print(f"Tổng số số nguyên tố nhỏ hơn 1 triệu là: {len(primes)}")
print(primes[:10])
