# ejercicio 12 año bisiesto

print("BIENVENIDO")

february = int(input("ingrese un dia del mes de febrero: "))

if february <= 28:
  print("el año es normal")
elif february == 29:
  print("el año es bisiesto")