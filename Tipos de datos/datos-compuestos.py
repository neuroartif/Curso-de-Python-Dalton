#Datos compuestos son datos que tienen dentro otros datos simples o compuestos que podemos agruparlos.
#En programación se cuenta del 0-9, en donde el 0 es la primera posición y el nueve, la última.
#En una lista tenemos índices y elementos, sindo el índice los números 0-9 y los elementos, ubicados en las posiciones dentro de la lista
#El elemento que ocupa la pocisión 1 representa el índice 0
#Paréntesis() Corchetes[] Llaves{}
#Matrices: Una lista[] es un tipo de matriz, la tupla() es otro tipo de matriz. Importante en la lista los datos se pueden modificar, en la tupla, no
#El array es otro tipo de matriz
lista = ["Pedro", "Neuroartif", True, 1.70]
tupla = ("Pedro", "Neuroartif", True, 1.70)

#print(lista [1])
#print(lista [0])
#Se puede comentar texto o comentar código, colocar # delante del código es comentar código. Print sirve para "presentar" el resultado de lo que hemos escrito

#Otro tipo de dato compuesto es el conjunto, para el mismo tenemos que utilizar una función llamada: "set", para los conjuntos utilizamos llaves{}
#En el conjunto se pueden redefinir los elementos, pero no podemos cambiarlos.
#Dentro de los conjuntos los datos no tienen una posición determinada o fija, por lo que no se puede acceder a los elementos por un índice
#En la lista y en la tupla pueden haber datos duplicados, pero en el conjunto no.
conjunto = {"Pedro", "Neuroartif", True, 1.70, "Pedro"}

#print(conjunto)

#Otro tipo de dato compuesto en el diccionario (dict). El diccionario tiene clave (key) y valor (value). Los valores se separan por coma.
diccionario = {
    'nombre' : "Pedro",
    'canal' : "Neuroartif",
    'esta_feliz' : True,
    'altura' : 1.70,
    'dato_duplicado' : "Pedro"
}

print(diccionario ['nombre'])
print(lista [0])

