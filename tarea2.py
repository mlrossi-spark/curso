# 1. Crear un nuevo repositorio
# 2. Tomar de base el programa de la clase pasada
# 3. Vamos a modificar el programa para que solo tome como válidos números entre 1 y 120 (si pone un número entre -inf y 0 o 121 a inf debe volver a preguntar)
# 4. Al inicio del programa preguntar cuantas personas registrar
# 5. Hacer que el programa que se hizo se ejecute esas n veces que se pusieron en el punto 4
# 6. Subir el programa al repositorio creado.

n = int(input('Ingrese  la cantidad de registros: '))

for i in range(n):
    nombre = input('Ingrese su nombre: ')
    apellido = input('Ingrese su apellido: ')

    edad = 0
    while edad<1 or edad>120:
        edad = int(input('Ingrese su edad: '))

    if edad < 18:
        condicion = 'menor'
    elif edad < 65:
        condicion = 'mayor'
    else:
        condicion = 'jubilado'

    print('Su nombre es: ' + nombre + ' ' + apellido + ' y usted es: ' + condicion)
