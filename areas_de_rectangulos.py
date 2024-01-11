#Lopez Arellano Ricardo David
#

print("       Sacar el area de 2 rectangulos y compararlos:");
rec1b=float(input("Dame la base del rectangulo 1: "));
rec1a=float(input("Dame la altura del rectangulo 1: "));
rec2b=float(input("Dame la base del rectangulo 2: "));
rec2a=float(input("Dame la altura del rectangulo 2: "));
suma1=rec1b*rec1a
suma2=rec2b*rec2a

if (suma1==suma2):
    print("los rectangulos son iguales");

elif (suma1>suma2):
    print("El rectangulo 1 es mayor que el rectangulo 2");

elif (suma1<suma2):
    print("El rectangulo 2 es mayor que el rectangulo 1");

#<>
