#Lab 7.1
#Ejemplo 1
#Sin anidamiento

##x=14
##s=0
##for c in range(1,11):
##    s=s+x**c
##    print("x=",x, "s=",s)
##
##x=15
##s=0
##for c in range(1,11):
##    s=s+x**c
##    print("x=",x, "s=",s)
##
##x=16
##s=0
##for c in range(1,11):
##    s=s+x**c
##    print("x=",x, "s=",s)
##
##x=17
##s=0
##for c in range(1,11):
##    s=s+x**c
##    print("x=",x, "s=",s)
##
    
#Con anidamiento
#Usa una variable diferente por cada bucle

for x in range(14,18): #bucle externo
    s=0
    for c in range (1,11): #bucle interno
        s=s+x**c
        print("x=",x, "s=",s)
