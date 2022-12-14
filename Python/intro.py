# -*- coding: utf-8 -*-
"""Intro.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19xXDgyMmF7yCQFIC02KueRwRQp7tl0U6

**Python básico**

# Hello, World!
"""

print("Hello, World!")

"""Acabamos de correr nuestro primer programa. Notar que el programa nos resalta las palabras de distintos colores. *print* es un termino "protegido"  y lo resalta en marrón. El color dependerá del programa que usemos.

# Sangrías (indentation)

Python utiliza la indentación para indicar las partes del código que deben ser ejecutadas juntas. Se admiten tanto tabulaciones como espacios. 

Es fundamental esto para Python. Un loop finaliza cuando se escribe un comando que tiene menor sangría que el anterior.

En este ejercicio se asignará un valor a una variable, comprobará si una comparación es verdadera, y luego - basándose en el resultado - imprimirá. 

(Podrés apretar Ctrl+Enter para que corra el código)
"""

x = 1
if x == 1:
  # Indented  
    print("x is 1")

"""Cualquier término de texto no protegido puede ser una variable. *x* podría haber sido tu nombre. Normalmente nombramos las variables de la forma más descriptiva posible para poder leer algoritmos como el texto (es decir, el código se describe a sí mismo).

---


Usar nombres de variables válidos!

* Los nombres de las variables pueden contener letras, números y guión bajo.
* NO se puede empezar el nombre de una variable con un dígito, o usar las palabras protegidas de Python (ej. False, list, None, zip, else, class, ...).
* NO usar un espacio en el medio del nombre de una variable.
* Case-sensitive


---

# Variables y Tipos de datos

[Data Types](https://drive.google.com/file/d/1tRSMdUwpOnH8AoLceyFPNJ3jenBb8YUw/view?usp=sharing)

Cada variable es un *objeto*.

Tipo de datos
* Números: Integer, Float, Boolean
* Strings (texto)
* Listas
* Tuple
* Array
* Diccionarios
* Set
* File

|Estructura de datos | Propiedades| Sintaxis|
|----|----|----|
|List | Ordenada, secuencia mutable | mylist = [1,2,3] |
|Tuple | Ordenada, secuencia inmutable | mytuple = (1,2,3) |
|Set | Conjunto no ordenado de valores únicos, mutable con elementos inmutables| myset = set([1,2,3]) o myset={1,2,3} |
|Dictionary | Conjunto mutable de pares de valores | mydict = {'first_value':1, 'second_value:2} |

Números
--

2 tipos de números: *integers* y *floats*.
Ojo! al convertir uno al otro
"""

myint = 7
print(myint)

myfloat = 7.0
print(myfloat)
# Convertir a float
myfloat = float(myint)
# `float` es un término protegido
print(myfloat)

# Convertir float a integer
myint = int(7.8)
print(myint)

"""* La división (/) siempre devuelve un número *float*.
* Existe la *floored division* (//) que devuelve un número *float* si alguno de los operandos es *float* o un entero si ambos son enteros.
"""

print(10 / 20)
print(10 / 2)

print(10 // 20)
print(10 // 2)
print(5.0 // 2)

# Conversión implícita
print(5 + 2.0)
# Conversión explícita
print(float(5 + 2))

"""---
Strings
---

Se puede usar comillas simples o dobles. Pero tener cuidado si el texto tiene apóstrofes...
"""

mystring = "Hello, World!"
print(mystring)
mystring = "Let's talk about apostrophes..."
print(mystring)
mystring = 'Let'
print(mystring)

"""También se pueden aplicar operadores simples a sus variables, o asignar múltiples variables simultáneamente."""

one = 1
two = 2
three = one + two
print(three)

hello = "Hello,"
world = "World!"
helloworld = hello + " " + world
print(helloworld)

a, b = 3, 4
print(a, b)

a=3
b=4
n=3*4
print('El producto de', a , 'por' , b , 'es', n)
# f-string
print(f'El producto de {a} por {b} es {n}')

"""Pero mezclar distintos tipos de variables causa problemas."""

#print(one + two + hello)

"""* Añadir variables a un *string* usando `format`: 

`"Variable {}".format(x)` reemplazará el `{}` en el *string* con el valor de la variable `x`.

* Para controlar la cantidad de decimales:

`"Variable {:10.4f}".format(x)` donde `10` es la cantidad de espacio asignado al *float* y `0.4f` es el número de decimales después del punto.
"""

variable = 1/3 * 100
print("Unformated variable: {}%".format(variable))
print("Formatted variable: {:.3f}%".format(variable))
print("Space formatted variable: {:10.1f}%".format(variable))

"""* Built-in functions: 
len(string)

* Built-in methods:
string.upper(), string.lower(), string.capitalize()

Ver más [functions](https://docs.python.org/3.7/library/functions.html) 

Ver más [built-in methods para strings](https://docs.python.org/3/library/stdtypes.html#string-methods)

---
Listas
---
Son una lista **ordenada** y **mutable** de cualquier tipo de variable. Podés combinar tantas variables como quieras, e incluso pueden ser de múltiples tipos. 

Normalmente, a menos que tengas una razón específica para hacerlo, las listas contendrán variables de un sólo tipo.

También puedes iterar sobre una lista (usar cada elemento de una lista en secuencia).

Una lista se coloca entre corchetes: [] y los elementos se separan con comas (,).
"""

mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
# Se puede `llamar' a cada item de la lista directamente. 
# Ojo! Python empieza a contar desde 0.
print(mylist[0])

# El último item de la lista se `llama' usando el -1. 
print(mylist[-1])

# También podés seleccionar un subgrupo de items (slice)
print(mylist[1:3])

# Fundamental para hacer loops usando `for` .
# `x` es una nueva variable que toma el valor de cada item de la lista en orden.
for x in mylist:
    print(x)

# Agregar elementos a lista
a = [1,2,3]

#a += [4,5]
#a += 4,5
#a[len(a):] = [4,5]
#a.extend([4,5])

##Ojo!
#a.append([4,5])
#a[-1:]=[4,5]

print(a)

"""* Comprueba qué tipo de variable es usando `isinstance`
* Usar `.sort()` para ordenar la lista alfabética o numéricamente.
* Obtener el número de elementos de una lista con `len(lista)` ([built-in functions](https://docs.python.org/3.7/library/functions.html)). 
* Obtener el más chico o más grande (número o alfabético): `min(list)` o `max(list)`
* Contar el número de veces que una variable particular aparece en una lista, usando `list.count(x)` (Ver más [built-in methods para listas](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)). 
* Enumera los outcomes de una lista usando `for i, x in enumerate(mylist)` 
* `enumerate` genera un *tuple* con el número de la enumeración que corresponde y lo que querés enumerar
"""

# Imaginemos que tenemos una lista de nombres no ordenados que de alguna manera se incluyeron algunos números al azar.
# Para este ejercicio, queremos imprimir la lista alfabética de nombres sin los números.
# Esta no es la mejor manera de hacer el ejercicio, pero ilustrará un montón de técnicas.
names = ["John", 3234, 2342, 3323, "Eric", 234, "Jessica", 734978234, "Lois", 2384]
print("Number of names in list: {}".format(len(names)))

# Primero eliminamos esos números
new_names = []
for n in names:
    if isinstance(n, str):
        # Si n es string, agregar a la lista
        # Notar la doble sangría
        new_names.append(n)

# Ahora tendríamos que tener sólo nombres en la lista. 
# Ordenémoslos
new_names.sort()
print("Cleaned-up number of names in list: {}".format(len(new_names)))

# Veámoslos, pero enumerándolos.
for i, n in enumerate(new_names):
    # Usar i y n como string
    # Agregar 1 a i porque las listas empiezan en 0.
    print("{}. {}".format(i+1, n))

for ele in enumerate(new_names): 
    print (ele)

"""También existen nested lists:"""

x = [10, [3.141, 20, [30, 'baz', 2.718]], 'foo']
# Para "llamar" la f de 'foo''
print(x[2][0])
print(x[2][-3])
# Para "llamar" a [3.141, 20]
print(x[1][0:2])
# Para eliminar un elemento
x[0:1]=[]
#x.remove(0)
print(x)

del x[1]
print(x)

"""Sets
--
Los conjuntos son listas (mutables) **sin entradas duplicadas**. Probablemente podrías escribir un algoritmo o un diccionario para lograr el mismo fin, pero los conjuntos son más rápidos y flexibles.

**Frozen sets** son inmutables. Pueden ser partes de un set. Pueden ser key de un diccionario.

x = frozenset(['foo', 'bar', 'baz'])
"""

# Extraer todos los componentes únicos de la frase
print(set("the rain is wet and wet is the rain".split()))

"""* Cree un conjunto único de términos con `set`
* Para obtener elementos presentes en ambos conjuntos, usar `set1.intersection(set2)`
* Para obtener los elementro únicos de ambos conjuntos, usar `set1.symmetric_difference(set2)`
* Para obtener los elementos diferentes entre ambos conjuntos use `set1.difference(set2)`
* Para obtener todos los elementos ambas listas, usar `set1.union (set2)`
"""

set_one = set(["Alice", "Carol", "Dan", "Eve", "Heidi"])
set_two = set(["Bob", "Dan", "Eve", "Grace", "Heidi"])

# Intersection (también se puede usar &)
print("Set One intersection: {}".format(set_one.intersection(set_two)))
print("Set Two intersection: {}".format(set_two.intersection(set_one)))
print("Set Two intersection:", set_two & set_one)

# Symmetric difference (también se puede usar ^)
print("Set One symmetric difference: {}".format(set_one.symmetric_difference(set_two)))
print("Set Two symmetric difference: {}".format(set_two.symmetric_difference(set_one)))
print("Set Two symmetric difference:", set_two ^ set_one)

# Difference (también se puede usar -)
print("Set One difference: {}".format(set_one.difference(set_two)))
print("Set Two difference: {}".format(set_two.difference(set_one)))
print("Set Two difference:", set_two - set_one)

# Union (también se puede usar |)
print("Set One union: {}".format(set_one.union(set_two)))
print("Set Two union: {}".format(set_two.union(set_one)))
print("Set Two union:", set_two | set_one)

# Está Bob en el set?
'Bob' in set_one

"""--- 
Diccionarios
---

Los diccionarios son uno de los tipos de datos más útiles y versátiles de Python. Son similares a las matrices, pero consisten en pares clave:valor (key:value). 

Cada valor almacenado en un diccionario **se accede por su clave**, y el valor puede ser cualquier tipo de objeto (string, número, lista, etc.).

Esto permite crear registros estructurados. 

**Los diccionarios se colocan entre {}. También se pueden definir usando:
dictionary_name=dict()**

Las *keys* de los diccionarios pueden ser cualquier objeto de tipo inmutable: string, built-in function (len), número, tuple (). **NO** puede ser una lista [] u otro diccionario dict().
"""

phonebook = {}
phonebook["John"] = {"Phone": "012 794 794",
                     "Email": "john@email.com"}
phonebook["Jill"] = {"Phone": "012 345 345",
                     "Email": "jill@email.com"}
phonebook["Joss"] = {"Phone": "012 321 321",
                     "Email": "joss@email.com"}
print(phonebook)

"""Tengan en cuenta que pueden anidar diccionarios y listas. Lo anterior muestra cómo puede agregar valores a un diccionario existente o crear diccionarios con valores.

Podes iterar sobre un diccionario como si fuera una lista, usando `.items()`.
"""

for name, record in phonebook.items():
    print("{}'s phone number is {}, and their email is {}".format(name, record["Phone"], record["Email"]))

"""Eliminar registros con `del` o `pop`. Estos son statements.

También se puede borrar con **methods**: d.pop()
"""

# `del`
del phonebook["John"]
for name, record in phonebook.items():
    print("{}'s phone number is {}, and their email is {}".format(name, record["Phone"], record["Email"]))

# `pop` te muestra el registro y después lo borra
jill_record = phonebook.pop("Jill")
print(jill_record)

for name, record in phonebook.items():
    # You can see that only Joss is still left in the system
    print("{}'s phone number is {}, and their email is {}".format(name, record["Phone"], record["Email"]))

# Si no existe, ERROR!
#del phonebook["John"]

# Quiero el teléfono de Joss
phonebook["Joss"]["Phone"]

"""Una cosa que hay que acostumbrarse a hacer, es probar las variables antes de asumir que tienen las características que estás buscando. Puedes probar en un diccionario para ver si tiene un registro, y pedir que te devuelva cierta respuesta por defecto si no lo tiene.

Esto se hace con `.get("key", default)`. 

`default` puede ser cualquier cosa, incluyendo otra variable. 

Si dejas en blanco el valor `default` (es decir, sólo `.get("key")`), el resultado será automáticamente `False` si no hay ningún registro.
"""

# False and True 
jill_record = phonebook.get("Jill", False)
if jill_record: 
    print("Jill's phone number is {}, and their email is {}".format(jill_record["Phone"], jill_record["Email"]))
else: # si es False
    print("No record found.")

"""# Operaciones básicas

---
Operadores aritméticos
---

Aritmética básica: 

| Símbolo | Función |
|----|---|
| +  | suma |
| -  | resta |
| /  | división |
| *  | multiplicación |
| **  | potencia |
| %  | devuelve el resto de una división |
| += | sumar y asignar (ej. a=+3 es lo mismo que a=a+3) |
"""

number = 1 +2 * 3 // 4
print(number)

remainder = 11 % 3
print(remainder)

squared = 7 ** 2
print(squared)

cubed = 2 ** 3
print(cubed)

"""---
List operators
---
"""

even_numbers = [2, 4, 6, 8]
uneven_numbers = [1, 3, 5, 7]
all_numbers = uneven_numbers + even_numbers

# Concatenar
print(all_numbers)

# Para ordenar 
all_numbers.sort()
print(all_numbers)

# También se puede armar una secuencia repetida
print([1, 2 , 3] * 3)

"""---
Operadores de texto
---
"""

# Concatenación de strings
helloworld = "Hello," + " " + "World!"
print(helloworld)

# Repetir secuencia
manyhellos = "Hello " * 10
print(manyhellos)

# No se puede hacer cualquier cosa...
#nohellos = "Hello " / 10
#print(nohellos)

"""* Obtenga el índice (ubicación) para la primera aparición de una letra específica con `string.index("l")` donde `l` es la letra que está buscando
* Como en las listas, cuente el número de apariciones de una letra específica con `string.count("l")`
* Obtenga segmentos de cadenas con `string[start:end]`, p. `string[3:7]`. Si no estás seguro del final de la *string*, podés usar números negativos para contar desde el final, p. `string [:-3]` para obtener un corte del primer carácter al tercero desde el final.
* También podés "saltar" a través de una cadena con `string[start:stop:step]`, ej. `string[2:6:2]` que omitirá un carácter entre los caracteres 2 y 5 (es decir, 6 es el límite).
* Podés usar un "step" negativo para invertir el orden de los caracteres, ej `string[::-1]`
* Podés convertir cadenas a mayúsculas o minúsculas con `string.upper()` y `string.lower()`
* Podés probar si una cadena comienza o termina con una subcadena con:
`string.startswith(substring)` o `string.endswith(substring)` que devuelve `True` o `False`
* Usá `in` para probar si una cadena contiene una subcadena, por lo que `substring in string` devolverá `True` o` False`
* Podés dividir una cadena en una lista genuina con `.split(s)` donde `s` es el carácter específico que se utilizará para dividir, ej `s = ","` o `s = " "`. Esto podría ser útil para dividir texto que contiene datos numéricos.
"""

a_string = "Hello, World!"
# Cuenta los espacios también
print("String length: {}".format(len(a_string)))

# Recordá que Python cuenta desde 0.

# Observá que hay ' dentro de "".

print("Index for first 'o': {}".format(a_string.index("o")))
print("Count of 'o': {}".format(a_string.count("o")))
print("Count of 'o' between character 4 and 8: {}".format(a_string.count("o",4,8)))
print("Count of 'o' from character 3 on: {}".format(a_string.count("o",4)))
print("Slicing between second and fifth characters: {}".format(a_string[2:6]))
print("Skipping between 3rd and 2nd-from-last characters: {}".format(a_string[3:-2:2]))
print("Reverse text: {}".format(a_string[::-1]))
print("Starts with 'Hello': {}".format(a_string.startswith("Hello")))
print("Ends with 'Hello': {}".format(a_string.endswith("Hello")))
print("Contains 'Goodbye': {}".format("Goodbye" in a_string))
print("Split the string: {}".format(a_string.split(" ")))
print("Does not split the string: {}".format(', '.join(a_string.split(", ")))) # son complementarios
print("Does not split the string: {}".format(a_string.strip(", "))) # solo si ", " está al principio o al final
print("Returns the same string: {}".format(a_string.upper().lower())) # son complementarios

"""---
Condiciones
---
Operadores `booleanos`:
* equal: `==`
* not equal: `!=`
* greater-than: `>`
* less-than: `<`

A esa lista de operadores booleanos se añade un nuevo conjunto de comparaciones: `and`, `or` and `in`.

`if`, `else`, `elif` son ejemplos de *control structures*, las cuales determinan qué comandos se ejecutan y en qué orden, permitiendo que algunos se salteen y otros que se repitan.
"""

# Simple boolean tests
x = 2
print(x == 2)
print(x == 3)
print(x < 3)

# Using `and`
name = "John"
print(name == "John" and x == 2)

# Using `or`
print(name == "John" or name == "Jill")

# Using `in` on lists
print(name in ["John", "Jill", "Jess"])

"""Podés usar `if`, `elif` y otros.

Recordá que el código debe estar correctamente indentado o tendrá un comportamiento inesperado.
"""

x = 2
y = 10
if x > 2:
    print("x > 2")
elif x < 10 or y > 50:
    print("x < 10 or y > 50")
elif x == 2 and y > 0:
    print("x == 2 and y > 50")
else:
    print("Nothing worked.")

# Se puede escribir separando con ;
x = 2
y = 10
if x < 10 or y > 50: print("x < 10 or y > 50")

"""* `not` se usa para obtener lo contrario de una prueba booleana particular: `not(False)` devuelve `True`
* `is` parecería, superficialmente, similar a` ==`, pero **comprueba si los objetos reales son los mismos, no si los valores que reflejan los objetos son iguales.**
"""

# Using `not`
name_list1 = ["John", "Jill"]
name_list2 = ["John", "Jill"]
print(not(name_list1 == name_list2))

# Using `is`
name2 = "John"
print(name_list1 == name_list2)

print(name_list1 is name_list2)

print(name_list1 is name_list1)

"""---
Truthy & Falsy
---

**Falsy Values**
* Empty lists []
* Empty tuples ()
* Empty dictionaries {}
* Empty sets set()
* Empty strings " "
* Empty ranges range(0)
* Integer: 0
* Float: 0.0
* `None`
* `False`

Podemos hacer la condición mucho más concisa usando `trusty`. Si la lista está vacía, los datos se evaluarán como `False`. Si no está vacía, se evaluará a `True`. Obtenemos la misma funcionalidad con un código más conciso.
"""

my_list=[1,2]

if len(my_list) != 0:
   print("Not empty!")

# Más conciso
if my_list:
   print("Not empty!")

# Otro ejemplo
a = 5
if a:
	print(a)
 
a = 0
if a:
	print(a)

"""# Loops

* Para *loops*, `for`, recorre una lista. 

**Otros tipos de loops:**
* `enumerate` en *lists* que te permite contar el número de "vuelta"
* *Range* crea una lista de números enteros para recorrer, `range(start, stop)` crea una lista de enteros entre start y stop, o `range(num)` crea una lista de cero hasta num, o `range (start, stop, step)` recorre una lista en incrementos de a "step".

* `while`, se ejecuta mientras una condición particular es` True`. 

* `while` es una declaración condicional (requiere una prueba para devolver `True`), eso significa que podemos usar `else` en un `while` (pero no `for`)
"""

# For
for i, x in enumerate(range(2, 8, 2)):
    print("{}. Range {}".format(i+1, x))

# While 
count = 0
while count < 5:
    print(count)
    count += 1 # Recordar que ya vimos esto
else:
    print("End of while loop reached")

# Ojo con las sangrías

"""* `break` finaliza un ` while` o `for` inmediatamente
* `continue` omite el loop actual y vuelve al loop condicional
* `pass` significa que no hay nada que mostrar
"""

# Break and while conditional
print("Break and while conditional")
count = 0
while True:
    # Esto correría para siempre a menos que pongamos el break
    print(count)
    count += 1
    if count >= 5:
        break

# Continue
print("Continue")
for x in range(8):
    # Check si x es par
    if (x+1) % 2 == 0:
        continue
    print(x)

# Pass
print("Pass")
for x in range(8):
    # Check si x es par
    if (x+1) % 2 == 0:
        pass
    print(x)

"""# List comprehensions

Una de las tareas comunes en la codificación es revisar una lista de elementos, editar o aplicar algún tipo de algoritmo y devolver una nueva lista.

Escribir largos tramos de código para lograr esto es tedioso y lleva mucho tiempo. La comprensión de la lista es una manera eficiente y concisa de lograr exactamente eso.

Como ejemplo, imaginemos que tenemos una frase en la que queremos contar la longitud de cada palabra, pero nos saltamos todas las "las":
"""

sentence = "for the song and the sword are birthrights sold to an usurer, but I am the last lone highwayman and I am the last adventurer"
words = sentence.split()
word_lengths = []
for word in words:
      if word != "the":
          word_lengths.append(len(word))
print(word_lengths)

# Usando una list comprehension
sentence = "for the song and the sword are birthrights sold to an usurer, but I am the last lone highwayman and I am the last adventurer"
word_lengths = [len(word) for word in sentence.split(" ") if word != "the"]
print(word_lengths)