#Función de contador

#1: Inicializar el contador y acumulador
acum=0
cont=1
#2: Colocar el contador en la condición
while cont<=5:
    print(cont)
    dato=int(input("dato= "))
    
#4: Actualizar el acum
    acum=acum+dato
    
#3: Actualizar el contador
    cont=cont+1
    
#Imprimir la suma
print("La suma es=", acum)
