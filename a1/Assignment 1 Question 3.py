def pale(n):
    last_2_digits = n % 100
    first_2_digits = n // 100
    middle_2_digits = (n // 10) % 100
    last_digit = n % 10
    return not (last_2_digits == 33 or first_2_digits == 33 or middle_2_digits == 33 or last_digit % 4 ==0 or last_digit == 33) 
