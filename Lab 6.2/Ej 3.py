#Lab 6.2
#Ej 3

import random
print("¡Bienvenido al tutor de la tabla de multiplicar!")

seguir="sí"

while seguir=="sí":
        num1= random.randint(1,9)
        num2= random.randint(1,9)
        msj=("¿Cuánto es: ?"+str(num1)+"x"+str(num2))


        result= num1*num2
        if result==msj:
            print("Correcto")
            seguir= input("¿Deseas continuar (sí/no): ?")
        else:
            print("Incorrecto. El resultado es= ", result)
else:
    print("¡Muchas gracias, vuelve pronto!")
    
