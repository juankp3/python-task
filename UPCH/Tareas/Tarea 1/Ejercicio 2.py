#Tarea 1
#Ejercicio 2

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))
num4 = int(input("Ingrese el cuarto número: "))
num5 = int(input("Ingrese el quinto número: "))


if num1>=num2:
    if num1>=num3:
        if num1>=num4:
            if num1>=num5:
                mayor=num1
            else:
                mayor=num5
        else:
            if num4>=num5:
                mayor=num4
            else:
                mayor=num5
    else:
        if num3>=num4:
            if num3>=num5:
                mayor=num3
            else:
                mayor=num5
        else:
            if num4>=num5:
                mayor=num4
            else:
                mayor=num5
else:
    if num2>=num3:
        if num2>=num4:
            if num2>=num5:
                mayor=num2
            else:
                mayor=num5
        else:
            if num4>=num5:
                mayor=num4
            else:
                mayor=num5
    else:
        if num3>=num4:
            if num3>=num5:
                mayor=num3
            else:
                mayor=num5
        else:
            if num4>=num5:
                mayor=num4
            else:
                mayor=num5


if num1<=num2:
    if num1<=num3:
        if num1<=num4:
            if num1<=num5:
                menor=num1
            else:
                menor=num5
        else:
            if num4<=num5:
                menor=num4
            else:
                menor=num5
    else:
        if num3<=num4:
            if num3<=num5:
                menor=num3
            else:
                menor=num5
        else:
            if num4<=num5:
                menor=num4
            else:
                menor=num5
else:
    if num2<=num3:
        if num2<=num4:
            if num2<=num5:
                menor=num2
            else:
                menor=num5
        else:
            if num4<=num5:
                menor=num4
            else:
                menor=num5
    else:
        if num3<=num4:
            if num3<=num5:
                menor=num3
            else:
                menor=num5
        else:
            if num4<=num5:
                menor=num4
            else:
                menor=num5



