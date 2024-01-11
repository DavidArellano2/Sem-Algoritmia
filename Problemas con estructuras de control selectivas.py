#Lopez Arellano Ricardo David

def e01(): #Numeros pares
    num= float(input("Escriba un número entero: "));
    if (num % 2 == 0)&(num>0):
        print("El número es par...");
    if (num<0):
        print ("Ingresa un numero valido...");
    print("     ");
#e01();

def e02(): #descuentos
    precio=float(input("Escribe el precio de tu producto comprado: "));
    desc1=precio-(precio*0.15);
    desc2=precio-(precio*0.08);
    if (precio>3000)&(precio>0):
        print("Se te aplicara un 15% de descuento y el costo sera: ",desc1);
    if (precio<3000)&(precio>0):
        print("Se te aplicara un 8% de descuento y el costo sera: ",desc2);
    if (precio<0):
        print("Ingresa un valor valido...")
    print("   ");
#e02();

def e03(): #calculadora
    dato1=float(input("Ingresa que quieres realizar:(suma=1, resta=2, multiplicacion=3 o division=4): "));
    dato2=float(input("Ingresa el primer valor: "));
    dato3=float(input("Ingresa el segundo valor: "));
    suma=(dato2+dato3);
    resta=(dato2-dato3);
    multi=(dato2*dato3);
    divi=(dato2/dato3);
    if (dato1 == 1):
        print("El resultado es: ",suma);
    if (dato1 == 2):
        print("El resultado es: ",resta);
    if (dato1 == 3):
        print("El resultado es: ",multi);
    if (dato1 == 4):
        print("El resultado es: ",divi);
e03();
     




#><
