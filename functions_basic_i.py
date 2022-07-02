# #1
# def number_of_food_groups():
#     return 5
# print(number_of_food_groups())
# RESULTADO: 5


# #2
# def number_of_military_branches():
#     return 5
# print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
# RESULTADO: Debería salir un error ya que la función number_of_days_in_a_week_silicon_or_triangle_sides() no está definida antes de la
# invocación de la función.


# #3
# def number_of_books_on_hold():
#     return 5
#     return 10
# print(number_of_books_on_hold())
# RESULTADO: Imprime 5 ya que la función se detiene luego de return y en ese caso el primer return y el único que se ejecuta devuelve 5


# #4
# def number_of_fingers():
#     return 5
#     print(10)
# print(number_of_fingers())
# Imprime 5 ya que la función se detiene luego de return y en ese caso el print está luego del return por tanto no devuelve nada

# #5
# def number_of_great_lakes():
#     print(5)
# x = number_of_great_lakes()
# print(x)
# RESULTADO: Imprime 5 pero por que la función tiene un print más no por que sea valor de retorno, el segundo print no imprime nada.

# #6
# def add(b,c):
#     print(b+c)
# print(add(1,2) + add(2,3))
# RESULTADO: Ejecuta el print dentro de la función devolviendo de forma individual la suma de 1+2=3 y de 2+3=5; mas, debe 
# devolver un error en el print de la suma de la funciones ya que no hay una variable asignada que pueda procesar la operación 
# dentro del print.

# #7
# def concatenate(b,c):
#     return str(b)+str(c)
# print(concatenate(2,5))
# RESULTADO: 25 siendo el resultado una cadena no un número

# #8
# def number_of_oceans_or_fingers_or_continents():
#     b = 100
#     print(b)
#     if b < 10:
#         return 5
#     else:
#         return 10
#     return 7
# print(number_of_oceans_or_fingers_or_continents())
#RESULTADO: Primero imprime el valor de b=100, luego devuelve 10 dado que se cumple el IF, en este caso el return 7 nunca se cumple, dado
# que el condicional es el que indica cuáles return se deberán ejecutar.

# #9
# def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
#     if b<c:
#         return 7
#     else:
#         return 14
#     return 3
# print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3)) /// RESULTADO: 7
# print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3)) /// RESULTADO: 14
# print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3)) /// RESULTADO: 21

# #10
# def addition(b,c):
#     return b+c
#     return 10
# print(addition(3,5))
# RESULTADO: 8, el único return que se ejecuta es el primero

# #11
# b = 500
# print(b)
# def foobar():
#     b = 300
#     print(b)
# print(b)
# foobar()
# print(b)
# RESULTADO: En recorrido imprime b=500, luego vuelve a imprimir b=500 ya que aún no se ha invocado la función. Ahora en la invocación se 
# imprime el nuevo valor de b que es 300. El último print imprime 500 dado que el valor de b no fue devuelto en un return, solo es 
# una llamada temporal.

# #12
# b = 500
# print(b)
# def foobar():
#     b = 300
#     print(b)
#     return b
# print(b)
# foobar()
# print(b)
# RESULTADO: En recorrido imprime b=500, vuelve a imprimir a b=500 dado que aún no se ha invocado la función. Al invocar la función se 
# imprime el valor de b=300, el último print devuelve 500 dado que está llamando a b no la función que es la que tiene el nuevo valor de b

# #13
# b = 500
# print(b)
# def foobar():
#     b = 300
#     print(b)
#     return b
# print(b)
# b=foobar()
# print(b)
# RESULTADO: En recorrido se imprime primero el valor de b=500, luego se imprime de nuevo el valor de b=500, dado que aún no se ha llamado 
# a la función. Ahora sí se le otorga a la variable b un nuevo valor, igual al retur de la función, en este paso al se llamada la función 
# se imprime el valor de b= 300 y en el último print ya se imprime el nuevo valor de b que también es 300

# #14
# def foo():
#     print(1)
#     bar()
#     print(2)
# def bar():
#     print(3)
# foo()
# RESULTADO: En orden deberá imprimir 1, luego ejecutará bar(), por lo que imprime 3 y finalmente imprime 2.


# #15
# def foo():
#     print(1)
#     x = bar()
#     print(x)
#     return 10
# def bar():
#     print(3)
#     return 5
# y = foo()
# print(y)
# RESULTADO: En orden al llamarse foo() se imprime 1, luego al llamarse bar() se imprime 3, se asigna a x el valor del return de bar() 
# que es 5, se imprime x=5, luego y toma el valor del return de foo() y se imprime 10 