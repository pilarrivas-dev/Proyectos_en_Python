num= int(input("¿Que operacion quieres realizar: 1.Suma, 2.Resta, 3. Multiplicacion y 4.Division?"))
numero1=int(input("Introduce el primer numero:"))
numero2=int(input("Introduce el segundo numero:"))

match(num):
    case(1):
        suma=numero1 + numero2
        print("El resultado de la suma es:", suma)

    case(2):
        resta=numero1 - numero2
        print("El resultado de la resta es:", resta)
    
    case(3):
        multi=numero1 * numero2
        print("El resultado de la resta es:", multi)

    case(4):
        divi=numero1 /  numero2
        print("El resultado de la division es:", divi)