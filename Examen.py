'''
La evaluación consiste en:

Desarrollar una aplicación en Python utilizando los conceptos de programación desarrollados durante la asignatura:
- Estructuras de entrada y salida
- Estructuras de decisión
- Estructuras de repetición
- Colecciones
- Funciones
- Manejo de archivos

Desarrolle una aplicación en Python utilizando Visual Studio Code como entorno de desarrollo según el siguiente enunciado:

Una empresa necesita analizar los datos de sus trabajadores para generar algunos reportes, y le ha solicitado a usted que
realice un prototipo en Python con los siguientes requerimientos:

La aplicación debe permitir analizar los sueldos de 10 empleados, los cuales para efectos de este prototipo se crearán de
forma aleatoria entre $300.000 y $2.500.000.

Utilice la siguiente lista para asignar los sueldos a cada empleado:
trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel
Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]

La aplicación deberá poseer un menú con las siguientes funcionalidades:
1. Asignar sueldos aleatorios.
2. Clasificar Sueldos.
3. Ver Estadísticas.
4. Reporte de Sueldos.
5. Salir del Programa.

Cada función se detalla a continuación:

1. Asignar sueldos aleatorios
Para la generación de estos sueldos debe crear una función capaz de generar los 10 sueldos de forma aleatoria los que serán 
usados posteriormente para la ejecución del programa.

2. Clasificar sueldos
Deberá desarrollar una función que permita mostrar la lista de empleados con su sueldo y su respectiva clasificación
según el siguiente esquema:

#Ejemplo Tabla de sueldos:

            TABLA DE SUELDOS
    *** Sueldos menores a $800.000 ***
    - TOTAL: 2

    Nombre empleado     Sueldo
    Juan Pérez          $   500.000
    María García        $   700.000

    *** Sueldos entre $800.000 y $2.000.000 ***
    - TOTAL: 2

    Nombre Empleado     Sueldo
    Pedro Soto          $ 1.100.000
    Isabel Gómez        $   800.000

    *** Sueldos superiores a $2.000.000 ***
    - TOTAL: 1

    Nombre Empleado     Sueldo
    Miguel Sánchez      $2.100.000

    ***    TOTAL SUELDOS:  $ 5.200.000   ***


3. Ver estadísticas
Crear una función que permita mostrar por pantalla los siguientes datos con respecto a los sueldos:
- Sueldo más alto
- Sueldo más bajo
- Promedio de sueldos
- Media geométrica

4. Reporte de sueldos
La aplicación deberá poseer una función para mostrar el detalle de los sueldos de los trabajadores, según la siguiente
regla de negocio:

- Descuento Salud 7%
- Descuento AFP 12%
- Sueldo líquido calculado en base al sueldo base menos el descuento en salud y menos el descuento afp.

Y mostrarse como en la siguiente tabla de ejemplo:

Ejemplo Sueldos en Pantalla:

    |                                       LISTADO DE SUELDOS                                      |
    |   Nombre empleado |   Sueldo Base |   Descuento Salud |   Descuento AFP   |   Sueldo Líquido  |
    |   Juan Pérez      |   $1000000    |       $ 70000     |       $ 120000    |       $ 810000    |
    |   Pedro Soto      |   $ 800000    |       $ 56000     |       $  96000    |       $ 648000    |

*(Estos datos se deberán exportar a un archivo de texto separado por comas (.csv) para su posterior lectura en otra
aplicación)

5. Salir del programa
La aplicación deberá finalizar para salir el programa mostrando un mensaje con sus datos

Ejemplo Mensaje salida de la aplicación:

    Finalizando Programa...
    Desarrollado por Héctor Águila
    Ingeniería Informática - Vespertino
    RUT: 15.996.388-8
'''


import random
import csv
import statistics

# Lista de trabajadores
trabajadores = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez",
                "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]

# Diccionario donde se almacenarán los sueldos.
sueldos = {}

# Aleatorización de sueldos
def asignar_sueldos():
    global sueldos
    sueldos = {trabajador: random.randint(300000, 2500000) for trabajador in trabajadores}
    print("\nSueldos Asignados Aleatoriamente.\n")

# Clasificación de los sueldos
def clasificar_sueldos():
    if not sueldos:
        print("Primero asigne los sueldos.\n")
        return

    menores_800000 = {sueldo: monto for sueldo, monto in sueldos.items() if monto < 800000}
    entre_800000_2000000 = {sueldo: monto for sueldo, monto in sueldos.items() if 800000 <= monto <= 2000000}
    mayores_2000000 = {sueldo: monto for sueldo, monto in sueldos.items() if monto > 2000000}
    
    print("\n*** Sueldos menores a $800.000 ***")
    print(f"TOTAL: {len(menores_800000)}")
    for sueldo, monto in menores_800000.items():
        print(f"{sueldo: <20} ${monto: >10,}")
    
    print("\n*** Sueldos entre $800.000 y $2.000.000 ***")
    print(f"TOTAL: {len(entre_800000_2000000)}")
    for sueldo, monto in entre_800000_2000000.items():
        print(f"{sueldo: <20} ${monto: >10,}")
    
    print("\n*** Sueldos superiores a $2.000.000 ***")
    print(f"TOTAL: {len(mayores_2000000)}")
    for sueldo, monto in mayores_2000000.items():
        print(f"{sueldo: <20} ${monto: >10,}")
    
    print("\n*** TOTAL SUELDOS: $", sum(sueldos.values()), " ***\n")

# Mostrar las estadísticas
def ver_estadisticas():
    if not sueldos:
        print("Primero asigne los sueldos.\n")
        return
    max_sueldo = max(sueldos.values())
    min_sueldo = min(sueldos.values())
    promedio = statistics.mean(sueldos.values())
    media_geometrica = statistics.geometric_mean(sueldos.values())
    
    print(f"\nSueldo más alto: ${max_sueldo:,}")
    print(f"Sueldo más bajo: ${min_sueldo:,}")
    print(f"Promedio de sueldos: ${promedio:,.0f}")
    print(f"Media geométrica: ${media_geometrica:,.0f}\n")

# Función para reporte de sueldos
def reporte_sueldos():
    if not sueldos:
        print("Primero asigne los sueldos.\n")
        return
    descuentos = []
    for trabajador, sueldo_base in sueldos.items():
        descuento_salud = sueldo_base * 0.07
        descuento_afp = sueldo_base * 0.12
        sueldo_liquido = sueldo_base - descuento_salud - descuento_afp
        descuentos.append([trabajador, sueldo_base, descuento_salud, descuento_afp, sueldo_liquido])
    
    print(f"\n| {'Nombre Empleado':<20} | {'Sueldo Base':<15} | {'Descuento Salud':<15} | {'Descuento AFP':<15} | {'Sueldo Líquido':<15} |")
    for d in descuentos:
        print(f"| {d[0]:<20} | ${d[1]:<14,} | ${d[2]:<14,.0f} | ${d[3]:<14,.0f} | ${d[4]:<14,.0f} |")
            
    with open('reporte_sueldos.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Nombre Empleado", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo Líquido"])
        writer.writerows(descuentos)
    print("\nReporte de sueldos exportado a 'Reporte_Sueldos.csv'.\n")

# Menú
def mostrar_menu():
    print("Seleccione una opción:")
    print("1. Asignar sueldos aleatorios")
    print("2. Clasificar sueldos")
    print("3. Ver estadísticas")
    print("4. Reporte de sueldos")
    print("5. Salir del programa")

# Función principal
def main():
    while True:
        mostrar_menu()
        opcion = input("Ingrese su opción: ")
        
        if opcion == '1':
            asignar_sueldos()
        elif opcion == '2':
            clasificar_sueldos()
        elif opcion == '3':
            ver_estadisticas()
        elif opcion == '4':
            reporte_sueldos()
        elif opcion == '5':
            print("\nFinalizando Programa...")
            print("Desarrollado por Héctor Águila")
            print("Ingeniería Informática - Vespertino")
            print("RUT: 15.996.388-8")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
