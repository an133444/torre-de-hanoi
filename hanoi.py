print('Torres de Hanoi')

# Definición de la función recursiva para resolver las Torres de Hanoi
def hanoi(n, origen, destino, auxiliar, pasos):
    """
    Resuelve el clásico problema de las Torres de Hanoi de forma recursiva.
    
    El objetivo es mover 'n' discos de la torre 'origen' a la torre 'destino'
    utilizando una torre 'auxiliar', siguiendo estas reglas:
    1. Solo se puede mover un disco a la vez.
    2. Un disco más grande nunca puede colocarse encima de un disco más pequeño.
    
    Args:
        n (int): El número de discos a mover.
        origen (str): El nombre de la torre de origen (e.g., 'A').
        destino (str): El nombre de la torre de destino (e.g., 'C').
        auxiliar (str): El nombre de la torre auxiliar (e.g., 'B').
        pasos (list): Una lista para almacenar cada movimiento realizado.
                      Cada movimiento se guarda como una tupla (origen, destino).
    """
    # Caso base de la recursión: Cuando solo queda un disco por mover.
    # Si hay un solo disco (n=1), se puede mover directamente de la torre de origen a la de destino.
    if n == 1:
        pasos.append((origen, destino))  # Se registra el movimiento del disco único.
    else:
        # Paso 1: Mover los n-1 discos superiores de la torre de origen a la torre auxiliar.
        # Para hacer esto, la torre de destino actual se convierte en la torre auxiliar temporal,
        # y la torre auxiliar se convierte en la de destino temporal para estos n-1 discos.
        hanoi(n-1, origen, auxiliar, destino, pasos)
        
        # Paso 2: Mover el disco más grande (el n-ésimo disco) restante en la torre de origen
        # directamente a la torre de destino final. Este movimiento es crucial porque es el único
        # que mueve el disco más grande a su posición final.
        pasos.append((origen, destino))  # Se registra este movimiento.
        
        # Paso 3: Mover los n-1 discos que están ahora en la torre auxiliar a la torre de destino final.
        # Para esto, la torre de origen original se convierte en la torre auxiliar temporal,
        # y la torre auxiliar se convierte en la de origen temporal para estos n-1 discos.
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
