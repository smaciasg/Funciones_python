# EJERCICIO 1 Cuenta regresiva: crea una función que acepte un número como entrada. Devuelve una lista nueva que cuente de uno en uno,
#  desde el número (como elemento 0) hasta 0 (como último elemento). 

def cuenta_regresiva(num):
    return  [i for i in range(num,-1,-1)]

print(f"EJERCICIO 1 - Resultado:\n{cuenta_regresiva(10)}\n")

# EJERCICIO 2 Imprimir y devolver: crea una función que reciba una lista con dos números. Imprime el primer valor y devuelve el segundo.
# Ejemplo: imprimir_y_devolver([1,2]) debe imprimir 1 y devolver 2

print("-----------------------------------------")
print("EJERCICIO 2 - Resultado:")
def imprimir_y_devolver(lista):
    for num in lista:
        print(lista[0])
        return lista[1]
x= imprimir_y_devolver([15,23])
print(x)

# EJERCICIO 3: Primero más longitud: crea una función que acepte una lista y devuelva la suma del primer valor de la lista, más la longitud de la lista.
# Ejemplo: primero_mas_longitud([1,2,3,4,5]) debe devolver 6 (primer valor: 1 +length: 5)

print("-----------------------------------------")

def primero_mas_longitud(lista):
    sum= lista[0] + len(lista)
    return sum

print(f"EJERCICIO 3 - Resultado:\n{primero_mas_longitud([10,20,30,40,50])}")

#EJERCICIO 4: Valores mayores que el segundo: escribe una función que acepte una lista y cree una nueva que contenga solo 
# los valores de la lista original que sean mayores que su segundo valor. Imprime cuántos valores son y luego devuelve la 
# lista nueva. Si la lista tiene menos de 2 elementos, has que la función devuelva False
# Ejemplo: valores_mayores_que_el_segundo([5,2,3,2,1,4]) debe imprimir 3 y devolver [5,3,4]
# Ejemplo: valores_mayores_que_el_segundo([3]) debe devolver False

print("-----------------------------------------")
print("EJERCICIO 4 - Resultado:\n")
def valores_mayores_que_el_segundo(lista):
    lista_mayores = []
    if len(lista) < 2:
        return False
    else: 
        for i in lista:
            if i>lista[1]:
                lista_mayores.append(i)
        print(f"La cantidad de valores mayores que {lista[1]} es {len(lista_mayores)}")
        return lista_mayores

lista= [5,1]
val_mayores = valores_mayores_que_el_segundo(lista)

if val_mayores != False: 
    print(f"y estos números son: {val_mayores}")
else:
    print("False - Lista menor a dos componentes")

# EJERCICIO 5: Esta longitud, ese valor: escribe una función que acepte dos enteros como parámetros: tamaño y valor. La función debe crear y devolver una lista cuya longitud sea igual al tamaño dado, y cuyos valores sean todos el valor dado.
# Ejemplo: length_and_value(4,7) debe devolver [7,7,7,7]
# Ejemplo: length_and_value(6,2) debe devolver [2,2,2,2,2,2]

print("-----------------------------------------")

def length_and_value(repeticiones,numero):
    lista = []
    while repeticiones>0:
        lista.append(numero)
        repeticiones -=1
    return lista

print(f"EJERCICIO 5 - Resultado:\n{length_and_value(3,7)}")