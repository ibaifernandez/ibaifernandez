# en_python_se_escribe_en_snake_case

# Declaración de variables

# Sin palabras clave tipo 'const', 'var' o 'let'
name = "Ibai" # Strings entre comillas
age = 37 # Integers
is_active = True # Booleanos con mayúsculas

# función 'print' para mostrar en consola
print(name)
print(age)
print(is_active)

# Función 'type()' para mostrar el tipo de dato

print(type(name))
print(type(age))
print(type(is_active))

juan = {                # Los objetos de Python se llaman diccionarios
    "name": "Juan",     # Las propiedades siempren van entre comillas 
    "age": 27,          # Cada "key-value pair" se separa por comas
    "dimensions": {     # Un diccionario puede llevar diccionarios dentro
        "mass": 87,
        "height": 183
    } 
}

print(juan) # Devuelve {'name': 'Juan', 'age': 27, 'dimensions': {'mass': 87, 'height': 183}}

print(juan['name']) # Devuelve 'Juan'
print(juan['dimensions']['mass']) # Devuelve 87

# Arrays hay de dos clases: listas y duplas

# Listas

frutas = ['uva', 'manzana', 'pera']

print(frutas) # Devuelve ['uva', 'manzana', 'pera']
print(frutas[0]) # Devuelve uva
print(frutas[1]) # Devuelve manzana
print(frutas[2]) # Devuelve pera

frutas.append('papaya') # .append() funcion como el .push() de JS
print(frutas) # Devuelve ['uva', 'manzana', 'pera', 'papaya']

# .length() de JS es sustituido por la función len()

print(len(frutas)) # Devuelve 4

frutas[0] = "limón"

print(frutas) # Devuelve ['limón', 'manzana', 'pera', 'papaya']

# Tuplas

numeros = ("uno", "dos", "tres")

print(numeros) # Devuelve ('uno', 'dos', 'tres')
print(numeros[0]) # Devuleve "uno"
print(len(numeros)) # Devuelve 3

# La principal diferencia entre listas y tuplas es que las primeras son mutables y las segundas no.

# Por tanto, por ejemplo, numeros[0] = "cuatro" # No funciona con tuplas


# Las variables siempre han de ser de un tipo, pero existen funciones para convertir un tipo de dato en otro; estas son: str(), int(), list(), dict(), float()

x = 7
y = "10"
# print(x+y)        # Devuelve
                    # Traceback (most recent call last):
                    # File "<string>", line 75, in <module>
                    # TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(x+int(y))     # Devuelve 17

#input funciona como el prompt() de JS; es decir, llega como string. Por tanto, 15 horas a segundos se calcularía:

input = 15
print(int(input)*60*60)

muebles = [{'name':'silla'},{'name':'mesa'},{'name': 'banco'}]

mis_muebles = map(lambda mueble: mueble['name'], muebles)
print(list(mis_muebles))

# Funciones

# name = 'Ibai'
# age = 21

# Palabra clave 'def'

# def saludar(name):
#     print ("¡Hola, " + name + "!")
# saludar(name) # Devuelve "¡Hola, Ibai!"

# String Literals

# def saludar(name):
#   print ("¡Hola, {}!".format(name))
# saludar("Jaime") # Devuelve "¡Hola, Ibai!"

# def decir_hola(name, age):
#     print("¡Hola, {name}! Tienes {age} años.".format(name, age))
# decir_hola(name,age)

# def saludar(name,age):
#     print("¡Hola, {}! ¡Tienes {} años!".format(name,age))
# saludar(name,age)

frutas = ['uva', 'pera', 'manzana']
for fruta in frutas:
    print(fruta)
    
# Condicionales y operadores lógicos (and, or, not)

# Condicional simple

if 7 > 5:
    print("¡Cierto!")
    
# Condicional compuesta

if 7 > 5 and 6 < 12:
    print("¡Correcto!")
    
# Función con condicional compuesta (and) y 'else'

def condicional1(num1,num2,num3,num4):
    if num1 < num2 and num3 > num4:
        print("Oh, yeah!")
    else:
        print("Whatever,man!")
        
condicional1(1,2,3,4)
condicional1(1,2,4,3)

# Función con condicional conmpuesta (or) y 'else'

def condicional2(num1,num2,num3,num4):
    if num1 < num2 or num3 > num4:
        print("Oh, yeah!")
    else:
        print("Whatever,man!")
        
condicional2(1,2,3,4)
condicional2(1,2,4,3)

# Función con condicional negativa (not) y 'else'

def condicional3(num1):
    if not num1 < 25:
        print("Oh, yeah!")
    else:
        print("Whatever,man!")
        
condicional3(24)
condicional3(26)

# Función con condicional simple, 'elif' y 'else'

def condicional4(num1):
    if num1 < 12:
        print("Oh, yeah!")
    elif num1 < 25:
        print("Whatever,man!")
    else:
        print("Nanay!")
        
condicional4(11)
condicional4(24)
condicional4(36)

# Clases

class Person:                           # Se define la clase (Pascalcase)
    def __init__(self, name, age):      # Se define la función constructora
                                        # con dos guiones bajos por cada
                                        # lado. Se le pasa el argumento
                                        # 'self' por defecto y tantos 
                                        # argumentos como quieras ver en la
                                        # 'instanciación' que 
                                        # posteriormente se haga de esta 
                                        # clase.
        self.name = name                # Igualamos argumentos
        self.age = age
    def serialize(self):                # Python exige que se defina un
                                        # método que, tomando 'self' como
                                        # argumento
        return {                        # devuelva (return) un objeto ({})
            "name":self.name,           # con la propiedad 'name'
            "age":self.age              # y la propiedad 'age'
        }
        
juan = Person("Juan", 22)               # Creamos la variable 'Juan'
                                        # instanciando desde la clase
                                        # 'Person' con los argumentos
                                        # "Juan" y 22

print(juan.serialize())                 # Imprimimos la variable juan
                                        # aplicando el método .serialize()