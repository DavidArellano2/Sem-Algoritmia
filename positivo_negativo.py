#Equipo 5
#Lopez Arellano Ricardo David
#
#Positivo y negativo


print("                SUMA DE NÚMEROS")

suma_neg = suma_pos = 0
numero= int(input("Escriba un número o escriba '0' para salir: "))

while numero != 0:	
	if numero < 0:
		suma_neg = suma_neg + 1	
	elif numero > 0:
		suma_pos = suma_pos + 1	
	numero= int(input("Escriba un número o escriba '0' para salir: "))
		
print("La cantidad de números positivos ingresados es : ", suma_pos)
print("La cantidad de números negativos ingresados es: ", suma_neg)

