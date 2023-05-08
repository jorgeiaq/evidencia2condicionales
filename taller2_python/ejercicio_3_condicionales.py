# ejercicio 3 numero mayor y menor de tres numeros

print("ingrese tres numero")
number1 = input("digite el primer numero: ")
number2 = input("digite un segundo numero: ")
number3 = input("digite un ultimo numero: ")

if number1 > number2 and number1 > number3:
  eldery = number1
elif number2 > number3 and number2 > number1:
  eldery = number2
else: 
  eldery = number3

if number1 < number2 and number1 < number3:
  minor = number1
elif number2 < number1 and number2 < number3:
  minor = number2
else:
  minor = number3

print("el numero mayor es:", eldery)
print("el numero menor es:", minor)