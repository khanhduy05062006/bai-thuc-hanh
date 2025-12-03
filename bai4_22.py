def all_digits_even(num):
    for digit in str(num):
        if int(digit) % 2 != 0:
            return False
    return True
even_digit_numbers = [str(i) for i in range(1000, 3001) if all_digits_even(i)]
print(",".join(even_digit_numbers))
