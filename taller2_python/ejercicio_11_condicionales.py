# ejercicio 11 descuentos de productos

# inicio
print("BIENVENIDO")

buys = int(input("ingrese el valor de sus compra para el descuento: "))

# desarrollo del ejercicio 

if buys <= 100:
  discount1 = 5
  amount_n1 = buys * (discount1 / 100)
  price_f1 = buys - amount_n1
  print("el precio fue de: ", price_f1)
  print("el descuento en pesos es de: ", amount_n1)
if buys >= 100 and buys <= 200:
  discount2 = 10
  amount_n2 = buys * (discount2 / 100)
  price_f2 = buys - amount_n2
  print("el precio en pesos es de: ", price_f2)
  print("el descuento es de: ", amount_n2)
else:
  discount3 = 15
  amount_n3 = buys * (discount3 / 100)
  price_f3 = buys - amount_n3
  print("el precio total en pesos fue de: ", price_f3)
  print("el descuento es de: ", amount_n3)