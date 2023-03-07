print('Escoja una de las siguientes opciones:\n')
print('1. programa que pida al usuario un número entero positivo y después imprima en pantalla todos los \n números impares desde el uno hasta dicho número separado por comas. \n')
print('2. programa que calcule el número factorial de un número seleccionado por el usuario. \n')
print('3. programa que solicite un número al usuario, despues indique si es primo o no; además imprima los \n número primos hasta este número.\n')

opc = input('Escoja una opcion: ')

if opc == '1':
    numero = int(input("Ingrese un número entero positivo: "))
    impares = ""
    for i in range(1, numero + 1, 2):
        impares += str(i) + ", "
    impares = impares[:-2]
    print("Los número impares desde el uno hasta", numero, ":")
    print(impares)

elif opc=='2':
    numero = int(input("Ingresa un número para calcular su factorial: "))
    factorial = 1
    if numero < 0:
        print("Lo siento, el factorial no está definido para números negativos.")
    elif numero == 0:
        print("El factorial de 0 es 1.")
    else:
        for i in range(1, numero + 1):
            factorial = factorial * i
        print("El factorial de", numero, "es", factorial)

elif opc=='3':
    num = int(input("Ingresa un número entero positivo: "))
    es_primo = True
    for i in range(2, num):
        if num % i == 0:
            es_primo = False
            break
    if es_primo:
        print(num, "es un número primo")
    else:
        print(num, "no es un número primo")
    print("Los números primos hasta", num, "son:")
    for i in range(2, num + 1):
        es_primo = True
        for j in range(2, i):
            if i % j == 0:
                es_primo = False
                break
        if es_primo:
            print(i)
