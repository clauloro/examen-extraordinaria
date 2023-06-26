def power_of_4(n):
    if not isinstance(n, int) or n <= 0:
        return False
    while n % 4 == 0:
        n /= 4
    return n == 1

print(power_of_4(1024))  
print(power_of_4(55))  
print(power_of_4("Four"))  
