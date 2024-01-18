def pow_function(x, n):
    
    if n == 0:
        return 1.0
    
    if n < 0:
        x = 1 / x
        n = -n

    if n % 2 == 0:
        half_pow = pow_function(x, n // 2)
        return half_pow * half_pow
    else:
        half_pow = pow_function(x, (n - 1) // 2)
        return x * half_pow * half_pow

x =int(input("Введи число: "))
n = int(input("Введи ступінь: "))
print(pow_function(x, n))  
