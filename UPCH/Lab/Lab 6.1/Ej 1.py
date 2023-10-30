#Lab 6.1
#Ej 1

#a) A=3, B=22 Entonces en B sumamos 1 más

##A=3
##B=23
##
##for S in range(A,B):
##    print(S)              

#Con múltiplos de 5 en forma horizontal ,end

##A=3
##B=23
##
##for i in range(A,B+1):
##    if i%5==0:
##        print(i, end=" ")


#b)

A=int(input("A="))
while A<=0:
    print("Error, A debe ser positivo")
    A=int(input("A= "))
print("Valor aceptado para A= ",A)

B=int(input("B="))
while B<=0:
    print("Error, B debe ser positivo")
    B=int(input("B= "))
print("Valor aceptado para B= ",B)

print("A= ", A, "B= ", B)

if A>B:
    aux=A
    A=B
    B=aux

suma=0

for i in range(A,B+1):
    if i%5==0:
        print(i,"*")
        suma=suma+i
    else:
         print(i)

print("La suma de múltiplos de 5 es: ", suma)






      
