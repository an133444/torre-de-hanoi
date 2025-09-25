Actividad Avanzada de Recursividad en Python: Torres de Hanoi
Objetivo

Aplicar recursividad mediante la resolución del problema de las Torres de Hanoi, implementando manejo de errores, soporte para N discos (parámetro), e impresión de cada movimiento. Además, practicar flujo de trabajo colaborativo con Git y GitHub utilizando ramas por integrante y pull requests.
Enunciado

Implemente un programa en Python que resuelva el problema de las Torres de Hanoi para N discos, donde N es un entero positivo ingresado por el usuario (o como argumento por línea de comandos). El programa debe imprimir cada movimiento en el formato: "Paso k: mover disco desde <origen> hacia <destino>". El algoritmo a usar debe ser recursivo.
Requisitos Funcionales

1) Debe aceptar un número de discos N (>= 1 y razonable, por ejemplo hasta 20).

2) Debe imprimir todos los movimientos en orden, numerados desde 1 hasta (2^N - 1).

3) Debe usar nombres de torres (por ejemplo A, B, C) y permitir personalización opcional.

4) Debe calcular y mostrar al final el número total de movimientos esperados (2^N - 1).
Requisitos Técnicos y de Calidad

• Implementación estrictamente recursiva del algoritmo de Hanoi.

• Manejo de errores:

  - Validar que N sea entero y esté dentro del rango permitido (p. ej., 1–20).

  - Capturar y reportar mensajes claros ante entradas inválidas (ValueError, TypeError).

• Código legible y documentado (docstrings, comentarios, tipado opcional).

• Pruebas básicas: verificación de la cantidad de movimientos para varios N (1, 2, 3, 4).
Entregables y Reglas de Envío (Git/GitHub)

• Trabajo individual o en parejas (máximo 2 estudiantes).

• El código debe subirse a un repositorio en GitHub.

• Cada integrante debe trabajar en su propia rama con su nombre o alias (ej.: feature/nombre-apellido).

• Todas las fusiones a main deben hacerse mediante Pull Request (PR), con revisión entre integrantes.

• Solo 1 persona realiza el envío del enlace del repositorio en la plataforma.

• Estructura sugerida del repo:

  /src/hanoi.py 
README.md

• Incluya un README con instrucciones para ejecutar el programa y las pruebas.
Guía Rápida de Flujo con Git (sugerido)

git clone <url_repo>
git checkout -b feature/tu-nombre
# implementas cambios
git add .
git commit -m "feat: implementar hanoi recursivo y validaciones"
git push -u origin feature/tu-nombre
# abrir Pull Request hacia main y solicitar revisión
Formato de Entrada y Salida

Entrada: un entero N (número de discos). Puede leerse por input() o por argumento --n/--discos.

Salida: impresión en consola de cada paso y un resumen final del total de movimientos.
Ejemplo de Salida (N = 3)

Paso 1: mover disco desde A hacia C
Paso 2: mover disco desde A hacia B
Paso 3: mover disco desde C hacia B
Paso 4: mover disco desde A hacia C
Paso 5: mover disco desde B hacia A
Paso 6: mover disco desde B hacia C
Paso 7: mover disco desde A hacia C
Total de movimientos: 7 (esperado: 2^3 - 1)