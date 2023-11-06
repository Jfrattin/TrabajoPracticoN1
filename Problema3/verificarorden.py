import os

def verificar_ordenamiento(archivo_original, archivo_ordenado):
    # Verificar el ordenamiento de los datos cargandolos todos a memoria y si estos están ordenados
    with open(archivo_ordenado, 'r') as archivo:
        lineas_ordenadas = archivo.readlines()
    
    if verificar_ordenamiento_lineas(lineas_ordenadas):
        print("El archivo está ordenado correctamente.")
    else:
        print("Error: El archivo no está ordenado correctamente.")

def verificar_ordenamiento_lineas(lineas):
    for i in range(len(lineas) - 1):
        numero_actual = obtener_numero_entero(lineas[i])
        numero_siguiente = obtener_numero_entero(lineas[i+1])
        
        if numero_actual > numero_siguiente:
            return False
    return True

def obtener_numero_entero(linea):
    palabras = linea.strip().split()
    for palabra in palabras:
        try:
            numero_entero = int(palabra.strip())
            return numero_entero
        except ValueError:
            continue

    return 0

# Ejecutar la función de verificación
verificar_ordenamiento('C:/AlgoritmosTuped/problema3/datos.txt', 'C:/AlgoritmosTuped/problema3/datos_ordenados.txt')
