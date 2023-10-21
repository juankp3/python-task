#Lab 7.1
#Ej 4

numAtletas = 10
numMediciones = 5

for atleta in range(1, numAtletas + 1):
    print(f"Atleta {atleta}:")
    pesoAnterior = float(input("Ingrese el peso anterior: "))
    sumaPesosActual = 0

    for medicion in range(1, numMediciones + 1):
        pesoActual = float(input(f"Ingrese el peso {medicion}: "))
        sumaPesosActual += pesoActual

    promedioPesoActual = sumaPesosActual / numMediciones
    variacion = promedioPesoActual - pesoAnterior

    estado = "subió de peso" if variacion > 0 else ("bajó de peso" if variacion < 0 else "estable")

    print(f"Estado general: {estado}")
    print(f"Variación de peso: {abs(variacion):.2f} kg\n")
