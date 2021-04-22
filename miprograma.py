# Hacer un programa en el que:
# 1-Se pregunte por el nombre de la persona
# 2-Se pregunte por el apellido de la persona
# 3-Se pregunte por la edad de la persona.
# El formato de salida debe ser:
# "Su nombre es: " + nombre + apellido + "y usted es " {condición de edad}
# La condición de edad es:
# 1. Si es menor de 18 escribir menor
# 2. Si tiene entre 18 y 65 escribir mayor
# 3. Si tiene entre 65 y 120 escribir jubilado
# 4. Si tiene más escribir cadaver

#apellido = input('Ingrese su apellido: ')

clientes = int(input('Ingrese numero de clientes: '))

for i in range (clientes):
    edad = int(input('Ingrese su edad: '))
    if edad < 18:
        condicion = 'menor'
    elif edad < 65:
        condicion = 'mayor'
    elif edad <= 120:
        condicion = 'jubilado'
    else:
        condicion = 'cadaver'
    print (condicion)
    break
#print('Su nombre es: ' + nombre + ' ' + apellido + ' y usted es: ' + condicion)
