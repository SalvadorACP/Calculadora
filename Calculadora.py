
# Funciones para realizar operaciones matemáticas
def suma(a, b):
    return print(a + b)

def resta(a, b):
    return print(a - b)

def multiplicacion(a, b):
    return print(a * b)

def division(a, b):
    if b == 0:
        return 'Error: División por cero'
    return print(a / b)

print("Ingrese los numeros para sumar")
a=float(input(print("Ingrese el numero uno")))
b=float(input(print("Ingrese el numero dos")))
resultado=suma(a,b)
print(resultado)

print("Ingrese los numeros para restar")
a=float(input(print("Ingrese el numero uno")))
b=float(input(print("Ingrese el numero dos")))
resultado=resta(a,b)
print(resultado)

print("Ingrese los numeros para multiplicar")
a=float(input(print("Ingrese el numero uno")))
b=float(input(print("Ingrese el numero dos")))
resultado=multiplicacion(a,b)
print(resultado)

print("Ingrese los numeros para dividir")
a=float(input(print("Ingrese el numero uno")))
b=float(input(print("Ingrese el numero dos")))
resultado=division(a,b)
print(resultado)