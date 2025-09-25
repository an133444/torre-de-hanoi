print('Torres de Hanoi')

# Definición de la función recursiva para resolver las Torres de Hanoi
def hanoi(n, origen, destino, auxiliar, pasos):
    # Caso base: si solo hay un disco, se mueve directamente
    if n == 1:
        pasos.append((origen, destino))  # Registrar el movimiento
    else:
        # Mover n-1 discos al auxiliar
        hanoi(n-1, origen, auxiliar, destino, pasos)
        pasos.append((origen, destino))  # Mover el disco más grande al destino
        # Mover los n-1 discos desde el auxiliar al destino
        hanoi(n-1, auxiliar, destino, origen, pasos)

# Función para obtener el número de discos del usuario
def obtener_n():
    entrada = input("Ingrese el número de discos (1-20): ")  # Solicitar entrada
    return int(entrada)  # Convertir la entrada a entero

# Función principal del programa
def main():
    try:
        n = obtener_n()  # Obtener el número de discos
        if not (1 <= n <= 20):  # Validar el rango permitido
            raise ValueError
    except:
        print("Error: Ingrese un número entero válido entre 1 y 20.")  # Mensaje de error
        return
    pasos = []  # Lista para almacenar los movimientos
    hanoi(n, 'A', 'C', 'B', pasos)  # Llamar a la función recursiva
    for i, (o, d) in enumerate(pasos, 1):  # Mostrar cada paso
        print(f"Paso {i}: mover disco desde {o} hacia {d}")
    print(f"Total de movimientos: {len(pasos)} (esperado: {2**n-1})")  # Mostrar el total

# Ejecutar la función principal si el archivo es ejecutado directamente
if __name__ == "__main__":
    main()
