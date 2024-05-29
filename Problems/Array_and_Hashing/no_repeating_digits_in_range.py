def has_no_repeating_digits(num):

    if num < 0:
        return False

    seen = 0
    while num > 0:
        digit = num % 10
        if seen & (1 << digit):
            return False
        seen |= 1 << digit
        num //= 10
    return True


def count_numbers_with_no_repeating_digits(start, end):
    count = 0
    for num in range(start, end + 1):
        if has_no_repeating_digits(num):
            count += 1
    return count



start_range = 2
end_range = 20

result = count_numbers_with_no_repeating_digits(start_range, end_range)
print(f"The count of numbers with no repeating digits in the range [{start_range}, {end_range}] is: {result}")
