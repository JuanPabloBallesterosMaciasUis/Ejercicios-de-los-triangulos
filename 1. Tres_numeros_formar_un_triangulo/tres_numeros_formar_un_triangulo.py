# Ejercicio 1 :Dados 3 numeros a, b , c, verificar si puede formar los lados de un triangulo.

print("____________________________")
print("____FORMAR UN TRIANGULO_____")
print("____________________________")

#input
a = int(input("\nDigite el valor para el lado a del triangulo: \n"))
b = int(input("\nDigite el valor para el lado b del triangulo: \n"))
c = int(input("\nDigite el valor para el lado c del triangulo: \n"))

#process and output
if a + b > c :
    print("____________________________")
    print("Se puede formar el triangulo")
    
elif b + c > a :
    print("____________________________")
    print("Se puede formar el triangulo")
   
elif a + c > b :
    print("____________________________")
    print("Se puede formar el triangulo")

else:
    print("________________________________")
    print("No se puede realizar el tringulo")
    