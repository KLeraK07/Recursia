def pow_function(x, n):
    # x^0 = 1
    if n == 0:
        return 1.0
    
    # Від'ємний показник ступеня
    if n < 0:
        x = 1 / x
        n = -n

    # Парний показник ступеня
    if n % 2 == 0:
        half_pow = pow_function(x, n // 2)
        return half_pow * half_pow
    # Непарний показник ступеня
    else:
        half_pow = pow_function(x, (n - 1) // 2)
        return x * half_pow * half_pow

# Приклади виклику функції
x =int(input("Введи число: "))
n = int(input("Введи ступінь: "))
print(pow_function(x, n))  