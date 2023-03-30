
def DiffOfDigits(num):
    if num < 0:
        return -3
    elif num >= 10 and num <= 99:
        tens_digit = num // 10
        ones_digit = num % 10
        return tens_digit - ones_digit
    else:
        return -2
print(DiffOfDigits(83))  
print(DiffOfDigits(38))
print(DiffOfDigits(-5))



