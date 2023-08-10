# Definición de variables de distintos tipos

#Entero (int)
entero = 10

#Flotante (float)
flotante = 3.14

#Cadena de caracteres (str)
cadena = "Hola, mundo"

#Booleano (bool)
booleano = True

#Valor nulo (NoneType)
nulo = None


# Concatenación de variables y conversión
concatenacion = cadena + " - Entero: " + str(entero) + " - Flotante: " + str(flotante) + " - Booleano: " + str(booleano)

# Límites de enteros y flotantes
limite_enteros = 2**31 - 1  # Límite para enteros con signo de 32 bits en Python
limite_flotantes = 1.8e308  # Límite para flotantes en Python

# Fórmula para la suma de los primeros n números pares: n * (n + 1)
n = entero
suma_pares = n * (n + 1)

# Impresión de resultados
print("Concatenación:", concatenacion)
print("Límite de enteros:", limite_enteros)
print("Límite de flotantes:", limite_flotantes)
print("Suma de los primeros", n, "números pares:", suma_pares)
