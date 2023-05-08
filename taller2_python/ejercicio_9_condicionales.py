# ejercicio 9 signo zodiacal

# incicio del programa
print("ingresa tu dia nacimiento correspondiente a este se le dara su signo zodiacal.")
# variables day y month para el ejercicio
day = int(input("ingrese su dia de nacimiento: "))
month = int(input("ingresa tu mes de nacimiento: "))

if month == 3 and day >= 21 or month == 4 and day <= 19:
  print("tu signo es aries.")
elif month == 4 and day >= 20 or month == 5 and day <= 20:
  print("tu signo es tauro.")
elif month == 5 and day >= 21 or month == 6 and day <= 20:
  print("tu signo es geminis.")
elif month == 6 and day >= 21 or month == 7 and day <= 22:
  print("tu signo es cancer.")
elif month == 7 and day >= 23 or month == 8 and day <= 22:
  print("tu signo es leo.")
elif month == 8 and day >= 23 or month == 9 and day <= 22:
  print("tu signo es virgo.")
elif month == 9 and day >= 23 or month == 10 and day <= 22:
  print("tu signo es libra.")
elif month == 10 and day >= 23 or month == 11 and day <= 21:
  print("tu signo es escorpio.")
elif month == 11 and day >= 22 or month == 12 and day <= 21:
  print("tu signo es sagitario.")
elif month == 12 and day >= 22 or month == 1 and day <= 19:
  print("tu signo es capricornio.")
elif month == 1 and day >= 20 or month == 2 and day <= 18:
  print("tu signo es acuario.")
elif month == 2 and day >= 19 or month == 3 and day <= 20:
  print("tu signo es picis.")