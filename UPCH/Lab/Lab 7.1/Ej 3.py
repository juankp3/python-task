#Lab 7.1
#Ej 3

seguir="Sí"

num=int(input("Ingrese un número: "))

print("Las operaciones disponibles son:")
print("A: Suma de dígitos")
print("B: Mayor y menor dígito")
print("C: Numero inverso")
print("D: Intercambiar el primer y último digito")
print("E: Salir")

op=input("\n¿Qué operación desea realizar?: ")

if op=="A":
    N=num
    suma=0
    while N>0:
        r=N%10
        N=N//10
        suma=suma+r
    print("La suma de cifras:", suma)

if op=="B":
    N=num
    mayor=N%10
    acum=0
    while N!=0:
        r=N%10
        if r>mayor:
            mayor=r
        acum=acum+r
        N=N//10
    print("La mayor cifra es:", mayor)
    




while seguir=="Sí":
    seguir=input("¿Desea seguir (sí/no)= ")

    
if op=="E":
    print("¡Gracias, vuelva pronto!")

    
