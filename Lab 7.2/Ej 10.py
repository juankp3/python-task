#Lab 7.2
#Ej 10

print("Números primos entre 1 y 10000:")
for num in range(2, 10001):
    es_primo = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            es_primo = False
            break
    if es_primo:
        print(num, end=" ")

print("\nNúmeros perfectos entre 1 y 10000:")
for num in range(2, 10001):
    suma_divisores = sum([i for i in range(1, num) if num % i == 0])
    if suma_divisores == num:
        print(num, end=" ")
