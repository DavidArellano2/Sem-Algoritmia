#Ricardo David Lopez Arellano

def e01(): #area cubo
        dato1=float(input("Escribe la medida de la arista del cubo: "));
        arista=dato1*dato1*6
        print("El area del cubo es: ",arista);
        print ("    ");
e01();

        
def e02(): #velocidad auto
        dato1=float(input("Escribe la velocidad a la que va el auto: "));
        dato2=float(input("Cual es la velocidad maxima en ese camino: "));
        if (dato1>dato2):
                print ("Estas arriba del limite de veocidad...");
        if (dato1<dato2):
                print("No estas arriba del limite de velocidad :)");
        print("   ");
e02();

def e03(): #angulos
        valor1=float(input("Escribe el primer valor del angulo interno del triangulo (En grados): "));
        valor2=float(input("Escribe el segundo valor del angulo interno del triangulo (En grados): "));
        valor3=float(input("Escribe el tercer valor del angulo interno del triangulo (En grados): "));
        
        if (valor1+valor2+valor3>180):
                print ("Te excediste en los grados, no se puede formar un triangulo...");
                valor1=float(input("Escribe el primer valor del angulo interno del triangulo (En grados): "));
                valor2=float(input("Escribe el segundo valor del angulo interno del triangulo (En grados): "));
                valor3=float(input("Escribe el tercer valor del angulo interno del triangulo (En grados): "));
                
        if (valor1+valor2+valor3<180):
                print("Te hacen falta grados, no se puede formar un triangulo...");
                valor1=float(input("Escribe el primer valor del angulo interno del triangulo (En grados): "));
                valor2=float(input("Escribe el segundo valor del angulo interno del triangulo (En grados): "));
                valor3=float(input("Escribe el tercer valor del angulo interno del triangulo (En grados): "));
                
        if (valor1+valor2+valor3 == 180):
                print("Si se puede formar un triangulo :)");
        print("   ");
e03();
        


	
