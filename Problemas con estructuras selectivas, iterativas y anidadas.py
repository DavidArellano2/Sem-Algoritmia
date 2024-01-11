#Lopez Arellano Ricardo David
#Problemas con estructuras selectivas, iterativas y anidadas

def e01(): #raices
    print("    ");  
    print("   Programa para calcular la ecuacion cuadratica");
    a=float(input("Ingrese el termino 'a': "));
    b=float(input("Ingrese el termino 'b': "));
    c=float(input("Ingrese el termino 'c': "));
    d=(b**2-(4*a*c));

    if (d>0):
        print("El resultado es: ", d);
        print("Las raices de la ecuacion son reales y diferentes");
    if(d == 0):
        print("El resultado es: ", d);
        print("Las raices de la ecuacion seran iguales y reales", d);
    if(d<0):
        print("El resultado es: ", d);
        print("Las raices seran complejas", d);
        print("    ");    
e01();

def e02(): #factorial
    print("    ");  
    print("   Programa para calcular el factorial");
    num=int(input("Introduce un numero: "));
    fac=1
    for i in range (num):
        fac=fac*num
        num=num-1;
    print ("El numero es: ",fac);
    print("    ");
#e02();

def e03():
    print("    ");  
    print("   Programa para calcular los numeros primos");
    n=int(input("Introduce un numero: "));
    if (n > 1):
        cont=0
        for i in range (2,n):
            rest=n%i;
            if rest==0:
                cont+=1
        if cont==0:
            print("El {} es un numero primo ".format(n));
        else:
            print("El {} no es un numero primo".format(n));
    else:
        print("El{} no es un numero primo".format(n));   
e03();
  





    
