#la idea de variable es porque los datos contenidos pueden variar
#una varia es un espacio en la que almacenamos diversos datos
#las variables se declaran y se definen, la definición es el valor que tiene la variable
#ejemplo:
nombre = "miguel"

#una vez se declara la variable el valor de la misma se puede modificar o redefinir
nombre = "pedro"
nombre = "miguel"
        
#Variables numéricas 
a = 4
b = 10
c = a + b

nombre = "miguel"
nombre = 25 + 37
nombre = 17 - 48
nombre = 13 * 35
nombre = 132 / 27
nombre = 5 ** 3
nombre = 25 ** (1/2)

#Concatenacion con (+) : unir variables
nombre = "Miguel"
bienvenida = "Hola, " + nombre + " ¿Cómo estás?"

#Concatenar con (f-String) Para integrar numeros en el texto
nombre = "Pedro"
bienvenida = f"Hola, {nombre} ¿Cómo estás?"
nombre = "14"
bienvenida = f"Hola, {nombre} ¿Cómo estás?"

#Borrar datos de la memoria
nombre = "Pedro"
bienvenida = f"Hola, {nombre} ¿Cómo estás?"
del bienvenida
nombre = "14"
bienvenida = f"Hola, {nombre} ¿Cómo estás?"
nombre = "14"
bienvenida = f"Hola, {nombre} ¿Cómo estás?"
nombre = "14"
del bienvenida
bienvenida = f"Hola, {nombre} ¿Cómo estás?"

#Operadores de pertenencia (in, not in), sirven para encontrar elementos en nuestros datos, estos nos dan (True/False)
nombre = "Miguel"
bienvenida = f"Hola, {nombre} ¿Cómo estás?"
name = "Leiah"
welcome = f"Hello, {name} ¿How are you?"
#Ejemplo: print("hello" not in welcome) True - Negación de lo falso
#print("hello" in welcome) False - Afirmación de lo falso

#camelCase : sirve para poder poner varias palabras en una variable, se realiza escribiendo cada palabra siguiente con la inicial mayúscula
nombreCompletoDelUsuario = "Miguel"
bienvenida = f"Hola, {nombre} ¿Cómo estás?"
#snake_case : recomendado para separa palabras en las variables en Python
nombre_completo_del_usuario = "Miguel"
bienvenida = f"Hola, {nombre} ¿Cómo estás?"


print("hello" not in welcome)