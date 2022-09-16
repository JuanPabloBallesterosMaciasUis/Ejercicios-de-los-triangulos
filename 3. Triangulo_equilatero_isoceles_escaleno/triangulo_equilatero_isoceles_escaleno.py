# Ejercicio 3 :Dados 3 numeros a, b , c, determinar si un triangulo es equilatero, isoceles o escaleno. 

print("_________________________________________")
print("")
print("  TRIANGULO EQUILATERO ISOCELES ESCALENO ")
print("_________________________________________")

print("Se verefica si se puede realizar el triangulo")

#input

a = int(input("\nDigite el valor para el lado a del triangulo: \n"))
b = int(input("\nDigite el valor para el lado b del triangulo: \n"))
c = int(input("\nDigite el valor para el lado c del triangulo: \n"))

#process and output

bandera = True

if a + b > c :
    print("____________________________")
    print("Se puede formar el triangulo")
    bandera = True
    
elif b + c > a :
    print("____________________________")
    print("Se puede formar el triangulo")
    bandera = True
   
elif a + c > b :
    print("____________________________")
    print("Se puede formar el triangulo")
    bandera = True

else:
    print("________________________________")
    print("No se puede realizar el tringulo")
    bandera = False


if (bandera):
    if a == b == c:
        print("El triangulo es equilatero")

    elif a==b or a==c:

        print("El triangulo es isoceles")
    elif a!=b!=c:

        print("El triangulo es escaleno")