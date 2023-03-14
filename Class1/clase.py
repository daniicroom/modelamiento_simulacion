print("Hola bebe")

num = 2
print(type(num))


num2 = 3.14
print(type(num2))

print(num,  "-", num2)

word = "hola"
word2 = 'hola'
print(type(word))

#string
num3 = input("Ingrese el numero 3")
num4 = input("Ingrese el numero 4")


total = num3 + num4
print(total)

#entero
num3 = int(input("Ingrese el numero 3"))
num4 = int(input("Ingrese el numero 4"))

total = num3 + num4
print("la suma de los numeros es", total)

#booleano
isTrue = True
isFalse = False

#potencia
total = num3 ** num4
print(total)

#listas
miLista = [4,"hola", True]

miLista.append("cosa2")
miLista[0] = 103
print(miLista)

#imprime la la longitud de la lista
print(len(miLista))


#Tuplas
miTupla = ("item1", "itme2", 2)
print(miTupla[0])


#condicionales

if len(miLista) > 3:
    print("miLista es mayor")

elif len(miLista) < 2:
    print("Es menor")
else:
    print("No es mayor")

#for
for i in range(len(miLista)):
    print(miLista[i])

for i in miLista:
    print(i)


#while
counter = 0
while True:
    counter += 1
    print(counter)
    if counter >= 20:
        break


#switch
languaje = input("Ingrese el lenguaje")

match languaje:
    case "javascript":
        print("Eligió javascript")
    case "python":
        print("Eligió python")

    case _:
        print("default")
    





