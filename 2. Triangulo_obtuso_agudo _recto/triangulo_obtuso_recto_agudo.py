# Ejercicio 2 :Dados 3 numeros a, b , c, determinar si un triangulo es obtuso recto o agudo.

print("_______________________________________")
print("")
print("   TRIANGULO OBTUSO AGUDO O RECTO")
print("_______________________________________")

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

    if c**2 < a**2 + b**2:
        print("_____________________")
        print("Es un triangulo agudo")
        print("")

    elif c**2 == a**2 + b**2:
        print("_____________________")
        print("Es un triangulo recto")
        print("")

    elif c**2 > a**2 + b**2:
        print("______________________")
        print("Es un triangulo obtuso")
        print("")

    
