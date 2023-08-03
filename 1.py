def reverse_number(n, rev_n=0):
    if n == 0:
        return rev_n
    else:
        last_digit = n % 10
        rev_n = rev_n * 10 + last_digit
        return reverse_number(n // 10, rev_n)

# Example usage:
num = 12345
reversed_num = reverse_number(num)
print(f"The reversed number of {num} is {reversed_num}")
