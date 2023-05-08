# ejercicio 2 numero mayor y menor 

print("bienvenido al programa")
number1 = input("ingrese el primer numero: ")
other = input("ingrese otro numero")

if number1 > other:
  elderly = number1
if other > number1:
  elderly = other
if number1 < other:
  minor = number1
if other < number1:
  minor = other

print("el numero mayor es:", elderly)
print("el numero menor es:", minor)