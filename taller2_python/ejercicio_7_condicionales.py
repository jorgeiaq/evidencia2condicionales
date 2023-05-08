# ejercicio 7 triangulo equilatero

print("ingrese lo solicitado para determinar si el triangulo es equilatero o no")
# variables side para los lados del triangulo
side1 = int(input("ingrese el lado 1 del triangulo: "))
side2 = int(input("ingrese el lado 2 del triangulo: "))
side3 = int(input("ingrese el ultimo lado del triangulo: "))

# proceso para determinar si el triangulo es equilatero

if side1 == side2 and side2 == side3:
  print("los tres datos son iguales esto significa que el triangulo es equilatero.")
else:
  print("no es equilatero.")