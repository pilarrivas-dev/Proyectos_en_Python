s1=int(input("Introduce el primer ingreso:"))
s2=int(input("Introduce el segundo ingreso:"))

def sumar(s1,s2):
    resultado = s1 +s2
    return resultado

ingresos_totales = sumar(s1,s2)

print("Los ingresos totales son:", ingresos_totales)