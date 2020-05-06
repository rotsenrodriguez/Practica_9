#esto es un comentario de una sola linea
"""
Esto es un comentario de varias
líneas
"""

print("Hola Mundo")
x = 10
print(type(x))
print(x)
x = y =z = 2.3
print(x, y, z )
print(type(x))
x = "cadena"
print(x)
print(type(x))
"""
Concatenar 1
"""
c1= "hola"
c2= "Nestor"
saludo = c1 +" "+ c2
print(saludo)
"""
Concatenar 2
"""
saludo2 = "{} {} {}".format(c1, c2, 3)
print(saludo2)

saludo3 = "Cambio de orden {1} {2} {0}".format(c1, c2, 4)
print(saludo3)