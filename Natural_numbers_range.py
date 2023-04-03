def getNaturalNumbers(num1, num2):
    # Check for negative or zero inputs
    if num1 <= 0 or num2 <= 0:
        return "-1"
    
    if num1 == num2:
        return str(num1)
    
    # Swap num1 and num2 if num1 is greater
    if num1 > num2:
        num1, num2 = num2, num1
    
    result = ""
    i = num1
    while i <= num2:
        result += str(i) + " "
        i += 1
    
    
    result = result[:-1]
    
    return result
print(getNaturalNumbers(1,10))
