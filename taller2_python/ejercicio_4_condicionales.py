# ejercicio 4 sueldo de empleados con horas extra

print("bienvenido")
name = input("ingrese su nombre: ")
hours = float(input("ingrese las horas trabajadas: "))

value_hours = 4
extra_value = value_hours * 2

salary = hours * value_hours
extra_value = 0
if hours <= 48:
  salary = hours * value_hours
  print("el empleado:", name, "tiene un sueldo de:", salary)
else:
  hours >= 48
  extra_value = hours * value_hours
  print("el empleado con nombre:", name, "tiene un sueldo con sus extras de:", extra_value)