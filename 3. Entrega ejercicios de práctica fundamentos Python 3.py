# %%
## Ejercicios de práctica Fundamentos Python (3)
## Nombre: Jhon Freddy Alvino Lozano

# %%
## A. Definir y llamar
## La función se crea una vez y se usa muchas veces

# %%
## 1. Definir una función
# Complete la palabra clave que define una función.

def saludar():
    print("Hola")

saludar()

# %%
## 2. Llamar a la función
# Complete la línea que ejecuta la función ya definida.

def bienvenida():
    print("Bienvenido al curso")

bienvenida()

# %%
## 3. Predice el orden de ejecución
# Sin ejecutar, determine en qué orden aparecen los mensajes.

def uno():
    print("A")

print("B")
uno()
print("C")

## Respuesta: B, A, C.
## Explicación: Primero se ejecuta la línea que está fuera (imprime B), luego la llamada a uno() imprime A, y por último se ejecuta el print final que imprime C.

# %%
## 4. Corrige el orden
# El programa falla porque la función se llama antes de existir. Reescriba el bloque completo en el orden correcto.

def saludar(nombre):
    print("Hola,", nombre)

saludar("Ana")

## Tu respuesta: En Python el código se lee de arriba hacia abajo. Si llamas a saludar("Ana") antes de escribir def saludar(...), el intérprete no reconoce el nombre de la función y genera un error de tipo NameError.

# %%
## 5. Función con un parámetro
# Complete el parámetro que recibe la función.

def saludar(nombre):
    print("Hola,", nombre)

saludar("Ana")

# %%
## 6. Función con dos parámetros
# Complete los parámetros necesarios para calcular el área.

def area(base, altura):
    return base * altura

print(area(3, 4))

# %%
## 7. Completa la llamada
# Complete los argumentos para obtener exactamente el resultado indicado.

def area(base, altura):
    return base * altura

print(area(5.0, 5.0))

# %%
## 8. Reutilizar la misma función
# Llame tres veces a la misma función con precios distintos.

def con_iva(precio):
    return precio * 1.19

print(con_iva(100))
print(con_iva(150))
print(con_iva(200))

# %%
## B. Parámetros y argumentos
## Lo que la función recibe para trabajar

# %%
## 9. Parámetro o argumento
# Observe la definición y la llamada, y distinga cada uno de los dos nombres.

def doble(n):
    return n * 2

resultado = doble(5)

## Respuesta: 'n' es el parámetro (la variable definida en la función) y 5 es el argumento (el valor real que le pasamos al llamarla).

# %%
## 10. Argumentos por posición
# Complete la llamada para que se imprima: Ana 20 Bogota.

def perfil(nombre, edad, ciudad):
    print(nombre, edad, ciudad)

perfil("Ana", 20, "Bogota")

# %%
## 11. Argumentos por nombre
# Complete los nombres de los parámetros para que el orden deje de importar.

def perfil(nombre, edad, ciudad):
    print(nombre, edad, ciudad)

perfil(edad=20, nombre="Ana", ciudad="Bogota")

# %%
## 12. Valor por defecto
# Complete el valor por defecto del parámetro saludo.

def saludar(nombre, saludo="Hola"):
    print(saludo, nombre)

saludar("Ana")

# %%
## 13. Reemplazar el valor por defecto
# Complete el argumento que sustituye al saludo por defecto.

def saludar(nombre, saludo="Hola"):
    print(saludo, nombre)

saludar("Luis", "Buen dia")

# %%
## 14. Orden de los parámetros
# El encabezado produce error porque los parámetros con valor por defecto van al final.

def registrar(producto, cantidad=1):
    print(producto, cantidad)

registrar("Cuaderno")

#Tu respuesta: Los parámetros obligatorios van siempre al inicio y los opcionales al final. Si se colocan al revés, Python se confunde al asignar los valores y genera un error de sintaxis.

# %%
## 15. Una lista como argumento
# Complete el recorrido para sumar todos los precios recibidos.

def total(precios):
    suma = 0
    for p in precios:
        suma = suma + p
    return suma

print(total([1200, 950, 3400]))

# %%
## C. return y resultados
## Lo que la función entrega al programa

# %%
## 16. Devolver un valor
# Complete la palabra clave que entrega el resultado.

def doble(n):
    return n * 2

print(doble(5))

# %%
## 17. Usar el valor devuelto
# Complete la llamada para guardar el resultado y operar con él.

def doble(n):
    return n * 2

resultado = doble(6)
print(resultado + 1)

# %%
## 18. Función sin return
# Sin ejecutar, determine qué imprimen las dos últimas líneas.

def saludo(nombre):
    print("Hola,", nombre)

x = saludo("Ana")
print(x)

## Respuesta: La primera línea sale por el print que está adentro de la función. La segunda imprime None porque la función no tiene un return que devuelva algún dato a la variable x.

# %%
## 19. print o return
# Corrija la función para que el resultado pueda seguir usándose en la suma.

def doble(n):
    return n * 2

total = doble(5) + 3
print(total)

## Respuesta: Se cambia print por return porque print solo muestra el dato en pantalla pero no guarda nada (devuelve None), lo que provoca un error al intentar sumar. Con return, la función entrega el resultado directamente al programa para poder usarlo en la operación y obtener 13.

# %%
## 20. return dentro de una condición
# Complete la instrucción que devuelve el segundo resultado.

def signo(n):
    if n < 0:
        return "negativo"
    return "positivo"

print(signo(-4))
print(signo(7))

# %%
## 21. return termina la función
# Sin ejecutar, determine qué se imprime y qué línea nunca se ejecuta.

def prueba(n):
    if n > 0:
        return "positivo"
    print("linea intermedia")
    return "otro"

print(prueba(5))

## Respuesta: Imprime "positivo". No sale la línea intermedia porque al cumplirse la condición n > 0, el primer return saca la ejecución de la función inmediatamente.

# %%
## 22. Devolver dos valores
# Complete la función para que entregue el mínimo y el máximo.

def resumen(valores):
    return min(valores), max(valores)

menor, mayor = resumen([8, 3, 10, 5])
print(menor, mayor)

# %%
## 23. Encadenar funciones
# Complete la llamada interna para calcular el precio con IVA redondeado.

def con_iva(p):
    return p * 1.19

def redondear(valor):
    return round(valor, 2)

print(redondear(con_iva(1200)))

# %%
## D. Ámbito y colecciones
## Qué vive dentro de la función y qué vive fuera

# %%
## 24. Variable local y global
# Sin ejecutar, determine qué imprime cada una de las dos llamadas.

mensaje = "global"

def prueba():
    mensaje = "local"
    print(mensaje)

prueba()
print(mensaje)

## Respuesta:
## local
## global

# %%
## 25. Evitar las variables globales
# Reescriba la función para que reciba el IVA como parámetro y no dependa de variables externas.

def con_iva(precio, iva=0.19):
    return precio * (1 + iva)

print(con_iva(1000))

## Respuesta: Al pasar el iva como parámetro dentro de la función, esta deja de depender de variables externas. Esto hace que el código sea autosuficiente, reusable y evita errores si el valor global cambia o desaparece.

# %%
## 26. No modificar el original
# Complete la función para que devuelva una lista nueva sin alterar la que recibe.

def agregar(lista):
    nueva = lista + [3]
    return nueva

datos = [1, 2]
print(agregar(datos))
print(datos)

# %%
## 27. Función que recibe una lista
# Complete la función que calcula el promedio de una lista de notas.

def promedio(notas):
    total = 0
    for n in notas:
        total = total + n
    return total / len(notas)

print(promedio([3.5, 4.2, 2.8]))

# %%
## 28. Función que recibe un diccionario
# Complete las claves para mostrar el nombre y la nota del estudiante.

def describir(alumno):
    print(alumno["nombre"], alumno["nota"])

describir({"nombre": "Laura", "nota": 4.6})

# %%
## 29. Función que devuelve una lista
# Complete el método que agrega elementos y el valor que se devuelve.

def aprobados(estudiantes):
    resultado = []
    for e in estudiantes:
        if e["nota"] >= 3.0:
            resultado.append(e["nombre"])
    return resultado

datos = [{"nombre": "Ana", "nota": 4.2}, {"nombre": "Luis", "nota": 2.8}]
print(aprobados(datos))

# %%
## Reto integrador
## Tres funciones que se llaman entre sí para producir un reporte

# %%
## 30. Reporte de notas con funciones
# Complete el programa que calcula el promedio de un estudiante, decide si aprueba y muestra el reporte.

def promedio(notas):
    total = 0
    for n in notas:
        total = total + n
    return total / len(notas)

def aprueba(prom, minimo=3.0):
    return prom >= minimo

def reporte(nombre, notas):
    prom = promedio(notas)
    print(nombre, round(prom, 2))
    if aprueba(prom):
        print("Aprobado")
    else:
        print("No aprobado")

reporte("Laura", [3.5, 4.2, 2.8])

## Respuesta:
## - promedio: Recibe una lista de números (notas) y retorna el valor numérico del promedio.
## - aprueba: Recibe el valor del promedio y una nota mínima requerida; retorna un valor booleano (True o False).
## - reporte: Recibe una cadena de texto (nombre) y una lista de notas; no retorna ningún valor (devuelve None), solo imprime en pantalla la información formateada.

# %%
## Autoevaluación rápida

## 1. ¿Puedo definir una función y llamarla en el orden correcto?
## Respuesta: Sí, declarando siempre la función primero con 'def' antes de intentar llamarla más adelante en el script.

## 2. ¿Puedo distinguir entre un parámetro y un argumento?
## Respuesta: Sí, el parámetro es el nombre de la variable definida dentro de la función y el argumento es el dato real que le enviamos al usarla.

## 3. ¿Puedo explicar la diferencia entre print y return?
## Respuesta: Sí, 'print' únicamente muestra texto en la consola pero no guarda nada, mientras que 'return' nos entrega un resultado para guardarlo en variables o usarlo en otras partes del código.

## 4. ¿Puedo decidir cuándo conviene extraer una función?
## Respuesta: Sí, cuando veo que estoy repitiendo bloques de código o para organizar tareas específicas dentro de mi programa.