# ejercicio 8 suma o multiplicacion de dos numeros

print("ingrese lo solicitado")
# inicio
a = int(input("ingrese un numero para a: "))
b = int(input("ingrese un numero para b: "))

# proceso
addition = a + b
if a > 0 and b > 0:
  print("devido a que los dos numeros son positivos entonces se sumaran: ", addition)
elif a < -1 and b < -1:
  multiplication = -a * (-b)
  print("en este caso se multiplicara: ", multiplication)

