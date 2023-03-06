# 1) Realice un programa donde se soliciten dos números al usuario, después se de como resultado el residuo y 
# el cociente de la división entre n1 y n2.
n1=int(input('ingrese un numero: '))
n2=int(input('ingrese un numero: '))
co=n1//n2
re=n1%n2
print(f"el residuo es {re}")
print(f"el cosiente es {co}")

# 2) Realice un programa que calcule el índice de masa corporal de una persona, donde le solicite al usuario 
# la estatura en cm y el peso en Kg. Después imprima como resultado el índice de masa corporal mediante un 
# mensaje que diga “Su IMC es valor” redondeado con dos decimales. 
estatura=int(input('ingrese su estatura en cm: '))
peso=int(input('ingrese su peso en kg: '))
IMC=peso/(estatura)**2
print(f"Su IMC es {IMC:.2f} " )

# 3) Realice un programa donde se solicite al usuario escribir el precio final de un artículo o producto, con 
# el que después calculará e imprimirá en pantalla el valor del IVA y el valor bruto (precio antes de IVA) del 
# artículo o producto.
preciofinal=float(input('ingrese el precio final de su compra: '))
SIVA=1.19
IVA=19
valorbruto=preciofinal/SIVA
valorIVA=valorbruto*(IVA/100)
print(f"el valor del iva del producto es de {valorIVA:.3f} y el del precio bruto es de {valorbruto:.3f}")

# 4) Realice un programa que permita calcular el costo anual del consumo de combustible de un vehículo, si el 
# usuario ingresa la distancia recorrida (Km) anual, el consumo de combustible (L / 100Km) anual y el costo 
# promedio anual del combustible por litros recorridos ($ / L)
dr=int(input('ingrese la distacia recorrida: '))
cc=int(input('ingrese el consumo de combustible anual: '))
cp=float(input('ingrese el costo promedio anual del combustible: '))
la=dr*cc/100
ca=la*cp
print(f"El costo anual del consumo de combustible es de $ {ca}")
