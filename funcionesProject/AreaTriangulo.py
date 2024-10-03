#EJEMPLO PARA CALCULAR EL AREA DE TRIANGULO

#VARIABLES DE ENTRADAS
base = int(input("ingresa la base:"))
altura =int(input("ingrese la altura:"))

#proceso
def calcularAreaTriangulo(b,a):
    area = (b*a)/2
    return  area

#invocar la funcion
resultado = calcularAreaTriangulo(base,altura)
print("el area del triangulo es:",resultado)
print(f"el area del triangulo cuya base {base} y altura {altura}")


#funcion con argumenntos predeterminados
def my_function(country = "colombia"):
    print("I AM FROM "+ country)
# invocar la funcion
my_function()
my_function("sweden")

#argumentos arbitarios
def mostrarEstudiante(*args):
    print("el estudiante:"+args[2])

    #invocamos la funcion
    mostrarEstudiante("emil","tobias","linus","bil","andres")

    def mostrarcarros(carro1,carro2,carro3):
        print("el carro es:"+carro2)

  mostrarEstudiante(carro1= "BMW",carro3 ="ferrari",carro2="ford")

def mostracliente(**kwargs):
      print("su apellido es:"+kwargs["apellido"])

mostracliente(nombre = "tobias,",apellido="refesnes")

def mifuncion():
    pass

x = min(5,10,15)
y =max(5,10,15)
print(x)
print(y)
num1 = pow(7,4)
print(num1)
 import math

 num2=math.sqrt(34)
 print(num2)
 num3 = math.ceil(7.8)
 num4 = math.floor(7.8)
 print(num3)
 print(num4)