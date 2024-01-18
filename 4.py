def Stairs(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    
    k = [0] * (n + 1)
    k[1] = 1
    k[2] = 2
    
    for i in range(3, n + 1):
        k[i] = k[i - 1] + k[i - 2]
    
    return k[n]

result = Stairs(int(input("Число від 1 до 45: ")))
print(result)
