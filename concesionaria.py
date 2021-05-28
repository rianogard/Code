def validacion(dato, comparacion, mensaje):
    while dato not in comparacion:
        dato = input(mensaje)


def calcular_precio(marca, puertas, color, ventas):
    autos = {'ford': 100000, 'chevrolet': 120000, 'fiat': 80000}
    cant_puertas = {'2': 50000, '4': 65000, '5': 78000}
    colores = {'blanco': 10000, 'azul': 20000, 'negro': 30000}

    precio = autos[marca] + colores[color] + cant_puertas[puertas]

    if ventas > 5 and ventas < 11:
        precio = precio * 0.9
    elif ventas > 10 and ventas < 51:
        precio = precio * 0.85
    elif ventas > 50:
        precio = precio * 0.82
    return precio


autos = ['ford', 'chevrolet', 'fiat']
cant_puertas = ['2', '4', '5']
colores = ['blanco', 'azul', 'negro']
ventas = []
cant_ventas = len(ventas)
mas_clientes = 'si'

print("-------------------PROGRAMA DE VENTa DE AUTOS-------------------")

while mas_clientes == 'si':
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")

    marca = input("Ingrese la marca (Ford, Chevrolet, Fiat): ")
    marca = marca.lower()
    validacion(marca, autos, "Marca invalida. Ingrese otra marca: ")
    marca = marca.lower()

    puertas = input("Ingrese la cantidad de puertas: ")
    validacion(puertas, cant_puertas, "Cantidad de puertas invalida. Ingrese otra cantidad de puertas: ")

    color = input("Ingrese el color (Blanco, Azul, Negro): ")
    color = color.lower()
    validacion(color, colores, "Color Invalido. Ingrese otro color: ")
    color = color.lower()

    precio = calcular_precio(marca, puertas, color, cant_ventas)

    ventas.append({'nombre': nombre, 'apellido': apellido, 'marca': marca,
                   'puertas': puertas, 'color': color, 'precio': precio})

    mas_clientes = input("seguir cargando clientes? (si/no) ")

for i in ventas:
    print(i['nombre'] + " " + i['apellido'] + " compro un " + i['marca'] + " " +
          i['color'] + " de " + i['puertas'] + " puertas a $" + str(i['precio']))
