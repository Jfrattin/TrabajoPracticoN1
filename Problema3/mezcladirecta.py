
from random import randint

def crear_archivo_de_datos(nombre, mb ):
    factor= mb/10
    
    f = 10**5
    N = 5*f
    
    cifras = 20
    tam_bloque = f # 1 M de valores por bloque a escribir
    
    print('Cantidad de valores a escribir:', N)
    
    # truncar archivo si existe
    with open(nombre, 'w') as archivo:
        pass
    
    # escribir datos
    N_restantes = N
    while N_restantes > 0:
        cif = cifras
        r = N_restantes % tam_bloque
        c = N_restantes // tam_bloque
        if c > 0:
            t = tam_bloque
        elif c == 0:
            t = r
        N_restantes -= t
        print('t =', t, ', N_restantes =', N_restantes)
        bloque = [str(randint(10**(cif-1), 10**cif-1))+'\n'
                  for i in range(t)]        
        with open(nombre, 'a+') as archivo:
            archivo.writelines(bloque)         

def merge_sort_externo(archivo_entrada, archivo_salida, tamano_bloque=1000):
    # División en bloques y ordenamiento interno
    bloques_ordenados = []
    with open(archivo_entrada, 'r') as file_entrada:
        while True:
            # Leer un bloque de líneas del archivo de entrada
            lineas = []
            for _ in range(tamano_bloque):
                linea = next(file_entrada, None)
                if linea is None:
                    break  # Si no quedan más líneas, sal del bucle
                lineas.append(int(linea.strip()))

            if not lineas:
                break  # Si no quedan más líneas, sal del bucle

            # Ordenar el bloque actual
            lineas_ordenadas = sorted(lineas)
            
            # Guardar el bloque ordenado en la lista
            bloques_ordenados.append(lineas_ordenadas)

    # Fusión de bloques y escritura en el archivo de salida
    with open(archivo_salida, 'w') as file_salida:
        merge_blocks(bloques_ordenados, file_salida)

def merge_blocks(sorted_blocks, file_salida):
    # Fusión de bloques (Mezcla Directa)
    while len(sorted_blocks) > 1:
        min_block_index = min(range(len(sorted_blocks)), key=lambda i: sorted_blocks[i][0])
        min_block = sorted_blocks[min_block_index]
        min_value = min_block.pop(0)
        if not min_block:
            sorted_blocks.pop(min_block_index)
        file_salida.write(f"{min_value}\n")
    
    for value in sorted_blocks[0]:
        file_salida.write(f"{value}\n")

def crearyordenar(archivo_entrada, archivo_salida,mb):
    crear_archivo_de_datos(archivo_entrada, mb )
    merge_sort_externo(archivo_entrada, archivo_salida)


if __name__ == "__main__":
    tamaño=10
    archivo_entrada = 'C:\AlgoritmosTuped\Problema3\datos.txt'
    archivo_salida = 'archivo_salida.txt'
    crearyordenar(archivo_entrada, archivo_salida,10)
    print("El archivo se creo y se ordeno de manera correcta.")