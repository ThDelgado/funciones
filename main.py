#list para capturar reultado de operaciones aritmeticas

numeros = [] 
#funciones de operaciones aritmeticas

def sumar(a = int, b = int): 
    suma = a + b 
    numeros.append(suma) 
    return suma
  

def restar(a = int, b = int): 
    resta = a - b 
    numeros.append(resta) 
    return resta 

def multiplicar(a = int, b = int): 
    multiplicacion = a * b 
    numeros.append(multiplicacion) 
    return multiplicacion  

def dividir(a = int, b = int): 
    division =  a / b
    numeros.append(division) 
    return division 

# claves y valores para los diccionarios
keys= ["suma", "resta", "multiplicacion", "division"]
values = numeros #se obtine de la lista con todos los resultados de operaciones aritmeticas

# funcion para convertir a diccionario
def convertirDiccionario(a:str, b:int): 
    """
    une un string y un entero y los convierte en un diccionario
    """
    diccionario = dict(zip(a, b))
    return diccionario


#funcion para solicitar numeros y validarlos
def solicitar_dos_numeros():
 
    while True:
        print("Ingrese dos numeros para sumar, multiplicar, restar y dividir")
        numero2 = int(input("Ingrese un numero, mayor que cero: "))  
        numero1 = int(input("Ingrese un numero, mayor que el anterior: "))  
        
        if  numero2 > 0 and numero1 > numero2:
            return  numero1 , numero2
        else:
            print("Los numeros no son validos")



#funcion que ejecuta todas las operaciones aritmeticas
def operaciones_aritmeticas(a:int, b:int):
    sumar(a, b)
    restar(a, b)
    multiplicar(a, b)
    dividir(a, b)
    return




#solicitando los numeros
numeros_validos = solicitar_dos_numeros()

#accediendo a la tupla para obtener los numeros
numero1 = numeros_validos[0]
numero2 = numeros_validos[1]

#ejecutando operaciones aritmeticas
operaciones_aritmeticas(numero1, numero2)

#imprimiendo y ejecutando funcion del diccionario
print(convertirDiccionario(keys,values))
