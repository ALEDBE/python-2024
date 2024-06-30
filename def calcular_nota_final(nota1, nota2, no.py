def calcular_nota_final(nota1, nota2, nota3, nota4, nota5):
    # Suponemos que todas las notas tienen el mismo peso
    notas = [nota1, nota2, nota3, nota4, nota5]
    nota_final = sum(notas) / len(notas)
    return nota_final

# Ejemplo de uso del programa
nota1 = float(input("Ingrese la nota 1: "))
nota2 = float(input("Ingrese la nota 2: "))
nota3 = float(input("Ingrese la nota 3: "))
nota4 = float(input("Ingrese la nota 4: "))
nota5 = float(input("Ingrese la nota 5: "))

# Calcular la nota final llamando a la función
nota_final = calcular_nota_final(nota1, nota2, nota3, nota4, nota5)

# Imprimir el resultado
print(f"La nota final del estudiante es: {nota_final}")
