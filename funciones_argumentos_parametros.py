#
#
#

def main():
    print("\t OPERADORES ARITMETICOS")
    n1=int(input("Dame un numero: "))
    n2=int(input("Dame otro numero: "))
    suma(n1,n2)
    resta(n1,n2)
    multi(n1,n2)
    div1(n1,n2)
    div2(n1,n2)
    mod(n1,n2)
    exp(n1,n2)

def suma(n1,n2):
    suma=n1+n2
    print(n1, "+" ,n2, "=" ,suma)

def resta(n1,n2):
    resta=n1-n2
    print(n1, "-" ,n2, "=" ,resta)

def multi(n1,n2):
    multi=n1*n2
    print(n1, "x" ,n2, "=" ,multi)

def div1(n1,n2):
    div1=n1//n2;
    print(n1, "/" ,n2, "=" ,div1)

def div2(n1,n2):
    div2=n1/n2
    print(n1, "/" ,n2, "=" ,div2)

def mod(n1,n2):
    mod=n1%n2
    print(n1, "%" ,n2, "=" ,mod)

def exp(n1,n2):
    exp=n1**n2
    print(n1, "**" ,n2, "=" ,exp)
    
main()
