def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Приклад виклику функції з параметром n 
result = fibonacci(int(input("Введіть число: ")))
print(result)