#Un condicional es un pedazo de código que nos indica que:
#Si un código es True, se ejecuta / si es False, no se ejecuta
#También puede implicar lo contrario:
#Si el primer código es True, no se ejecuta el contrario / si es False, se ejecuta el contrario
#Ejemplos estructura:
#if condicion:
#    comparación
#if True:
    #acción se ejecuta
#if False:
    #acción no se ejecuta

edad = 16

if edad >= 18:
    print("puede pasar")

else:
    print("no puedes pasar")
    
#Todo lo que esta dentro del bloque forma parte de la condición

contraseña_almacena = "neuroartif007"
contraseña_escrita = "Leaiha2017"

if contraseña_almacena == contraseña_escrita:
    print("iniciando seccion")

else:
    print("contraseña equivocada, vulva a intentar")
    