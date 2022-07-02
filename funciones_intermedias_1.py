# EJERCICIO 1: Actualizar valores en diccionarios y listas
# x = [ [5,2,3], [10,8,9] ] 
# estudiantes = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# directorio_deportes = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]

# LITERAL 1: Cambia el valor 10 en x a 15. Una vez que hayas terminado, x ahora debería ser [ [5,2,3], [15,8,9] ].

x = [ [5,2,3], [10,8,9] ] 
x[1][0]=15
print(f"EJERCICIO 1 - LITERAL 1 - Resultado:\n{x}")

# LITERAL 2: Cambia el "apellido” del primer alumno de 'Jordan' a 'Bryant'.
print("------------------------------------------------------------")
estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
estudiantes[0]["last_name"] = 'Bryant'
print(f"EJERCICIO 1 - LITERAL 2 - Resultado:\n{estudiantes}")

# LITERAL 3: En el directorio_deportes, cambia "Messi" por "Andrés".
print("------------------------------------------------------------")
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}

directorio_deportes['fútbol'][0]="Andrés"
print(f"EJERCICIO 1 - LITERAL 3 - Resultado:\n{directorio_deportes}")

# LITERAL 4: Cambia el valor 20 en z a 30.
print("------------------------------------------------------------")
z = [ {'x': 10, 'y': 20} ]
z[0]["y"] = 30
print(f"EJERCICIO 1 - LITERAL 4 - Resultado:\n{z}")


#/////////////////////////////////////////////////////////////////////////////////////////
#EJERCICIO 2: Iterar a través de una lista de diccionarios
# Crea una función iterateDictionary(some_list)para que, dada una lista de diccionarios, la función recorra
# cada diccionarios de la lista e imprima cada llave y el valor asociado. Por ejemplo, dada la siguiente lista:
print("------------------------------------------------------------")
print(f"EJERCICIO 2 - LITERAL 1 - Resultado:\n")
estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
def iterateDictionary(diccionario):
    lista_completa = ""
    for dicc in diccionario:
        datos = []
        for key,val in dicc.items():
            datos_juntos = f"{key} - {val} "
            datos.append(datos_juntos)
        lista_completa += f"{', '.join(datos)}\n"
    return (lista_completa)

print(iterateDictionary(estudiantes))
# debería devolver: (está bien si cada par clave-valor termina en 2 líneas separadas;
# un bonus para que aparezcan exactamente como se muestra a continuación)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

#/////////////////////////////////////////////////////////////////////////////////////////
#EJERCICIO 3: Obtener valores de una lista de diccionarios
# Crea una función iterateDictionary2(key_name, some_list)que, dada una lista de diccionarios y un nombre de clave, la función 
# imprima el valor almacenado en esa clave para cada diccionario. Por ejemplo, iterateDictionary2('name', estudiantes) debería generar:
print("------------------------------------------------------------")
print(f"EJERCICIO 3 - LITERAL 1 - Resultado:\n")

estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def iterateDictionary2(key_name, some_list):
    retorno = ""
    for dicc in some_list:
        retorno += f"{dicc[key_name]}\n"
    return retorno

print(iterateDictionary2("first_name", estudiantes))
print(iterateDictionary2("last_name", estudiantes))

#/////////////////////////////////////////////////////////////////////////////////////////
#EJERCICIO 4: Iterar a través de un diccionarios con valores de lista
# Crea una función printInfo(some_dict)que, dado un diccionario cuyos valores son todos listas, imprima el nombre de cada clave junto 
# con el tamaño de su lista, y luego imprima los valores asociados dentro de la lista de cada clave. Por ejemplo:

dojo = {
    'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

print("------------------------------------------------------------")
print(f"EJERCICIO 4 - LITERAL 1 - Resultado:\n")

def printInfo(some_dict):
    for key in some_dict:
        print (len(some_dict[key]),key.upper())
        lista = ""
        for val in some_dict[key]:
            lista +=f"{val}\n"
        print(lista)

printInfo(dojo)

# salida:
# 7 UBICACIONES
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORES
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon