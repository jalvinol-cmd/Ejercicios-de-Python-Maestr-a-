# %%
## Ejercicios de práctica Fundamentos Python (4)
## Programación orientada a objetos

# %%
## A. Clases y objetos
## Definir la plantilla y crear ejemplares

# %%
## 1. Su primera clase
# Complete la definición para que la clase guarde el nombre y la edad de una persona.

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

p = Persona("Ana", 21)
print(p.nombre, p.edad)

# %%
## 2. Crear varios objetos
# Cree tres objetos distintos a partir de la misma clase y muestre el nombre de cada uno.

a = Persona("Ana", 21)
b = Persona("Luis", 30)
c = Persona("Carlos", 25)

for x in [a, b, c]:
    print(x.nombre)

# %%
## 3. Leer y modificar un atributo
# Lea el valor actual del atributo, modifíquelo y compruebe que el cambio quedó guardado.

p = Persona("Luis", 30)
print(p.edad)
p.edad = 31
print(p.edad)

# %%
## 4. Objetos independientes
# Complete y responda: al cambiar la edad de un objeto, ¿qué ocurre con el otro?

a = Persona("Ana", 21)
b = Persona("Ana", 21)
a.edad = 40
print(a.edad, b.edad)

## Su respuesta: Al modificar la edad del objeto 'a', el objeto 'b' permanece en 21. Cada instancia ocupa un espacio de memoria totalmente independiente con sus propios valores.

# %%
## 5. La clase no guarda datos
# Explique por qué la siguiente línea produce un error y corríjala para que imprima el nombre de un objeto.

p = Persona("Ana", 21)
print(p.nombre)

## Su respuesta: Produce AttributeError porque 'nombre' es un atributo de instancia (definido con self en __init__) y no de clase. No existe dentro del molde 'Persona', sino dentro de cada objeto instanciado a partir de ella.

# %%
## B. Atributos y métodos
## Lo que el objeto sabe y lo que el objeto hace

# %%
## 6. Un método que consulta
# Escriba el método para que devuelva True cuando la nota sea mayor o igual que 3.0.

class Estudiante:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def aprobo(self):
        return self.nota >= 3.0

print(Estudiante("Ana", 4.2).aprobo())

# %%
## 7. Un método que modifica
# Complete el método para que suba la nota sin superar nunca 5.0 y devuelva el nuevo valor.

class Estudiante:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def aprobo(self):
        return self.nota >= 3.0

    def subir(self, puntos):
        self.nota = min(5.0, self.nota + puntos)
        return self.nota

e = Estudiante("Luis", 4.8)
print(e.subir(0.5))

# %%
## 8. Método con parámetros
# Agregue un método que reciba una nota nueva y devuelva el promedio entre la nota guardada y la recibida, con dos decimales.

class Estudiante:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def aprobo(self):
        return self.nota >= 3.0

    def subir(self, puntos):
        self.nota = min(5.0, self.nota + puntos)
        return self.nota

    def promedio_con(self, otra):
        return round((self.nota + otra) / 2, 2)

e = Estudiante("Sara", 3.0)
print(e.promedio_con(4.0))

# %%
## 9. Atributo de clase
# Complete el contador para que registre cuántos objetos se han creado en total.

class Estudiante:
    total = 0

    def __init__(self, nombre):
        self.nombre = nombre
        Estudiante.total += 1

Estudiante("Ana")
Estudiante("Luis")
print(Estudiante.total)

# %%
## 10. ¿De instancia o de clase?
# Indique junto a cada atributo si debería ser de instancia o de clase, y justifique el último caso.

# codigo_curso = "20000151" -> Atributo de clase
# self.nombre = nombre       -> Atributo de instancia
# self.nota = nota           -> Atributo de instancia
# nota_minima = 3.0          -> Atributo de clase

## Su respuesta: 'nota_minima' y 'codigo_curso' son atributos de clase porque son compartidos globalmente por toda la entidad. 'nombre' y 'nota' son de instancia porque cada estudiante tiene valores propios particulares.

# %%
## 11. Encontrar el error
# El código no funciona. Identifique las dos fallas, corríjalas y escriba abajo qué mensaje mostraba Python.

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def con_iva(self):
        return self.precio * 1.19

p = Producto("Laptop", 1000)
print(p.con_iva())

## Su respuesta:
## Fallas:
## 1. El constructor estaba escrito como '__init' (sin doble guion bajo al final) y le faltaba el parámetro 'self'.
## 2. Las asignaciones en el constructor no usaban 'self.' para asociar los datos al objeto.
## 3. El método 'con_iva' no recibía 'self' como parámetro para poder acceder a 'self.precio'.
## Mensaje de error original: TypeError: __init__() takes 2 positional arguments but 3 were given o NameError: name 'precio' is not defined.

# %%
## C. Encapsulamiento y métodos especiales
## Proteger el estado interno y personalizar el objeto

# %%
## 12. Atributo privado
# Complete la clase para que el saldo no pueda modificarse directamente desde fuera.

class Cuenta:
    def __init__(self, saldo):
        self._saldo = saldo

    def consultar(self):
        return self._saldo

c = Cuenta(100)
print(c.consultar())

# %%
## 13. Validar antes de modificar
# Escriba el método para que rechace los valores menores o iguales que cero y devuelva el saldo actualizado en los demás casos.

class Cuenta:
    def __init__(self, saldo):
        self._saldo = saldo

    def consultar(self):
        return self._saldo

    def consignar(self, valor):
        if valor <= 0:
            return "Valor inválido"
        self._saldo += valor
        return self._saldo

c = Cuenta(100)
print(c.consignar(-20))
print(c.consignar(50))

# %%
## 14. Retirar con control de saldo
# Escriba el método para rechazar retiros mayores al saldo y actualizar el saldo cuando sea válido.

class Cuenta:
    def __init__(self, saldo):
        self._saldo = saldo

    def consultar(self):
        return self._saldo

    def consignar(self, valor):
        if valor <= 0:
            return "Valor inválido"
        self._saldo += valor
        return self._saldo

    def retirar(self, valor):
        if valor > self._saldo:
            return "Fondos insuficientes"
        self._saldo -= valor
        return self._saldo

c = Cuenta(100)
print(c.retirar(200))
print(c.retirar(40))

# %%
## 15. __str__: una vista legible
# Personalice la representación en formato texto del objeto.

class Estudiante:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def __str__(self):
        return f"{self.nombre}: {self.nota}"

print(Estudiante("Ana", 4.2))

# %%
## D. Herencia y polimorfismo

# %%
## 16. Heredar de una clase base
# Haga que Estudiante herede de Persona utilizando super().__init__().

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

class Estudiante(Persona):
    def __init__(self, nombre, nota):
        super().__init__(nombre)
        self.nota = nota

print(Estudiante("Ana", 4.2).nombre)

# %%
## 17. Sobrescribir un método
# Redefina el método saludar en la clase hija para incluir la nota.

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        return f"Hola, soy {self.nombre}"

class Estudiante(Persona):
    def __init__(self, nombre, nota):
        super().__init__(nombre)
        self.nota = nota

    def saludar(self):
        return f"Soy {self.nombre} y mi nota es {self.nota}"

print(Estudiante("Ana", 4.2).saludar())

# %%
## 18. Una llamada, varias respuestas
# Recorra una lista con objetos heterogéneos ejecutando la misma llamada de método.

grupo = [Persona("Sara"), Estudiante("Ana", 4.2)]
for p in grupo:
    print(p.saludar())

# %%
## 19. ¿Herencia o composición?
# Asigne el tipo de relación correspondiente a cada escenario.

# Un docente es una persona           -> Herencia ("es un")
# Un curso tiene estudiantes          -> Composición ("tiene un")
# Una cuenta de ahorros es una cuenta -> Herencia ("es un")
# Una biblioteca tiene libros         -> Composición ("tiene un")

# %%
## E. Reto integrador

# %%
## 20. La clase Curso
# Complete la clase para administrar una lista de estudiantes e inscribir y calcular promedio.

class Estudiante:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def aprobo(self):
        return self.nota >= 3.0

class Curso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiantes = []

    def inscribir(self, estudiante):
        self.estudiantes.append(estudiante)

    def promedio(self):
        if len(self.estudiantes) == 0:
            return 0
        suma = sum(e.nota for e in self.estudiantes)
        return round(suma / len(self.estudiantes), 2)

c = Curso("Python")
c.inscribir(Estudiante("Ana", 4.2))
c.inscribir(Estudiante("Luis", 2.8))
print(c.promedio())

# %%
## 21. El reporte del curso
# Construya el método para generar el resumen de aprobados y señalar al mejor estudiante.

class Curso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiantes = []

    def inscribir(self, estudiante):
        self.estudiantes.append(estudiante)

    def promedio(self):
        if len(self.estudiantes) == 0:
            return 0
        suma = sum(e.nota for e in self.estudiantes)
        return round(suma / len(self.estudiantes), 2)

    def reporte(self):
        if not self.estudiantes:
            return "Sin estudiantes registrados"
        aprobados = 0
        mejor = self.estudiantes[0]
        for e in self.estudiantes:
            if e.aprobo():
                aprobados += 1
            if e.nota > mejor.nota:
                mejor = e
        return f"{aprobados} aprobados | mejor: {mejor.nombre}"

c = Curso("Python")
c.inscribir(Estudiante("Ana", 4.2))
c.inscribir(Estudiante("Luis", 2.8))
print(c.reporte())

# %%
## 22. Diseñe usted la clase
# Implemente la estructura para Vehiculo y Parqueadero.

class Vehiculo:
    def __init__(self, placa, tipo, hora_entrada):
        self.placa = placa
        self.tipo = tipo
        self.hora_entrada = hora_entrada

class Parqueadero:
    def __init__(self):
        self.vehiculos = []

    def recibir(self, vehiculo):
        self.vehiculos.append(vehiculo)

    def entregar(self, placa):
        for v in self.vehiculos:
            if v.placa == placa:
                self.vehiculos.remove(v)
                return v
        return None

    def contar(self):
        return len(self.vehiculos)

pq = Parqueadero()
pq.recibir(Vehiculo("XYZ123", "Automóvil", "08:00"))
pq.recibir(Vehiculo("ABC456", "Motocicleta", "08:30"))
print(pq.contar())
pq.entregar("XYZ123")
print(pq.contar())