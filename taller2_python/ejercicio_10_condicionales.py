# ejercicio 10 perimetro y area 

print("ingrese los valores.")

base = int(input("ingrese la base del cuadrilatero: "))
heigth = int(input("ingrese la altura del cuadrilatero: "))



if base == heigth:
  print("el cuadrilatero es un cuadrado.")
  side1 = int(input("ingrese el lado 1:"))
  side2 = int(input("ingrese el segundo lado:"))
  perimeter1 = 4 * base
  print("el perimetro es:", perimeter1)
  surface1 = side1 * side2
  print("la superfifice es:", surface1)
else:
  print("el cuadrilatero es un rectangulo.")
  perimeter2 = 2 * (base + heigth)
  print("el perimetro es:", perimeter2)
  surface2 = base * heigth
  print("la superficie es:", surface2)