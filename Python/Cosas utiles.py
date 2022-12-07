#PYTHON

###------- VISUAL STUDIO CODE -------###

# KEYBOARD SHORTCUTS

# Guardar la imagen del workspace para poder volver a abrir los mismos archivos que en tu ultima sesion>
file -> Add folder to workspace -> Save Workspace As

# Habilitar la opcion de buscar y reemplazar en una seleccion (find and replace in selection) en Visual Studio Code:
desgargar extension Quick Replace In Selection

# Seleccionar varias lineas al mismo tiempo:
alt+shift

# Wrap text (que el texto se ajuste al tamaño de la ventana):
alt+z

# Seleccionar una palabra y luego seleccionar todas las repeticiones de esa palabra
ctrl + d

# Mostrar/visualizar la base de datos completa con todas las columnas (para ver en Visual Studio Code u otros):
pd.set_option('display.max_columns', None)
pd.set_option('max_row', None) #esta otra no sé qué hace


###----------------------------------###

###------- USEFUL COMMANDS -------###

# Transform years into decades
import numpy as np
(np.floor(df['year']/10)*10).astype(np.int64)

## METODOS DE STRINGS
# Reemplazar una parte de un string por otra
saludo = 'hola'
print(saludo.replace('la', 'mbre'))

# Cambiar todo a mayuscula
place = "poolhouse"
print(place.upper())

# Cambiar la primera letra a mayuscula
print('hola'.capitalize())

## METODOS DE LISTAS
# Contar la cantidad de veces que aparece un elemento en una lista
lista1 = [1,2,3,4,1,1]
print(lista1.count(1))

# Obtener el indice de un objeto dentro de una lista / obtener la posicion de un elemento en una lista
lista1 = [1,2,3,4]
print(lista1.index(3))

# The ; sign is used to place commands on the same line. The following two code chunks are equivalent:
# Same line
print('Hello'); print('Bye')

# Separate lines
print('Hello')
print('Bye')

# Copiar objetos (listas)
lista1 = [1,2,3,4]
lista2 = lista1 # aca estas copiando la referencia a la lista1, no los objetos
del[lista2[2]]
print(lista1)
    # Para copiar los elementos, y no solo la referencia, hay que escribir
y = list[lista1]
# o
y = x[:]

# Eliminar un elemento de una lista
lista1 = [1,2,3,4]
del[lista1[2]]
print(lista1)

# Appendear / Agregar filas de otro data frame que no esten en el data frame actual
df_diff = df2[~df2.col1.isin(A.col1)]
df_full = pd.concat([df1, df_diff], ignore_index=True)

# Crear un archivo csv / Exportar un data frame a csv
df.to_csv("path")

# Cambiar el nombre de muchas columnas a la vez
cambio_cols = {'v1old': 'v1new', 'v2old': 'v2new'}
df.rename(columns=cambio_cols,
          inplace=True)

# Crear una variable fecha a partir de variables para anio mes y dia:
df['fecha'] = pd.to_datetime(dict(year=df.anio, month=df.mes, day=1)) # aca no tengo dia y le pongo 1

# Crear una columna / crear una variable en un data frame que tome diferentes valores de acuerdo una condicion
db['var'] = np.where(db['var2']=='valor', valorsitrue, valorsifalse)

# Crear una columna / crear una variable en un data frame que tome diferentes valores de acuerdo mas de una condicion
df = pd.DataFrame({'Type':list('ABBC'), 'Set':list('ZZXY')})
conditions = [
    (df['Set'] == 'Z') & (df['Type'] == 'A'),
    (df['Set'] == 'Z') & (df['Type'] == 'B'),
    (df['Type'] == 'B')]
choices = ['yellow', 'blue', 'purple']
df['color'] = np.select(conditions, choices, default='black')
print(df)

# Crear una columna variable con un promedio ponderado por grupo:
func_prom_pond = lambda x: np.average(x, weights=db.loc[x.index, "pesos"])
db['prom_pond'] = db4.groupby('grupo')['variable'].transform(func_prom_pond)

# Crear una muestra aleatorio de una secuencia
random.sample(range(1, 11), k=5)

# Generar una muestra aleatoria de un data frame
db.sample(n=1000, replace=False)

# Seleccionar las filas de un data frame que tengan missing value en una columna
df[df['var'].isnull()]

# Eliminar duplicados segun una variable:
df.drop_duplicates(subset=['var'])

# Merge / unir dos data frames
db1 = db1.merge(db2[['var_a_mergear']] how='left', on=[nombre de variable llave], indicator=True) #indicator te dice si agregar una columma que te diga el resultado del merge, ademas de true se le puede poner el strign que quieras

# Intertar una columna / variable al principio de un data frame
df.insert(0, 'nombrevar', var)

# Cambiar la posicion de una columna en un data frame (aca se pone en la posicion 0, al principio)
col = df.pop('Name')
df.insert(0, 'Name', col)

# Eliminar todos los objetos creados por el usuario:
for element in dir():
    if element[0:2] != "__":
        del globals()[element] # VERR PORQUE GENERA PROBLEMAS

# Seleccionar los elementos de una lsita que empiecen con determinado string:
result = [i for i in some_list if i.startswith('string')]

# Quedarse con / seleccionar las columnas de un tipo / clase determinado:
df.select_dtypes(np.number) # u otra clase, no probe con otra

# Convertir todas las columnas & variables a una clase determinada
def f(x):
    try:
        return x.astype(float) # o cualquier otra clase
    except:
        return x
df2 = df.apply(f)

# Quedarse con la primera fila de cada grupo
db.grouby('var').first()

# Ordenar un data frame segun multiples columnas:
df.sort_values(['var1', 'var2'], ascending=[False, True])

# Exportar un grafico a png o pdf o jpg:
import matplotlib as plt

# Calcular media / promedio por grupo:
db.groupby('variable', as_index=False).mean()
# y agregarlo como columna>
db['nueava_var'] = db0.groupby('var_grupo')['var_a_promediar'].transform('mean')

### Hacer graficos de carrera de barras:
# Primero hay que bajarse un programa para manejar videos que ese llama ffmpeg, unzipearlo en una carpeta tipo C o Program files, y agregarlo al path. Usar este tutorial:
http://blog.gregzaal.com/how-to-install-ffmpeg-on-windows/
# Despues instalar el paquete de python para ese progrma en el cmd:
pip install ffmpeg-python
# Se puede chequear si se hizo bien poniendo en el cmd:
ffmpeg -version
# Instalar el paquete para hacer graficos de carreras en el cmd:
pip install bar_chart_race
# Ejemplo de como se usa:
# es importante que la base este en formato wide. Ver tutorial: https://www.dunderdata.com/blog/official-release-of-bar_chart_race-a-python-package-for-creating-animated-bar-chart-races
bcr.bar_chart_race(
    df = db2,
    filename = path_figures +  'carrera_1.mp4')

# Actualizar un paquete con pip. En cmd escribir:
pip install paquete --upgrade

# Contar los missing values de todas las columnas de un data frame:
print(df.isnull().sum())

# Eliminar la ultima fila o la primer fila de un data frame:
df.drop(df.tail(n).index,inplace=True) # drop last n rows
df.drop(df.head(n).index,inplace=True) # drop first n rows

# Eliminar la ultima columna de un data frame:
df.drop(df.columns[[-1,]], axis=1, inplace=True)

# Separar una cadena por un character:
texto.split(',') #en este caso es una coma
objeto.text.split('\n') #acá es si el objeto no es texto, primero lo pasás a texto

# Separar una cadena por comas, ignorando las comas entre comillas "":
funcion = re.compile(r",(?=(?:[^\"']*[\"'][^\"']*[\"'])*[^\"']*$)")
funcion.split(objeto)

# Equivalente al comando "fillin" de Stata
import itertools
cols_a_combinar = ["var1", "var2", "var3"]
combinaciones = []
for var in cols_a_combinar:
    combinaciones.append(db[var].unique().tolist())
df1 = pd.DataFrame(columns = cols_a_combinar, data=list(itertools.product(*combinaciones)))
#df1


# Convertir un array (series) a una lista:
array.tolist()

# Obtener los valores únicos de una columna/variable:
db["variable"].unique()
#Si querés que sea una lista:
db["variable"].unique().tolist()

# Factorizar/Encodear una variable (asignarle a cada valor único de string un número):
pd.factorize(db['variable'])

# Cread dummies para diferentes valores de una misma variable (en realidad se dice "one-hot" encoding, dummies seria si dejas una categoria afuera, como en una regresión):           
pd.get_dummies(df, columns=["variable"])

# Eliminar todas las variables que empiezan con determinado string:
db = db.drop(db.filter(like='stringinicial').columns, axis=1)

# Eliminar una lista de columnas / variables a la vez:
eliminar = ['var1', 'var2']
db.drop(eliminar, axis=1, inplace=True)

# Tabular una variable:
db.groupby(['variable']).size()
#mejor:
db.variable.value_counts()

# Tabular una variable y quedarse con los procentajes de cada grupo:
db.groupby(['var1', 'var2'])['var3'].agg('count') / db['var3'].agg('count')

# Traductor de Stata a Python
http://www.danielmsullivan.com/pages/tutorial_stata_to_python.html

# Seleccionar / ver determinadas columnas de un data frame segun su posicion: (ej. ultimas 10 columnas)
df.iloc[:,-10:]

# Unir elementos/string/cadenas de una lista (o cualquier otro string/cadena) con un string:
" ".join(item for item in lista)

# Seleccionar / ver determinadas columnas de un data frame según su nombre:
db[['var1', 'var2']]

# Seleccionar filas de acuerdo al valor de una columa
db.loc[db['variable']==valor]

# Seleccionar filas de acuerdo a varios valores de una misma columna:
db[ db['variable'].isin(['valor1', 'valor2', 'valor3']) ]

#Abrir un CSV como dataframe con Pandas
import pandas as pd
df = pd.read_csv('archivo.csv')

#Cambiar un número de entero a no entero:
variable = float(variableentera)

#Convertir de no entero a entero
variable = int(variablefloat)

#Floored division: hace una división y te devuelve un núm entero si los dos son enteros y sino n float:
5//2

#OJO CON LA TOLERANCIA. A veces le preguntas si x==2.5 pero en realidad es 2.50000, o una movida así con el tema de los floats y pedirle enteros

#Hacer una lista:
nombrelista = [ ]
#(si le pones parentesis es un tupple, es inmutable)

#Llamar a un elemento de la lista (ojo que empieza desde la posición cero)
print(nombrelista[0])
#Para pedir el último valor ponés -1

#Llamar un subgrupo de la lista:
print(nombrelista[2:4])
#Ojo que el último (posición 4) no lo agarra

#Agregar un elemento a la lista: 
nombrelista.append(29)

# Loopear según el nombre de las variables (ej con un sufijo de tiempo) (aca las puse en una lista:
var1=1
var2=13
var3=-5
lista = []
for i in range(1,4):
    lista.append( eval("var"+str(i)) )
lista

#Un loop: agarrar elemento por elemento y mostrarlo:
for x in mylist:
    print(x)

#Un loop: agregar elementos a la lista, acá agrega el 4 y el 5
a = [1,2,3]
a += [4,5] 
#(o sin corchetes)

# Loopear por numeros:
for i in range(2,10,2): #inicio, fin, salto
    ...

#Quedarte con los strings de una lista:
    
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

#Eliminar un (dos) elemento de la lista:
lista[0:2]=[ ]



#######################################
############# CURSO UNSAM #############
#######################################

#OPERACIONES BÁSICAS:

#La potencia es con **

#Sumar y asignar: += . Lo que hace es sumarle tres a la variable y sobreescribirla con el resultado.



#Definir una funcion:
def say_hello()
	print(‘Hello, World’)
#ejemplo:
def calificar(sujeto, adjetivo):
        print("{} es {}".format(sujeto, adjetivo))
calificar ("Juan", "capo")

#Testear si funciona la función:
print(callable(say_hello) 	y tendría que salir true


return 
#es como una función que devuelve un valor. Este valor a menudo no es visto por el usuario humano, pero puede ser usado por la computadora en otras funciones.
#Ej:
def add_three(num):
    return num + 3

 
#%%CURSO UNSAM
#Usá el guión bajo (underscore, _) para referirte al resultado del último cálculo.

#Ejecutar en una terminal de Windows:
C:\SomeFolder>hello.py
hello world

C:\SomeFolder>c:\python36\python hello.py
hello world

#A veces es conveniente especificar un bloque de código que no haga nada. El comando pass se usa para eso.
if a > b:
    pass
else:
    print('No ganó a')

x + y      #Suma
x - y      #Resta
x * y      #Multiplicación
x / y      #División (da un float, no un int)
x // y     #División entera (da un int)
x % y      #Módulo (resto)
x ** y     #Potencia
abs(x)     #Valor absoluto


x << n     #Desplazamiento de los bits a la izquierda
x >> n     #Desplazamiento de los bits a la derecha
x & y      #AND bit a bit.
x | y      #OR bit a bit.
x ^ y      #XOR bit a bit.
~x         #NOT bit a bit.

import math
a = math.sqrt(x)
b = math.sin(x)
c = math.cos(x)
d = math.tan(x)
e = math.log(x)

x < y      #Menor que
x <= y     #Menor o igual que
x > y      #Mayor que
x >= y     #Mayor o igual que
x == y     #Igual a
x != y     #No igual a

#Con esto en mente, ¿podrías explicar el siguiente comportamiento?
>>> bool("False")
True
>>>

#Normalmente las cadenas de caracteres solo ocupan una linea. Las comillas triples nos permiten capturar todo el texto encerrado a lo largo de múltiples lineas:
# Comillas triples
c = '''
Yo no tengo en el amor
Quien me venga con querellas;
Como esas aves tan bellas
Que saltan de rama en rama
Yo hago en el trébol mi cama
Y me cubren las estrellas.
'''

#Código de escape
#Los códigos de escape (escape codes) son expresiones que comienzan con una barra invertida, \ y se usan para representar caracteres que no pueden ser fácilmente tipeados directamente con el teclado. Estos son algunos códigos de escape usuales:
'\n'      #Avanzar una línea
'\r'      #Retorno de carro El retorno de carro (código '\r') mueve el cursor al comienzo de la línea pero sin avanzar una línea. El origen de su nombre está relacionado con las máquinas de escribir.
'\t'      #Tabulador
'\''      #Comilla literal
'\"'      #Comilla doble literal
'\\'      #Barra invertida literal

#Indexación de cadenas
#Las cadenas funcionan como los vectores multidimensionales en matemática, permitiendo el acceso a los caracteres individuales. El índice comienza a contar en cero. Los índices negativos se usan para especificar una posición respecto al final de la cadena.
a = 'Hello world'
b = a[0]          # 'H'
c = a[4]          # 'o'
d = a[-1]         # 'd' (fin de cadena)
También se puede rebanar (slice) o seleccionar subcadenas especificando un range de índices con :.
d = a[:5]     # 'Hello'
e = a[6:]     # 'world'
f = a[3:8]    # 'lo wo'
g = a[-5:]    # 'world'

Operaciones con cadenas
Concatenación, longitud, pertenencia y replicación.
# Concatenación (+)
a = 'Hello' + 'World'   # 'HelloWorld'
b = 'Say ' + a          # 'Say HelloWorld'

# Longitud (len)
s = 'Hello'
len(s)                  # 5

# Test de pertenencia (in, not in)
t = 'e' in s            # True
f = 'x' in s            # False
g = 'hi' not in s       # True

# Replicación (s * n)
rep = s * 5             # 'HelloHelloHelloHelloHello'

#Métodos de las cadenas
#Las cadenas en Python tienen métodos que realizan diversas operaciones con este tipo de datos.
#Ejemplo: sacar (strip) los espacios en blanco sobrantes al inicio o al final de una cadena.
s = '  Hello '
t = s.strip()     # 'Hello'
#Ejemplo: Conversión entre mayúsculas y minúsculas.
s = 'Hello'
l = s.lower()     # 'hello'
u = s.upper()     # 'HELLO'
#Ejemplo: Reemplazo de texto.
s = 'Hello world'
t = s.replace('Hello' , 'Hallo')   # 'Hallo world'

#Más métodos de cadenas:
#Los strings (cadenas) ofrecen una amplia variedad de métodos para testear y manipular textos. Estos son algunos de los métodos:
s.endswith(suffix)     # Verifica si termina con el sufijo
s.find(t)              # Primera aparición de t en s (o -1 si no está)
s.index(t)             # Primera aparición de t en s (error si no está)
s.isalpha()            # Verifica si los caracteres son alfabéticos
s.isdigit()            # Verifica si los caracteres son numéricos
s.islower()            # Verifica si los caracteres son minúsculas
s.isupper()            # Verifica si los caracteres son mayúsculas
s.join(slist)          # Une una lista de cadenas usando s como delimitador
s.lower()              # Convertir a minúsculas
s.replace(old,new)     # Reemplaza texto
s.split([delim])       # Parte la cadena en subcadenas
s.startswith(prefix)   # Verifica si comienza con un sufijo
s.strip()              # Elimina espacios en blanco al inicio o al final
s.upper()              # Convierte a mayúsculas

#Los strings son "inmutables" o de sólo lectura. Una vez creados, su valor no puede ser cambiado. Esto implica que las operaciones y métodos que manipulan cadenas deben crear nuevas cadenas para almacenar su resultado.

#Ejercicio 1.16: Testeo de pertenencia (test de subcadena)¶
#Experimentá con el operador in para buscar subcadenas. En el intérprete interactivo probá estas operaciones:
>>> 'Naranja' in frutas
?
>>> 'nana' in frutas
True
>>> 'Lima' in frutas
?
>>>
#Ejercicio 1.21: Expresiones regulares
#Una limitación de las operaciones básicas de cadenas es que no ofrecen ningún tipo de transformación usando patrones más sofisticados. Para eso vas a tener que usar el módulo re de Python y aprender a usar expresiones regulares. El manejo de estas expresiones es un tema en sí mismo. A continuación presentamos un corto ejemplo:
>>> texto = 'Hoy es 6/8/2020. Mañana será 7/8/2020.'
>>> # Encontrar las apariciones de una fecha en el texto
>>> import re
>>> re.findall(r'\d+/\d+/\d+', texto)
['6/8/2020', '7/8/2020']
>>> # Reemplazá esas apariciones, cambiando el formato
>>> re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\2-\1', texto)
'Hoy es 2020-8-6. Mañana será 2020-8-7.'
>>>
#Para más información sobre el módulo re, mirá la documentación oficial en inglés o algún tutorial en castellano. Es un tema que escapa al contenido del curso pero te recomendamos que mires en detalle en algún momento. Aunque no justo ahora. Sigamos...
#Comentario
#A medida que empezás a usar Python es usual que quieras saber qué otras operaciones admiten los objetos con los que estás trabajando. Por ejemplo. ¿cómo podés averiguar qué operaciones se pueden hacer con una cadena?
#Dependiendo de tu entorno de Python, podrás ver una lista de métodos disponibles apretando la tecla tab. Por ejemplo, intentá esto:
>>> s = 'hello world'
>>> s.<tecla tab>
>>>
#Si al presionar tab no pasa nada, podés volver al viejo uso de la función dir(). Por ejemplo:
>>> s = 'hello'
>>> dir(s)
['__add__', '__class__', '__contains__', ..., 'find', 'format',
'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace',
'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition',
'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit',
'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase',
'title', 'translate', 'upper', 'zfill']
>>>
#dir() produce una lista con todas las operaciones que pueden aparecer luego del parámetro que le pasaste, en este caso s. También podés usar el comando help() para obtener más información sobre una operación específica:
>>> help(s.upper)
#Help on built-in function upper:

#upper(...)
    S.upper() -> string

    #Return a copy of the string S converted to uppercase.


#Los elementos de una cadena pueden ser separados en una lista usando el método split():
line = 'Pera,100,490.10'
row = line.split(',') #la coma indica el elemento que separa
row
['Pera', '100', '490.10']

#Para encontrar rápidamente la posición de un elemento en una lista, usá index().
nombres = ['Rosita','Manuel','Luciana']
nombres.index('Luciana')   # 2
#Si el elemento está presente en más de una posición, index() te va a devolver el índice de la primera aparición. Si el elemento no está en la lista se va a generar una excepción de tipo ValueError.
#rdenar una lista
#Las listas pueden ser ordenadas "in-place", es decir, sin usar nuevas variables.
s = [10, 1, 7, 3]
s.sort()                    # [1, 3, 7, 10]

# Orden inverso
s = [10, 1, 7, 3]
s.sort(reverse=True)        # [10, 7, 3, 1]

# Funciona con cualquier tipo de datos que tengan orden
s = ['foo', 'bar', 'spam']
s.sort()                    # ['bar', 'foo', 'spam']
#Usá sorted() si querés generar una nueva lista ordenada en lugar de ordenar la misma:
t = sorted(s)               # s queda igual, t guarda los valores ordenados

#Podés acceder a los elementos de las listas anidadas usando múltiples operaciones de acceso por índice.
>>> items[0]
'spam'
>>> items[0][0]
's'
>>> items[1]
['Banana', 'Mango', 'Frambuesa', 'Pera', 'Granada', 'Manzana', 'Lima']
>>> items[1][1]
'Mango'
>>> items[1][1][2]
'n'
>>> items[2]
[101, 102, 103]
>>> items[2][1]
102
>>>
#MANERA DE VER LO QUE ESTÁS ITERANDO (con un ejemplo de la clase):
for i,c in enumerate(cadena):
        capadepenapa=capadepenapa+c
        if c in ("aeiou"):
            capadepenapa=capadepenapa+"p"+c #es lo mismo que poner capadepenapa += "p"+c
        print(i,c,capadepenapa)
print(capadepenapa)


#PARA HACER UN BLOQUE/SECCIÓN:
####   #%% Sección 1

Cómo chequear la versión de Python:
import sys
print(sys.version)


# Cuantiles ponderados
 
def comando_cuantiles(df, variable, cuantiles, ponderador=None):

    import matplotlib.pyplot as plt
    #!pip install weightedcalcs
    import weightedcalcs as wc

    if ponderador!=None:
        calc = wc.Calculator(ponderador)
        percentiles = []
        #Computo los percentiles
        for x in range(1,cuantiles+1) :
            p = calc.quantile(df[df[variable]>0], variable,x/100)
            percentiles = percentiles + [p]

        data=df[df[variable]>0]
        lista_df = []
        link = []
        
        for index, row in data.iterrows():
            t = False
            per=0
            for i in percentiles:
                if t==False:   
                    if row[variable]>=i:
                        t=False
                    else:
                        t=True
                    per += 1
            lista_df = lista_df  + [per]
            link = link + [row['link']]
        dict_df = {'link':link,'percentil':lista_df}
        out = pd.DataFrame.from_dict(dict_df)
        out.percentil = out.percentil.astype(int)

        return out
    # else:
    #     df.quantile(q=cuantiles)
        
#     bar_df = gdf.groupby('percentil').agg({'ponderador':'sum'})
#     bar_df = bar_df.reset_index()
#     plt.bar(bar_df['percentil'], bar_df[ponderador])


###################################
###### DATOS ESPACIALES ###########
###################################

import geopandas as gpd

# Leer un archivo shape / geoespacial
mapa = gpd.read_file('path')

# Graficar el mapa
mapa.plot

# Explorar el mapa / graficar el mapa sobre un mapa real:
mapa.explore()

# Generar una matriz de distancias entre los puntos de un geo data frame:
matriz_distancias = mapa.geometry.apply(lambda g: mapa.distance(g))

# Covertir un data frame en geo data frame
db_gdf = gpd.GeoDataFrame(data=db, geometry=gpd.points_from_xy(db.longitud, db.latitud), crs='epsg:4326')

# Uniones espaciales / Seleccionar puntos dentro de un poligono
db_gdf = gpd.sjoin(db_gdf, polydf, op = 'within')

# Cambiar el CRS de un geo data frame
db_gdf = db_gdf.to_crs('epsg:4326') # creo que hay otro que se llama set_crs # y otra es db_gdf.crs = {'init': 'epsg:4326'}

# Crear un shapefile / convertir un geo data frame a shapefile
gdf.to_file("algo.shp")

# Diferencia entre estos dos CRSs 3857 y 4326: https://gist.github.com/Rub21/49ed3e8fea3ae5527ea913bf80fbb8d7

# Graficar dos capas juntas
base_plot = poligono.plot()
puntos.plot(ax=base_plot, color='blue');

# Ver ipynb "arreglo_espacioal_estaciones_servicio"



# %% BASIC COMMANDS

# Look for the position of an element in a list/dictionary/etc according to its value
x=["a","b"]
x.index("b")

# Create a list of numbers from 1 to n
list(range(1,5))

# Create a dictionary from two lists
list_a=["a", "b", "c"]
list_b=[1,2,3]
dict1 = dict(zip(list_a, list_b))

# %% DICTIONARIES
a= {"saludo":"hola"}

# Get keys
a.keys()

# Add/change a key-value pair
a["saludar"] = "holar"

# Delete key-value pairs
del(a["saludar"])

# Check if value is part of keys
"saludar" in a

# Dictionary of dictionaries
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }
    # Use chained square brackets
print(europe["france"]["capital"])

# %% LOOPS

# for lop

# pair index with value
fam =[1,3,5,1]
for index, value in enumerate(fam):
    print("index " + str(index) + ": " + str(value))
    
# Iterate through key-value pairs in a dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }
for country, capital in europe.items():
    print(country, " ", capital)
    
# Iterate over elements of a 2D numpy array
for x in np.nditer(my_array) :
    ...

# Continue code in the next line
df.groupby("col") \
    .mean()

# %% NUMPY - ARRAYS

# Logical equivalents of AND and OR and NOT
np.logical_and()
np.logical_or()
np.logical_not()

# %% NUMPY - RANDOM NUMBERS
from numpy import random

# Set seed
random.seed(123)
np.random.seed(123)

# %% PANDAS - DATA FRAMES
import pandas as pd

# Build a DataFrame from a dictionary of lists (column by column)
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
cars_dict = { 'country':names, 'drives_right':dr, 'cars_per_cap':cpc }
cars = pd.DataFrame(cars_dict)

# Build a DataFrame from a list of dictionaries (row by row)
list_of_dicts[{"country":"United States", 'drives_right':"True", 'cars_per_cap':809},
{"country":"Australia", 'drives_right':"False", 'cars_per_cap':731}]
cars=pd.DataFrame(list_of_dicts)

# Access/change row index
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']
cars.index = row_labels

# Read a csv file
pd.read_csv("file.path") # index_col to say which column corresponds to row index

# Write a csv file / convert data frame to csv
df.to_csv("file.csv")

# Select a column of a data frame (several ways)
cars["cars_per_cap"] # returns a pandas series
type(cars["cars_per_cap"])

cars[["cars_per_cap"]] # returns a pandas (sub) data frame
type(cars[["cars_per_cap"]])

# Select multiple columns of data frame
df[["col1, col2"]]
#or
cols = ["col1, col2"]
df[cols]

# Select rows by index
cars[0:5]

# Slice by rows/columns

# Select rows by row names
cars.loc["US"]
cars.loc[["US", "RU"]]

# Select rows by row names and column names
cars.loc[["RU"], ["country"]]

# Select all rows from columns
cars.loc[:, ["country", "drives_right"]]

# Subset data frame based on positions of rows/columns
cars.iloc[[1, 4]]
cars.iloc[[1, 4], [0, 1]]
cars.iloc[:, [0, 1]]

# Iterate over column names of data frame
for col in cars:
    print(col)

# Iterate over rows of data frame (row labes and row data)
for lab, row in cars.iterrows():
    print(lab)
    print(row)
    
# AAPLY METHOD: pass a function to a column of  data frame (it can be a lambda function)
# Create new columns by using apply on a function
    # eg the length of the name of the country
cars["length_country_name"] = cars["country"].apply(len)
cars

# Display column names, data types and missing values
df.info()

# Data frame dimension attribute
df.shape

# Overview of descriptive statistics of data frame
df.describe()

# Values of data frame (attribute) / get data frame values as array
df.values

# Columns of data frame (attribute)
df.columns

# Row names / row indexes (attribute)
df.index

# Sort rows of data frame
df.sort_values("column_name")
df.sort_values("column_name", ascending=False)
# Sort data frame accoridn to multiple columns
df.sort_values(["column_name", "col_name2"], ascending=[True, False])

# Subsetting according to logicla condition
df[df["col"]>10]
df[df["col"]=="value"]
df[(df["col"]>10) & (df["col"]=="value")] # !!! add parenthesis

# Subsetting using .isin()
df[df["col"].isin(["v1", "v2"])]

# Create a new column
df["col"] = df["col2"]*2

## SUMMARY STATISTICS
df["col"].mean() # mean of column
df["col"].median() # median of column
df["col"].mode() # mode of column
df["col"].min() # minimum of column
df["col"].max() # maximum of column
df["col"].var() # variance of column
df["col"].std() # standard deviation of column
df["col"].sum() # sum of column
df["col"].quantile() # quantile of column
df["col"].cumsum() # cumulative sum of column
# NOTE: this are all calculated based on the "index" axis of the data frame, which means "by rows", because of the default value
df.mean(axis="index")
# But you can also calculate summary statistics for each row (across columns)
df.mean(axis="columns")
# If you dont specify any column, the operation is computed over all columns
df.mean()

# Custom summary statistics using ".agg()" method (example: get 30th percentile)
def pct30(column):
    return column.quantile(0.3)
df["col"].agg(pct30) # there can be more than one function as arguments
df["col"].agg([pct30, median])

## COUNTING
# Count unique values of a column
df["col"].value_counts()
# count unique values and sort by frequency in descending order
df["col"].value_counts(sort=True)
# turn the counts into proportions of the total
df["col"].value_counts(normalize=True)
# Count by groups
df.groupby(['col1']).agg({'col2': 'count'}).reset_index()

# Drop duplicates
df.drop_duplicates(subset=["column1", "column2"])

# Group by column
df.groupby(["col1", "col3"])["col2", "col4"].agg([np.min, np.max, np.mean, np.median])
df.groupby("col").agg({'col2':'count'})
    # Group by index (when you have a multiindex)
df.groupby(level=0).agg({'col2':'count'}) # first index

# Pivot tables
df.pivot_table(values="col1", index="col_group") # mean by default
df.pivot_table(values="col1", index="col_group", aggfunc=[np.mean, np.median])
df.pivot_table(values="col1", index="col_group1", columns="col_group2") # group by two columns
df.pivot_table(values="col1", index="col_group1", columns="col_group2", fill_value=0) # group by two columns, fill missing values
df.pivot_table(values="col1", index="col_group1", columns="col_group2", fill_value=0, margins=True) # group by two columns, add row and column totals

## ROW INDEXES

# Set column as row INDEX
df = df.set_index("col")
# Reset data frame index
df.reset_index() # turns index as column
df.reset_index(drop=True) # discard index column
# Row indexes are useful because they allow you to subset much more easily. Instead of writing
df[df["col"].isin(["val1", "val2"])]
# you can write
df.loc[["val1", "val2"]]
# You can use multiple columns as index / multi-level/hierarchichal index
df = df.set_index(["col1", "col2"])
# Subsetting is done slightly differently
df.loc[[("val1_col1", "val1_col2"), ("val2_col1", "val2_col2")]]
# Sort by index
df.sort_index(level=["ind1", "ind2"], ascending=True)

# Slicing a data frame by index
    # first sort index
df.loc["val0":"val11"] # last value is included (this is different from list subsetting)
    # with multiple indexes
df.loc[("val1_ind1","val1_ind2"):("val2_ind1","val11_ind2")]
# This is particularly useful when indexes are dates. For example, you can pass a year as an argument without specifying month or day
df.loc["2013":"2015"]
df.loc["2013-01":"2015-12"]

# Slicing a data frame by column/s
df.loc[:, "col1":"col3"]

# Subsetting a data frame by row/column number / position
df.iloc[1:3, 6:8]

# Access the components of a date
df["col1"].dt.month
df["col1"].dt.year
# For example, if you have a column with a date, you can create a new column with the year
df["year"] = df["date"].dt.year

# Get all missing values of df == True
df.isna()

# Check if there are any missing values in each column
df.isna().any()

# Count missing values of columns
df.isna().sum()
df.isna().sum().plot(kind="bar") # plot nº of NaNs in a bar chart

# Remove rows with missing values
df.dropna()
df.dropna(subset = ['col1', 'col2']) # remove rows with missing values on specific columns

# Replace missing values with another value
df.fillna("MISSING")


# %% JOINING DATA - MUTATING JOINS - PANDAS

## INNER JOIN: return rows with matching values in both tables
df.merge(df2, on="col", suffixes=("_df1", "_df2"))

## LEFT JOIN
df.merge(df2, on='col', how='left') # default is 'inner'

## RIGHT JOIN
df.merge(df2, on='col', how='right') # default is 'inner'

## OUTER JOIN
df.merge(df2, on='col', how='outer') # default is 'inner'
# it can be used to find rows that do not have a match

# Merge according to columns with differnt names
df.merge(df2, left_on='col1', right_on='col1_right')

# Add a column that specifies the result of the merge for each row
df1.merge(df2, on="id", indicator=True)

## MERGE A TABLE TO ITSELF: you can do this with any type of merge

# Merge on data frame indexes> the sintax is the same as before (on='id') except when keys do not have the same name, where you have to add
df.merge(df2, on='id', left_on='col_df', right_on='right_col', left_index=True, right_index=True) # you need to set this last two to True

# Read csv and set column as index
pd.read_csv('file.csv',  index_col='col')

# Verifying merges (if not valid, returns error message)
df.merge(df2, on='id', validate='one_to_one') # default is "none"
df.merge(df2, on='id', validate='one_to_many')
df.merge(df2, on='id', validate='many_to_many')
df.merge(df2, on='id', validate='many_to_one')

# Merge ORDERED data or TIME SERIES data

# MERGE ORDERED
pd.merge_ordered(df1, df1, on='date') # default of how argument is 'outer'
# You can INTERPOLATE missing data 
pd.merge_ordered(df1, df1, on='date', fill_method='ffill') # forward fill: with the last value
# When using merge_ordered() to merge on multiple columns, the order is important when you combine it with the forward fill feature. The function sorts the merge on columns in the order provided.

# MERGE AS OF (also very useful for TIME SERIES data)
# similar to a left merge_ordered, but matches on the nearest key column and not on exact matches
pd.merge_asof(df1, df2, on='date') # default 'direction' argument is 'backwards': assigns the last row where the key column value in the right table is less than or equal to the key column value in the left table
pd.merge_asof(df1, df2, on='date', direction='forward') # assings the last row in the right table where the key is equal or greater than the one in the left
pd.merge_asof(df1, df2, on='date', direction='nearest')


# %% JOINING DATA - FILTERING JOINS - PANDAS

# Filter observations from one table based on whether or not they match an observation in another table

# SEMI JOIN:
# - Returns observations in the left table that have a match in the right table.
# Only the columns from the left table are shown. 
# No duplicate rows are returned, even if there is a one-to-many relationship
df_3 = df1.merge(df2, on="id") # first do an inner join
df1["id"].isin(df_3["id"])

# ANTI JOIN:
# - Returns observations in the left table that DO NOT have a match in the right table.
# - Only the columns from the left table are shown. 
df_3 = df1.merge(df2, on="id", how="left", indicator=True) # first do an inner join
df_3.loc[df_3["_merge"] == 'left_only', 'gid']


# %% JOINING DATA - CONCATENATION - PANDAS

# Vertical bind / row bind (default)
pd.concat([df1, df2, df3])
    # You can ignore the index
pd.concat([df1, df2, df3], ignore_index=True)
    # Add keys labels to identify which row came from which data frame
pd.concat([df1, df2, df3], ignore_index=False, keys=["1", "2", "3"])
    # You can bind two tables where one has more rows than the other. The method will keep all columns. You can sort columns alphabetically
pd.concat([df1, df2, df3], sort=True)
    # Only keep matching columns
pd.concat([df1, df2, df3], join='inner') # default is 'outer'

# Append method on data frames: simplified version of concat
df.append([df2, df3], ignore_index=True, sort=True)

# Horizontal bind / row bind (default)
pd.concat([df1, df2, df3])

# Verifying concatenations
df.concat(verify_integrity=True) # deafult is False. True verifies if there are duplicated indexes

# %% SELECTING DATA - QUERY 
# Similar to the WHERE clause of a SQL statement
df.query('col > 10') # returns all rows where col is grater than 10
df.query('col > 10 and col < 20')
df.query('col > 10 or col2 == "value"') # use double quotes inside the statement

# %% RESHAPING DATA - melt

# Reshape data from wide to long format
df.melt(id_vars=['col1', 'col2'])
    # chose which variables will remain unpivoted
df.melt(id_vars=['col1', 'col2'], value_vars=['2019', '2020'])
    # Set names for the new variable column and the values column
df.melt(id_vars=['col1', 'col2'], var_name='years', value_name='dollars')


# %% DATA VISUALIZATION WITH MATPLOTLIB

# Gallery: https://matplotlib.org/2.0.2/gallery.html
# Working with images: https://matplotlib.org/stable/tutorials/introductory/images.html
# Animations: https://matplotlib.org/stable/api/animation_api.html
# Geospatial data: https://scitools.org.uk/cartopy/docs/latest/

import matplotlib.pyplot as plt

x=[1,2,3,4]

y=[4,65,12,4]

z=[3,3,2,1]

# To visualize graph, show it
plt.show()

# To close visualization
plt.clf()

# Line plot
plt.plot(x, y, kind="line") # here "line" is default, so not necessary

# Scater plot
plt.scatter(x, y) # or df.plot(x,y,kind="scatter")
    # Set dot size according to a variable
plt.scatter(x, y, s=z)

# Histogram
plt.hist(x)
# control bin number
plt.hist(bins=29)

# Title
plt.title("Title")

# X and Y labels
plt.xlabel()
plt.ylabel()

# Change to logarithmic scale
plt.scale("log")

# Bar plot
plt.plot(kind="bar")
df.plot(kind="bar")

# Place two or more graphs in the same plot
df.plt.hist(alpha=0.7)
df2.plt.hist(alpha=0.7)
plt.show()

# Plot multiplie histogramas at a time, but not on the same plot
df.[["col1", "col2"]].hist()

# Add legend to plot
plt.legend(["A", "B"])


# (INTRODUCTION TO DATA VISUALIZATION WITH MATPLOTLIB)

# Create figure and axis objects
# Figure: container that holds everything you see on the page
# Axis: part of the page that holds the data
fig, ax = plt.subplots()
plt.show()

# LINE CHARTS

# Plotting command: methods of the axis object
ax.plot(df['col1'], df['col2'])
plt.show()

# Add more data (multiple line plots in the same figure)
fig, ax = plt.subplots()
ax.plot(df['col1'], df['col2'])
ax.plot(df2['col1'], df2['col2'])
plt.show()

# Line plot with dots (markers)
fig, ax = plt.subplots()
ax.plot(df['col1'], df['col2'], marker='o') # other options: https://matplotlib.org/stable/api/markers_api.html
plt.show()

# Change the linestyle of a line plot
fig, ax = plt.subplots()
ax.plot(df['col1'], df['col2'], linestyle="--") # other options: https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html
plt.show() # another option is "None"

# Change color of line graph
ax.plot(df['col1'], df['col2'], color='r') # Red

# Customize axis labels
ax.set_xlabel('Time')
ax.set_ylabel('Time')

# Title
ax.set_title('Title')

# Multiple plots in the same figure ('Small multiples': similar data across diferent groups/subjects)
fig, ax = plt.subplots(3, 2) # figure object with 3 rows, 2 columns
plt.show()
# Now "ax" is an array of axis objects
# See dimensions of axis
ax.shape
# Add a plot to one of the axis objects
ax[0,0].plot(df['col1'], df['col2']) # top left subplot
# only one column
fig, ax = plt.subplots(3, ) # figure object with 3 rows, 1 columns
plt.show()
ax[0].plot(df['col1'], df['col2']) # top subplot

# Set equal range of axis in subplots
fig, ax = plt.subplots(2, 1, sharey=True)

# Plotting TIME SERIES data
# First set date column as index of pandas data frame
df = pd.read_csv('df.csv', parse_dates=['date'], index_col='date')
# Add the index as the X axis
ax.plot(df.index, df['col'])

# Use two Y axis scales
fig, ax = plt.subplots()
ax.plot(df.index, df['col1'], color='blue')
ax.set_ylabel('Axis 1', color='blue') # color may also be passed here
ax.tick_params('y', colors='blue') # you can also set color of ticks and ticks label 
ax2 = ax.twinx() # share the same x axis, but not the same y axis
ax2.plot(df.index, df['col2'], color='red')
ax2.set_ylabel('Axis 2', color='red')
ax2.tick_params('y', colors='red') # you can also set color of ticks and ticks label 
plt.show()

# Create a function to plot a time series
def plot_timeseries(axes, x, y color, xlabel, ylabel):
    axes.plot(x, y, color=color)
    axes.set_xlabel(xlabel)
    axes.set_ylabel(ylabel)
    axes.tick_params('y', colors=color)
# Replicating the exercise above
fig, ax = plt.subplots()
plot_timeseries(ax, df.index, df['col1'], 'blue', 'Xlab', 'Ylab')
plot_timeseries(ax, df.index, df['col2'], 'red', 'Xlab2', 'Ylab2')
plt.show()

# Add annotations (to a time series plot)
ax.annotate("Annotation", xy = (pd.Timestamp('2015-10-06'), 1), \ # xy is the position of the point
    xytext = (pd.Timestamp('2015-10-06'), -0.2), \# xytext is the position of the text
    arrowprops={"arrowstyle":"->", "color":"gray"}) # "Arrow properties": Add an arrow that points from the text to the data point
# More options at: https://matplotlib.org/stable/tutorials/text/annotations.html


# BAR CHARTS

# Create a bar chart
fig, ax = plt.sbuplots()
ax.bar(df.index, df['col'])
plt.show()

# Rotate tick labels
ax.set_xticklabels(df.index, rotation=90)

# Stacked bar chart
fig, ax = plt.sbuplots()
ax.bar(df.index, df['col1'])
ax.bar(df.index, df['col2'], bottom=df['col1']) # the bottom of col2 bars should be the height of col1 bars
ax.bar(df.index, df['col3'], bottom=df['col1']+df['col1'])
plt.show()

# Add a legend to stackedd bar chart
fig, ax = plt.sbuplots()
ax.bar(df.index, df['col1'], label="COL 1")
ax.bar(df.index, df['col2'], bottom=df['col1'], label="COL 2") # first, define labels
ax.bar(df.index, df['col3'], bottom=df['col1']+df['col1'], label="COL 3")
ax.legend() # call axes legend method
plt.show()

# HISTOGRAMS

# Multiple histograms in the same plot
fig, ax = subplots()
ax.hist(df['col1'], label="C1")
ax.hist(df['col2'], label="C2")
ax.legend()
plt.show()

# Set number of bins of a histogram. Two options
    # Quantity of bins
ax.hist(df.col, bins=5)
    # Sequence of values
ax.hist(df.col, bins=[10, 20, 30, 40, 50])

# Change histogram type
ax.hist(df.col, bins=5, histtype="step") # displays the histogram with thin lines instead of solid bars

# STATISTICAL PLOTTING

# Add error bars to bar charts
fig, ax = subplots()
ax.bar("group1", df['g1'].mean(), yerr=df['g1'].std())

# Add error bars to line charts
fig, ax = subplots()
ax.errorbar(df['col1'], df['col2'], yerr=df['col2_std'])

# BOXPLOTS
# Create two boxplots in the same plot
fig, ax = subplots()
ax.boxplot([df['col1'], df['col2']])
ax.set_xticklabels(['Col1', 'Col2'])
plt.show()

# SCATTER PLOTS
fig, ax = subplots()
ax.scatter(df['col1'], df['col2'])
plt.show()

# Create scatter plot with multiple groups of points
# eg with time series
sixties = df["1960-01-01": "1960-12-31"]
seventies = df["1970-01-01": "1970-12-31"]
fig, ax = subplots()
ax.scatter(sixties['col1'], sixties['col2'], color='blue', label='sixties')
ax.scatter(seventies['col1'], seventies['col2'], color='red', label='seventies')
ax.legend()
plt.show()

# Encoding a third variable by color (as a gradient of color)
fig, ax = subplots()
ax.scatter(df['col1'], df['col2'], c=df.index) # here index could be a time series index

# PREPARING YOUR FIGURES TO SHARE WITH OTHERS

# Changing the overall style of the figure / Set figure style
plt.style.use("ggplot") # This style will apply to all figures in the session until you change it to another style
fig, ax = plt.subplots()
ax.plot(df['col1'], df['col2'])
ax.plot(df2['col1'], df2['col2'])
plt.show()
# Go back to default style
plt.style.use("default") 
# See all styles: https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html
# Guidelines:
    # - Avoid dark backgrounds
    # - Preer colorblind options ("seaborn-colorblind", "tableau-colorblind10")
    # If printed with color, use less ink
    # f printed black and white, use "grayscale"

# SAVING FIGURES

# Replace plt.show() with a call to fig.savefig()
fig, ax = plt.subplots()
ax.plot(df['col1'], df['col2'])
fig.savefig("file.png", quality=50) # Also "jpg", "svg". Avid quality values above 95
# Or control dpi (dots per inch, resolution)
fig.savefig("file.png", dpi=300)

# Control figure size
fig, ax = plt.subplots()
ax.plot(df['col1'], df['col2'])
fig.set_size_inches([4,5]) # Height and width
fig.savefig("file.png", dpi=300)

# JOINTPLOTS: scatter plots together with histograms of both variables
sns.jointplot(x = paid_apps['Price'], y = paid_apps['Rating'])



# %% INTRODUCTION TO DATA VISUALIZATION WITH SEABORN
# https://seaborn.pydata.org/

# Built in dataset
tips = sns.load_dataset("tips")

# Built on matplotlib, used to work with pandas data frames.

import seaborn as sns
import matplotlib.pyplot as plt # you also need to import matplotlib

# Make a plot with seaborn
sports = ['football', 'baseball', 'baseball', 'baseball', 'baseball', 'football']
sns.countplot(x=sports) # or sns.countplot(y=sports)
plt.show()

# Using pandas with seaborn
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
# Scatter plot (in Seaborn "relplots" are prefered to scatterplots)
sns.scatterplot(x='col1', y='col2', data=df)
plt.show()

# Add a third variable as hue (color) (color by group)
tips = sns.load_dataset("tips")
sns.scatterplot(x="total_bill", y="tip", data=tips,
    hue="smoker", # variable for hue (legend is added automatically)
    hue_order=["Yes", "No"], # order of labels in legend
    palette={"Yes":"black", "No":"red"} # define palette of colors
    ) 
plt.show()

# RELATIONAL PLOTS

# Creating multiple plots in figure (relplot())
# Relplot - SCATTERPLOTS
tips = sns.load_dataset("tips")
sns.relplot(x="tota_bill", y="tip", data=tips, kind="scatter", col="smoker") # use the col argument
plt.show()
# Arrange multiple plots vertically
sns.relplot(x="tota_bill", y="tip", data=tips, kind="scatter", row="smoker") # or row argument
# Use two dimensions
sns.relplot(x="tota_bill", y="tip", data=tips, kind="scatter", col="smoker", row="time")
# Set number of plots per row
sns.relplot(x="tota_bill", y="tip", data=tips, kind="scatter", col="day", col_wrap=2)
# Change the order of the plots
sns.relplot(x="tota_bill", y="tip", data=tips, kind="scatter", col="day", col_wrap=2, col_order=["Thur", "Fri", "Sat", "Sun"])

# Customizing scatterplots (can be used in both scatterplots and relplots)
tips = sns.load_dataset("tips")
    # Varying the point size accoridng to a column
sns.relplot(x="tota_bill", y="tip", data=tips, kind="scatter", size="size")
    # Add color variation according to point size
sns.relplot(x="tota_bill", y="tip", data=tips, kind="scatter", size="size", hue="size") # size is quantitative variable
    # Varying point style
sns.relplot(x="tota_bill", y="tip", data=tips, kind="scatter", hue="smoker", style="smoker")
    # Varying point transparency
sns.relplot(x="tota_bill", y="tip", data=tips, kind="scatter", alpha=0.4)

# LINE PLOTS
import seaborn as sns
import matplotlib.pyplot as plt
sns.relplot(x='col1', y='col2', data=df, kind="line")
plt.show()

# Add a trendline to a scatter plot
sns.lmplot(x='col1', y='col2', data=df, ci=None)

# Multiple line plots with different colors and line styles
sns.relplot(x='col1', y='col2', data=df, kind="line", hue="col3", style="col3")
# if you dont want the line style to vary by group, remove style argument and add argument dashes=False
# If a line plot is fed multiple observations for each X-value, it aggregates them and shows the mean and a 95% confidence interval for the mean
# If instead of a 95% confidence interval you want 1 standard deviation, use
sns.relplot(x='col1', y='col2', data=df, kind="line", ci="sd")
# Or turn it off
sns.relplot(x='col1', y='col2', data=df, kind="line", ci=None)

# Different point markers
sns.relplot(x='col1', y='col2', data=df, kind="line", hue="col3", style="col3", markers=True)

# CATEGORICAL PLOTS: COUNT PLOT, BAR PLOT and POINT PLOT
sns.catplot(x='col1', data=df, kind="count") # count plot
sns.catplot(x='col1', y='col2', data=df, kind="bar") # bar plot (shows mean of variable with CIs)

# Order the bars of a categorical plot
cat_order = ['cat1', 'cat2']
sns.catplot(x='col1', data=df, kind="count", order=cat_order)

# Change the orientation of the bars in a categorical plot
sns.catplot(x='col2', y='col1', data=df, kind="bar") # just switch the X and Y variables
sns.catplot(y='col1', data=df, kind="count", order=cat_order)

# BOX PLOTS
sns.catplot(x='var_grupo', y='col1', data=df, kind='box')

# Change the order of the boxplots
cat_order = ['cat1', 'cat2']
sns.catplot(x='var_grupo', y='col1', data=df, kind='box', order=cat_order)

# Omit outliers
sns.catplot(x='var_grupo', y='col1', data=df, kind='box', sym='') # sym can also be changed to change te appearence of the outliers

# Change the whiskers
sns.catplot(x='var_grupo', y='col1', data=df, kind='box', whis=2.0) # Extend to 2x interquantile range
sns.catplot(x='var_grupo', y='col1', data=df, kind='box', whis=[5,95]) # Extend to a specific percentile
sns.catplot(x='var_grupo', y='col1', data=df, kind='box', whis=[0,100]) # Extend to min and max values

# POINT PLOTS: show the mean of a quantitative variable for the mean of observations in each category, with 95% CI
sns.catplot(x='cat_var', y='var1', data=df, kind='point')
sns.catplot(x='cat_var', y='var1', data=df, kind='point', hue='var2') # add multiple lines with diff colors
sns.catplot(x='cat_var', y='var1', data=df, kind='point', join=False) # do not join points
# Us median instead of mean
from numpy import median
sns.catplot(x='cat_var', y='var1', data=df, kind='point', estimator=median)
# Add caps to the confidence intervals
sns.catplot(x='cat_var', y='var1', data=df, kind='point', capsize=0.2)

# Pre-set FIGURE STYLES: white (default), dark, whitegrid, darkgrid, ticks
# Set figure style
sns.set_style("whitegrid")
# 'whitegrid'  Add a grid in the background
# 'ticks'  Add tick marks
# 'dark'  Add a grey background
# 'dark'  Add a grey background and white grid

# Pre-set seaborn DIVERGING PALETTES: "RdBu", "PRGn"
# Set color palette
sns.set_palette("RdBu")
sns.catplot(x='col1', data=df, kind="count")
# Reverse a palette: "RdBu_r", "PRGn_r"

# Pre-set seaborn SEQUENTIAL PALETTES: Greys, Blues, PuRd, GnBu (best for continuous variable)
sns.set_palette("Blues")

# Create custom palette
custom_palette = ['red', 'green', 'orange', 'blue', 'yellow', 'purple']
sns.set_palette(custom_palette)
custom_palette = ['#FBB4AE', '#B3CDE3', '#CCEBC5', '#DECBE4', '#FED9A6', '#FFFFCC'] # with hex color codes
sns.set_palette(custom_palette)

# Change the SCALE STYLE / SIZE of a plot: paper (default), notebook, talk, poster (basically, the size of the labels relative to the plot increases as you go right in the options)
sns.set_context('notebook')

# PLOT TITLES AND AXIS LABELS
# Seaborn plots create two different types of objects: FacetGrid and AxesSubplot
# How to see this:
g = sns.scatterplot(x='col1', y='col2', data=df)
type(g) # returns "matplotlib.axes._subplots.AxesSubplot"
# While
g = sns.catplot(x='col1', y='col2', data=df, kind='box')
type(g) # returns 'seaborn.axisgrid.FacetGrid'
# a FacetGrid consists of one or more axes suplots. relplot() and catplot() can create subplots
# AxesSubplots, on the other hand, can only contain one plot. Like scatterplot() or countplot(), etc, which return a single AxesSubplot object

# Add a TITLE to a FacetGrid object
g = sns.catplot(x='col1', y='col2', data=df, kind='box') # First assign the plot to an object
g.fig.suptitle('New title') # now use subtitle method
# Adjust the height of the title
g.fig.suptitle('New title', y=1.05) 

# Add a TITLE to an AxesSubplot object
g = sns.scatterplot(x='col1', y='col2', data=df)
g.set_title('New title', y=1.05)
# Set it for various subplots
g = sns.catplot(x='col1', y='col2', data=df, kind='box', col='var3')
g.set_titles('This is {col_name}', y=1.05)

# Add AXIS LABELS
g = sns.catplot(x='col1', y='col2', data=df, kind='box', col='var3')
g.set(xlabel= 'xlab',
    ylabel='ylab')

# ROTATE tick labels
g = sns.catplot(x='col1', y='col2', data=df, kind='box', col='var3')
plt.xticks(rotation=90)


# %% INTERMEDIATE DATA VISUALIZATION WITH SEABORN
import matplotlib.pyplot as plt
import seaborn as sns
tips = sns.load_dataset("tips")

# HISTOGRAM
sns.histplot(tips['total_bill'])

# More general: DISTRIBUTION PLOT (best plot to start with)
sns.displot(tips['total_bill']) # default is histogram
# KERNEL DENSITY PLOT
sns.displot(tips['total_bill'], kind='kde')
# Set number of bins, add kernel density plot
sns.displot(tips['total_bill'], bins=10, kde=True)
# Add tick marks for each observation
sns.displot(tips['total_bill'], rug=True)
sns.displot(tips['total_bill'], kind='kde', rug=True, fill=True)
# Estimated cumulative density function
sns.displot(tips['total_bill'], kind='ecdf') 

# REGRESSION PLOTS
sns.regplot(data=tips, x='total_bill', y='tip')

# FACETING: the use of plotting multiple graphs by changing only a single variable

# LM PLOT: relation between 2 variables
sns.lmplot(data=tips, x='total_bill', y='tip', hue='sex') # regression line for each value of "hue" variable
sns.lmplot(data=tips, x='total_bill', y='tip', col='sex') # one graph for each value of "hue" variable
sns.lmplot(data=tips, x='total_bill', y='tip', row='sex')

# SEABORN STYLES
# Compare styles
for style in ['white', 'dark', 'whitegrid', 'darkgrid', 'ticks']:
    sns.set_style(style)
    sns.displot(tips['total_bill'])
    plt.show()

# Remove axis lines
sns.histplot(tips['total_bill'])
sns.despine(left=True) # left Y axis. Also top, right, bottom

# COLORS

# Use matplotlib color codes
sns.set(color_codes = True)
sns.displot(tips['total_bill'], color= 'g')

# Define PALETTE of colors
palettes = ['deep', 'muted', 'pastel', 'bright', 'dark', 'colorblind']
for p in palettes:
    sns.set_palette(p)
    sns.palplot(sns.color_palette()) # Display a color palette
    plt.show()
# You can also define it within a plot
sns.violinplot(data=df,
         x='Award_Amount',
         y='Model Selected',
         palette='husl')

# Defining custom color palettes
# Circular colors: when data is not ordered
sns.palplot(sns.color_palette("Paired", 12)) # 12 colors. palplot is to plot the palette
# Sequential colors: when data has a consistent range from high to low
sns.palplot(sns.color_palette("Blues", 12))
# Diverging colors: when both the low and high values are interesting
sns.palplot(sns.color_palette("BrBG", 12))

# Customizing with matplotlib
# Set a limit to the axis scale
fig, ax = plt.subplots()
sns.histplot(tips['total_bill'], ax=ax)
ax.set(xlim = (0,40)) # you can either 

# Set figure size
fig, (ax0, ax1) = plt.subplots(nrows=1, ncols=2, sharey=True, figsize=(7,4))
sns.histplot(tips['total_bill'], ax=ax0)
sns.histplot(tips['size'], ax=ax1)
# Graph a vertical line
ax0.axvline(x=20, label='line', linestyle='--', linewidth=2)
ax0.legend()

## CATEGORICAL PLOTS
# 3 GROUPS:
# 1) The ones that show all individual observations on the plot: STRIPPLOT and SWARMPLOT
# 2) Abstract representations: BOXPLOT, VIOLIN PLOT, BOXENPLOT
# 3) Statistical estimates: BARPLOT, POINTPLOT, COUNTPLOT
tips = sns.load_dataset("tips")

# STRIPPLOT
sns.stripplot(data=tips, y='total_bill', x='sex')
sns.stripplot(data=tips, y='total_bill', x='sex', jitter=True) # jitter adds a random jitter (like wiggle) sideways so that points are more easily visualized

# SWARMPLOT: points will not overlap, but it is not so convenient for very large data sets
sns.swarmplot(data=tips, y='total_bill', x='sex') 

# VIOLIN PLOT: combination of a kernel density plot and a boxplot (takes time to render)
sns.violinplot

# BOXENPLOT: enhanced box plot (quicker than a violin plot)
sns.boxenplot(data=tips, y='total_bill', x='sex')

# BARPLOT
sns.barplot(data=tips, y='total_bill', x='smoker', hue='sex')

# POINTPLOT
sns.pointplot(data=tips, y='total_bill', x='smoker', hue='sex')


## REGRESSION PLOTS

# REGPLOT
sns.regplot(data=tips, y='total_bill', x='tip') # linear regression line
# Add a marker to each point
sns.regplot(data=tips, y='total_bill', x='tip', marker='+')
# Polinomial regression
sns.regplot(data=tips, y='total_bill', x='tip', order=2) # of order 2
# Add an estimator
sns.regplot(data=tips, y='total_bill', x='tip', x_estimator=np.mean) # !!! fix example
# Disable the regression line (just the scatter plot)
sns.regplot(data=tips, y='total_bill', x='tip', fit_reg=False)

# RESIDUAL PLOT: plots the residuals of regression between y and x
sns.residplot(data=tips, y='total_bill', x='tip') # linear regression
sns.residplot(data=tips, y='total_bill', x='tip', order=2) # polynomial of order 2

## MATRIX PLOTS

# Create a matrix-like object from two variables of a data frame / CROSS-TABULATION
mat = pd.crosstab(tips['day'], tips['time'], values=tips['total_bill'], aggfunc='mean')

# HEATMAP
sns.heatmap(mat)
# Turn on annotations in individual cells / display cell value in numbers
sns.heatmap(mat, annot=True)
# Define a color map
sns.heatmap(mat, annot=True, cmap="YlGnBu")
# Hide the color bar
sns.heatmap(mat, annot=True, cmap="YlGnBu", cbar=False)
# Define the width of the lines between the cells
sns.heatmap(mat, annot=True, cmap="YlGnBu", cbar=False, linewidths=.5)
# Center the color scheme on a psecific value 
sns.heatmap(mat, annot=True, cmap="YlGnBu", cbar=False, linewidths=.5, center=mat.loc[1,2])

# CORRELATION MATRIX PLOT
sns.heatmap(tips[list(tips.columns)].corr(), cmap='YlGnBu')

# FACETTING: eg. multiple plots of the same variable across categories
g = sns.FacetGrid(tips, col='sex')
g.map(sns.boxplot, 'total_bill')
# catplot() is a shortcut to create a facet grid more easily
sns.catplot(x='total_bill', data=tips, col='sex', kind='box')
# Facet grid accept matplootlib plots
import matplotlib.pyplot as plt
g = sns.FacetGrid(tips, col='sex')
g.map(plt.scatter, 'total_bill', 'tip')
# lmplot() plots scatter and regression plots on a FacetGrid
sns.lmplot(data=tips, x='total_bill', y='tip', col='sex', col_order=['Male', 'Female'], row='day', fit_reg=False)

# PAIRGRID: shows pairwise relationships between data elements
g = sns.PairGrid(tips, vars=['total_bill', 'tip'])
g.map(sns.scatterplot)
# Define graphs on diagonals and off diagonls
g = sns.PairGrid(tips, vars=['total_bill', 'tip'])
g.map_diag(sns.histplot)
g.map_offdiag(sns.scatterplot)
# pairplot is a shortcut function to a pair grid
sns.pairplot(tips, vars=['total_bill', 'tip'], kind='reg', diag_kind='hist', hue='sex', palette='husl')
# Increase transparency
sns.pairplot(tips, vars=['total_bill', 'tip'], diag_kind='hist', hue='sex', palette='husl', plot_kws={'alpha':0.5})

# JOINT GRID: compare distribution between two variables
g = sns.JointGrid(tips, x='total_bill', y='tip')
g.plot(sns.regplot, sns.histplot)
# Advanced jointgrid: bivariate kernel density plot
g = sns.JointGrid(tips, x='total_bill', y='tip')
g.plot_joint(sns.kdeplot)
g.plot_marginals(sns.kdeplot, fill=True)
# Shortcut with jointplot()
sns.jointplot(data=tips, x='total_bill', y='tip', kind='hex')
# Overlay a kernel density plot over the scatter plot
sns.jointplot(data=tips, x='total_bill', y='tip', kind='scatter').plot_joint(sns.kdeplot)

# %% INTRODUCTION TO STATISTICS

# Calculate the mode
import statistics
statistics.mode(df['col'])

# Variance
np.var(df['col']) # population variance
np.var(df['col'], ddof=1) #  sample variance

# Standar deviation
np.std(df['col']) # population
np.std(df['col'], ddof=1) #  sample

# Mean absolute deviation (like variance but without squaring. It penalizes distances equally)
np.mean(np.abs(df['col']-mean(df$col)))

# Quantiles
np.quantile(df['col'], 0.5) # median
np.quantile(df['col'], [0.5,0.9])
np.quantile(df['col'], np.linspace(0,1,5)) # five quantiles with equal distance

# Interquantile range
from scipy.statshist import iqr
iqr(df['col'])

# Outliers according to boxplot criterion
from scipy.stats import iqr
iqr(df['col'])
lower_threshold = np.quantile

# Sample a data frame
df.sample(n=10) # without replacement
df.sample(n=10, replace=True) # with replacement

# Calculate cumulative probabilities (less than or equal to) of a Uniform distribution
from scipy.stats import uniform
uniform.cdf(7, 0, 12) # pointvalue=7, lower=0, upper=12. Prob of getting 7 in a uniform range of 0-12

# Generate random numbers with a uniform distribution
from scipy.stats import uniform
uniform.rvs(0, 5, size=10) # min, max, n

# Generate a variable with binomial distribution
from scipy.stats import uniform
binom.rvs(1, 0.5, size=100) # n of coins, prob of success, n of trials

# Calculate point probabilities of a Binomial distribution
from scipy.stats import binom
binom.pmf(5, 100, 0.5) #n of success, n trials, prop of success

# Calculate cumulative probabilities (less than or equal to) of a Binomial distribution
from scipy.stats import binom
binom.cdf(5, 100, 0.5) #n of success, n trials, prop of success

# Calculate cumulative probabilities (less than or equal to) of a normal distribution
from scipy.stats import norm
norm.cdf(50, 47, 5) # value, mean, sd

# Calculate point values of percentiles of a normal distribution
from scipy.stats import norm
norm.ppf(0.9, 47, 5) # value, mean, sd

# Generate random numbers with a normal distribution
norm.rvs(0, 1, size=100) # mean, sd, n

# Calculate point probabilities of a Poisson distribution
from scipy.stats import poisson
poisson.pmf(5, 8) # value, lambda (mean rate)

# Calculate cumulative probabilities (less than or equal to) of a Poisson distribution
from scipy.stats import norm
poisson.cdf(5, 8) # value, lambda (mean rate)

# Generate random numbers with a Poisson distribution
norm.rvs(8, size=100) # lambda, size

# Calculate cumulative probabilities (less than or equal to) of a Exponential distribution
from scipy.stats import expon
expon.cdf(5, 8) # value, 1/lambda (1/mean Poisson rate)

# Calculate the (Pearson) correlation between two variables
df['col1'].corr(df['col2'])

# %% INTRODUCTION TO NUMPY
# It is a foundational library on which others like scikit-learn, scipy, matplotlib, pandas and tensorflow are built
# Array: a grid like object that holds data. Can have any number of dimensions, and each dimension can have any length. Admit only one data type, uses less memory.
import numpy as np

# Create an array from a list
list1=[1,5,1,2,3,6]
array=np.array(list1)
type(array)
# 2 dimensions
list_of_lists= [[1,4,3],
                [7,4,7],
                [10,5,2]]
np.array(list_of_lists)
# 3 dimensions: list of lists of lists

# Other ways of creating arrays
np.zeros((2,3)) # 2 rows, 3 columns of zeros
np.ramdom.ramdom((3,6)) # random numbers between 0 and 1 (function "random" of numpy module "random")
np.arange(-3,4) # evenly spaced array of consecutive integers, from -3 to 4 (excluded)
np.arange(4) # beings at 0
np.arange(-3, 4, 3) # steps of 3
np.array(range(1,13)) # Create a sequence of numbers

# Return the dimension of an array
array.shape

# Convert a mult-dimensional array into a one-dimensional array
array.flatten()

# Redefine the shape of an array
array.reshape((2,3)) # the tuple passed must be compatible with the number of elements of the original array

# NUMPY DATA TYPES: more specific than Python data types
# They include the type of data (integer, float, string) AND the available memory in bits
# Eg: 'np.int64', 'np.float32', '<U12' (unicode string with max length 12), 'bool_'

# Return the data type of an array
array.dtype

# You can determine the data type when creating an array
np.array([1.23,4.5,1], dtype=np.float32)

# Convert array data type (for example to reduce memory usage)
array.astype(np.int8)

# INDEXING arrays
array[0] # one dimension
array[2,4] # two dimensions. third row of fifth column
array[1] # second row
array[:, 3] # fourth column

# SLICING arrays
array[2:4] # one dimension (2 is included, 4 is not)
array[2:4, 5:8] # two dimensions
array[2:4:1, 5:8:1] # two dimensions, with step value (skip one in columns)

# SORTING an array along an axis
np.sort(array) # axis 1, by column (so each row is ordered from smallest to largest)
# The default axis is the last axis of the array passed to it. If the array is 2D, then the last axis is columns
np.sort(array, axis=0) # axis 0, by rows (so each column is ordered from smallest to largest)

# FILTERING
# Boolean mask: an array of booleans with the same shape as the filtered array
# Fancy indexing: returns an array of elements which meet a certain condition
one_to_five = np.array([1,2,3,4,5])
mask = one_to_five % 2 == 0
one_to_five[mask]
# ... with 2D arrays
classroom_ids_and_sizes = np.array([[1,22], [2,21], [3,27], [4,26]])
# eg check which values in second column are even
mask = classroom_ids_and_sizes[:, 1] % 2 == 0
# then index the first column using that mask, to return the class ids
classroom_ids_and_sizes[:, 0][mask]

# Filtering with NP.WHERE: returns an array of indices of elements that meet a certain condition
np.where(classroom_ids_and_sizes[:, 1] % 2 == 0) # returns a tupple of arrays, one for each dimension index
# For 2D arrays, it returns two tupples of arrays, because identifying each element requires two indices
row_index, col_index = np.where(sudoku==0) # it is helpful to unpack the indices in two objects

# Replace all elements of an array with a specific value
np.where(array == value, 'replace_with_this_if_condition_is_met', array) # change to that string, otherwise return original element

# ADDING AND REMOVING ELEMENTS OF AN ARRAY

# Concatenation (arrays must have compatible shapes and dimensions. it never adds new dimensions)
np.concatenate((array1, array2)) # along the first axis (default axis=0, adding new rows) 
np.concatenate((array1, array2), axis=1) # along the second axixs, adds new columns
# To concatenate a 2D array with a 1D array, first you need to reshape the 1D array
array_1D = np.array([1,2,3])
column_array_2D = array.1D.reshape((3,1)) # here you "add" the column
column_array_2D

# Delete row of array
np.delete(array, 1, axis=0) # in the position of 1 there can be a slice, index or array of indices. Here you  delete the second row.
# Delete column of array
np.delete(array, 3, axis=1)

# SUMMARIZING DATA
# AGREGATING METHODS
array.sum() # sums all elements in array
array.sum(axis=0) # sum all rows in each column (create column totals)
array.sum(axis=1) # sum all columns in each row (create row totals)
array.sum(axis=1, keepdims=True) # If True, the dimensions that are collapsed when aggregating are left in the output array and set to 1 (for dimension compatibility)
array.min()
array.max()
array.mean()
array.cumsum(axis=0)

# VECTORIZED OPERATIONS
# Use of optimized code in C language
array + 3 # add a scalar
array * 3 # multiply
array1 + array2 # add compatible arrays
array1 * array2
array > 3 # boolean mask

# Convert Python functions to a numpy vectorized function
array = np.array(["NumPy", "is", "awesome"]) # eg, check the length of each element
len(array) > 2 # this does not work element-wise because len is a Python function
vectorized_len = np.vectorize(len) # create vectorized function
vectorized_len(array) > 2

# BROADCASTING: math operations between arrays of different shapes
# Summing a scalar to an array is an example
# Still arrays have to be somewhat compatible
# Numpy compares sets of array dimensions from right to left
# Two dimensions are compatible when one of them has a length of one or they are of equal lengths
# Both arrays have to be compatible across all of their dimensions. But the two arrays do not need to have the same number of dimensions.
# Examples: (10,5) and (10, 1) / (10,5) and (5,) are compatible. (10,5) and (5,10) / (10,5) and (10,) are NOT compatible
np.arange(10.reshape((2,5))) + np.array([0,1,2,3,4])
# The assumption is that the user is trying to broadcast row-wise
# Eg this does not work
np.arange(10).reshape((2,5)) + np.array([0,1])
# But this does
np.arange(10).reshape((2,5)) + np.array([0,1]).reshape((2,1))

# SAVING AND LOADING ARRAYS

# RGB ARRAY: each value describes the red, green and blue component of a single picture
rgb = np.array([[[255,0,0], [255,0,0], [255,0,0]],
                [[0,255,0], [0,255,0], [0,255,0]],
                [[0,0,255], [0,0,255], [0,0,255]]
                ])
plt.imshow(rgb)
plt.show()

# Arays con be saved in .csv, .txt, .pkl, and .npy (ideal)

# Load a numpy array
with open("file.npy", "rb") as f: # Open takes 2 arguments: the name of the file and the open mode (here: "read binary")
    file_array = np.load(f)

# Save a numpy array
with open("file2.npy", "wb") as f: # wb: "write binary"
    np.save(f, file2)

# Call the documentation of a numpy method
help(np.ndarray.flatten)

# ARRAY ACROBATICS: changing axis order (useful for data augmentation, eg flipping images)

# Flip an array along every axis
np.flip(array)
np.flip(array, axis=(0,1)) # flip along specific axis

# Transpose an array
np.transpose(array)
np.transpose(array, axes=(1,0,2)) # specify transpose order (here makes column to rows but leaves 3rd dim untouched) (!!! its "axEs" not "axis". Order matters here)

# STACKING AND SPLITTING
# Split an array
red, green, blue = np.split(rgb_array, 3, axis=2) # array, number of equally sized arrays desired after the split, the axis to plit along (here: split rgb along the third axis into 3 arrays to isolte red green and blue values of an rgb image)
# Each object created will have the same number of dimensions as the original array

# Stack arrays
# Remember that it is not possible to concatenate data in a new dimension. Instead we use stacking
# All arrays must have the same shape and number of dimensions
np.stack([array1, array2], axis=2) # axis 



# %% PYTHON DATA SCIENCE TOOLBOX 1

# Define a function
def square(value):   # function header, parameter
    new_value= value**2 # function body
    return new_value
square(5) # now 5 is the "argument"

# DOCSTRINGS
# Describe what your function does, serves as documentation
def square(value):   # function header, parameter
    """ Return the square of a value."""
    new_value= value**2 # function body
    return new_value

# Return multiple values
def raise_both(value1, value2):
    """ Raise value1 to the power of value2 and vice versa."""
    new_value1 = value1**value2
    new_value2 = value2**value1

    new_tuple=(new_value1, new_value2)

    return new_tuple
raise_both(2,3)

# SCOPE in functions
# Not all objects area ccessible everywhere in a script
# Scope: part of the program where an object or name may be accesbile 
# 2 types of scopes: global,local
# Global: defined in the main body of a script
# Local: name defined inside a function (when the function is done, the name ceases to exist)
# Built-in-scope: names in th epre-defined built-ins module
# If Python cannot find a name in the local scope, it will look in the upper scope until it reaches global

# Alter the value of a GLOBAL name WITHIN a function call
new_val = 10
def square(value):
    """ Return the square of a value."""
    global new_val # searches new_val in global environment
    new_value= new_val**2
    return new_value
square(5)

# See Python's built-in scope
import builtins
dir(builtins)

# NESTED functions
def mod2plus5(x1, x2, x3):
    """Returns the remainder plus 5 of three values."""

    def inner(x):
        """Returns the remainder plus 5 of a value"""
        return x % 2 + 5
    
    return(inner(x1), inner(x2), inner(x3))
print(mod2plus5(1,2,3))

# A function to return a function
def raise_val(n):
    """Return the inner function."""

    def inner(x):
        """Raise x to the power of n."""
        raised = x ** n
        return raised

    return inner
square = raise_val(2)
cube = raise_val(3)
print(square(4), cube(3))

# Create and changed names in an enclosing scope (the 'upper' scope)
def outer():
    """Prints the value of n."""
    n = 1

    def inner():
        nonlocal n # n's value in the enclosing scope ('outer') will be modified but whatever is done in this scope 
        n = 2
        print(n)
    inner()
    print(n)
outer()

# DEFAULT ARGUMENTS
def power(number, pow=1): # pow takes a default value of 1
    """Raise number to the power of powe."""
    new_value = number ** powreturn new_value
power(9,2)

# FLEXIBLE ARGUMENTS
def add_all(*args): # *args turns all arguments passed to the funtion into a tupple
# Args do not need to have a keyword
    """Sum all values in *args together."""
    sum_all = 0
    for num in args:
        sum_all += num
    return sum_all
add_all(1,4,5)
add_all(1,4,5,123,-76)
# Flexible amount of KEYWORD ARGUMENTS
def print_all(**kwargs):
    """"Print out key-value pairs in **kwargs."""
    for key, value in kwargs.items():
        print( key + ': ' + value)
print_all(name='Harry', job='student')

# LAMBDA FUNCTIONS
# A quicker way to write functions
raise_to_power = lambda x, y: x ** y # arguments: instructions
raise_to_power(3,5)
# ANONYMOUS FUNCTIONS
# Pass functions to sequences using map
nums = [3,7,5,9]
square_all = map(lambda num: num ** 2, nums) # apply this lambda function to the list "nums"
print(square_all) # returns a map object
print(list(square_all)) # returns results in a list
# Apply a lambda function in a filter // filter the elements of a list according to a condition
list1 = ['asedfa', 'da', 'sadasda'] # eg return strings with more than 2 characters
result = filter(lambda string: len(string)>2, list1)
print(list(result))
# Reduce() and lambda functions
# Reduce loops through the elements of a list, and performs the function over the result of the previous iteration (algo así)
from functools import reduce
stark = ['robb', 'sansa', 'arya', 'brandon', 'rickon']
result = reduce(lambda item1, item2: item1 + item2, stark)
print(result)

# ERROR HANDLING
# Catch exceptions with try-except clause
def sqrt(x):
    try:
        return x ** 0.5
    except TypeError: # here we catch only one kind of error
        print("x must be an int or float")
sqrt(1)
sqrt('1')
# Raise an error: when you wish your function not to work in specific circumnstances, regardless of whether Python would raise an error or not
sqrt(-1) # this runs ok with the previous function
def sqrt(x):
    if x<0:
        raise ValueError('x must be non-negative')
    try:
        return x ** 0.5
    except TypeError: # here we catch only one kind of error, but you can specify none, just write 'except'
        print("x must be an int or float")
sqrt(-1)


# %% PYTHON DATA SCIENCE TOOLBOX 2

## ITERATORS
# ITERABLE: an object that has an associated iter() method (an iterator)
# For example: lists, strings, dictionaries, range objects, and file connections are iterables, and have their associated iterators
# A for loop, for example, applies the function iter() "Under the hood" to an iterable object

# Iterate over a string
word = 'ask'
it = iter(word)
next(it)

# Star operator: unpack all elements of an iterator at once
word = 'ask'
it = iter(word)
print(*it)

# Iterate over the key-value pairs of a dictionary
dic = {'country':'ARG', 'city':'CABA'}
for key, value in dic.items():
    print(key, value)

# Iterate over file connections
file = open('file.txt')
it = iter(file)
print(next(it))

# ENUMERATE: takes an iterable as an argument and returns a tuple with pairs of the elements of the iterable and their index
list1 = ['vsd', 'asdq', 'asdf']
for index, value in enumerate(list1, start=0): # the default is to begin enumeration at 0
    print(index, value)

# ZIP: accepts an arbitrary number of iterables and returns an iterator of tuples
list1 = ['vsd', 'asdq', 'asdf']
list2 = ['ok', 'bye', 'hello']
print(list(zip(list1, list2)))
for z1, z2 in zip(list1, list2):
    print(z1, z2)
# Unpacking a zip object (retrieve original lists as tuples)
z1 = zip(list1, list2)
list1_ = zip(*z1)
print(list1_)

# Loading a file with iterators
# For example, to load heavy data into different chunks
# Here we calculate the sum of a column in different parts
import pandas as pd
total = 0
for chunk in pd.read_csv('file.csv', chunksize=1000):
    total =+ sum(chunk['col'])
print(total)

# LIST COMPREHENSIONS
# Format: [output expression for iterator in variable in iterable]
nums = [12, 8, 21, 3, 16]
new_nums = [num + 1 for num in nums]
print(new_nums)
# You can do this with any iterable. The components are: an iterable, an iterator variable (the members of the terable), and the output expression
# Create a list with a sequence of numbers
result = [num for num in range(11)] # from 0 to 11
print(result)
# Replace nested for-loops
[(num1, num2) for num1 in range(0,2) for num2 in range(6,8)]

# Nested list comprehensions: for example, create a matrix like:
matrix1 = [[0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4]]
matrix2 = [[col for col in range(5)] for row in range(5)]
matrix1==matrix2

# Conditionals in comprehensions
[num ** 2 for num in range(10) if num % 2 == 0] # eg: square all even numbers from 0 to 9
[num ** 2 if num % 2 == 0 else 0 for num in range(10)] # eg: square all even numbers from 0 to 9, and output 0 for odds
# You can include conditions on the output expression, as above, and also on the iterable
# Format: [output expression conditional on output for iterator variable in iterable conditional on iterable]

# DICTIONARY COMPREHENSIONS
# eg. dictionary of positive integers as keys and their negative counterparts as values
{num: -num for num in range(10)}

# Create a dictionary froma zip object
list1 = ['vsd', 'asdq', 'asdf']
list2 = ['ok', 'bye', 'hello']
dict(zip(list1, list2))

# GENERATOR EXPRESSIONS / GENERATORS
# Definition: it does not store the list/dictionary in memmory. It returns a generator object over which we can iterate to produce the elements of the list/dictionary
result = (2 * num for num in range(10))
for num in result:
    print(num)
result = (2 * num for num in range(10))
print(list(result))
result = (2 * num for num in range(10))
print(next(result))
# This is an example of LAZY EVALUATION: you delay the evaluation of an expression until the value is needed

# GENERATOR FUNCTIONS: functions that produce generator objects
# Eg: return a generator of values from 0 to n
def num_sequence(n):
    """Generate values from 0 to n."""
    i= 0
    while i < n:
        yield i
        i += 1
result = num_sequence(10)
print(type(result))
print(next(result))

# Create a generator for a file (to stream data)
def read_large_file(file_object):
    """A generator function to read a large file lazily."""
    # Loop indefinitely until the end of the file
    while True:
        # Read a line from the file: data
        data = file_object.readline()
        # Break if this is the end of the file
        if not data:
            break
        # Yield the line of data
        yield data
# Open a connection to the file
with open('world_dev_ind.csv') as file:
    # Create a generator object for the file: gen_file
    gen_file = read_large_file(file)
    # Print the first three lines of the file
    print(next(gen_file))
    print(next(gen_file))
    print(next(gen_file))

# Stream data in chunks with Pandas
df_reader = pd.read_csv('ind_pop.csv', chunksize=10)
print(next(df_reader))
for chunk in df_reader:
    print(chunk)