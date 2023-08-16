import re
import ply.lex as lex
from tabulate import tabulate

#Se contará cuaántas veces aparece un Token especifico en la entrada
#Contadores
num_count=0
roman_count=0
bin_count=0
hex_count=0
oct_count=0



"""
@date: 11/8/2023
@description: Convierte un numero en decimal a otro sistema numérico destino
@params: numero (número decimal a convertir), opcion_salida (Cadena que indica el sistema al que se desea convertir)
@return: El número escrito en el sistema decimal indicado
"""
def convertir(numero, opcion_salida):
    try: 
        # Convertir a la opción de salida
        if opcion_salida == "Binario":
            resultado = bin(int(numero))[2:]
        elif opcion_salida == "Octal":
            resultado = oct(int(numero))[2:]
        elif opcion_salida == "Decimal":
            resultado = str(numero)
        elif opcion_salida == "Hexadecimal":
            resultado = hex(int(numero))[2:]
        elif opcion_salida == "Romano":
            resultado = convertirRomano(numero)
        else:
            print("Opción de salida inválida.")
            return None
    except ValueError:
        print("Has ingresado un valor no válido")

    return resultado

"""
@date: 11/8/2023
@description: Convierte un numero decimal a un número romano
@params numero (Numéro en decimal a convertir)
@return numeroRomano
"""
def convertirRomano(numero):
    numero_descompuesto=[]
    numero_romano=""
    tamanio = len(numero) #Guarda el tamaño del número
    for i in numero:
        numero_descompuesto.append(int(i)) #Guarda cada digito en un arreglo. En la posición 0 se encuentra el de mayor valor posicional
    if tamanio==4:
        #millares
        numero_romano +=letrasRomanas(numero_descompuesto[0],"millar")
        #Centenas
        numero_romano+=letrasRomanas(numero_descompuesto[1],"centena")
        #Decenas
        numero_romano+=letrasRomanas(numero_descompuesto[2], "decena")
        #Unidades
        numero_romano+=letrasRomanas(numero_descompuesto[3], "unidad")

    elif tamanio==3:
        #Centenas
        numero_romano+=letrasRomanas(numero_descompuesto[0],"centena")
        #Decenas
        numero_romano+=letrasRomanas(numero_descompuesto[1], "decena")
        #Unidades
        numero_romano+=letrasRomanas(numero_descompuesto[2], "unidad")

    elif tamanio==2:
        #Decenas
        numero_romano+=letrasRomanas(numero_descompuesto[0], "decena")
        #Unidades
        numero_romano+=letrasRomanas(numero_descompuesto[1], "unidad")

    elif tamanio==1:
        #Unidades
        numero_romano+=letrasRomanas(numero_descompuesto[0], "unidad")

    return numero_romano



"""
@date: 11/8/2023
@description: Dependiendo de la posición será el valor para el número en el sistema romano. La función evalúa posición para retornar su valor
@params: numero (valor numérico a convertir), valorPosicional (indica si es millar, centena, etc)
@return: Retorna la cadena de letras romanas correspondientes al valor numérco enviado
"""
def letrasRomanas(numero, valorPosicional):
    if valorPosicional=="millar":
        if numero==1:
            return "M"
        elif numero==2:
            return "MM"
        elif numero==3:
            return "MMM"
        
    elif valorPosicional=="centena":
        if numero==1:
            return "C"
        elif numero==2:
            return "CC"
        elif numero==3:
            return "CCC"
        elif numero==4:
            return "CD"
        elif numero==5:
            return "D"
        elif numero==6:
            return "DC"
        elif numero==7:
            return "DCC"
        elif numero==8:
            return "DCCC"
        elif numero==9:
            return "CM"
    
    elif valorPosicional=="decena":
        if numero==1:
            return "X"
        elif numero==2:
            return "XX"
        elif numero==3:
            return "XXX"
        elif numero==4:
            return "XL"
        elif numero==5:
            return "L"
        elif numero==6:
            return "LX"
        elif numero==7:
            return "LXX"
        elif numero==8:
            return "LXXX"
        elif numero==9:
            return "XC"
        
    elif valorPosicional=="unidad":
        if numero==1:
            return "I"
        elif numero==2:
            return "II"
        elif numero==3:
            return "III"
        elif numero==4:
            return "IV"
        elif numero==5:
            return "V"
        elif numero==6:
            return "VI"
        elif numero==7:
            return "VII"
        elif numero==8:
            return "VIII"
        elif numero==9:
            return "IX"
    return " "

print("-"*20)
print("Prueba de las funciones de conversión")
romano=convertir("525","Romano")
binario=convertir("10","Binario")
print("Convertimos 525 a romano y 10 a binario")
print(romano)
print(binario)







"""
@description: Función para leer un archivo
@date: 15/08/2023
@params: nombre_del_archivo

"""
def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
            return contenido
    except FileNotFoundError:
        return "El archivo no fue encontrado"
    except Exception as e:
        return f"Ocurrió un error: {e}"



"""
@descrption: Analizador lexico con ply
@date: 15/8/2023
"""
#Declaración de palabras clave. Para nuestro proyecto son las palabras que indican el destino de conversión
#Las claves del diccionario son los lexemas y los valores son el nombre del token
reservadas = {
    'Romano' : 'ROMANO',
    'Binario' : 'BINARIO',
    'Octal' : 'OCTAL',
    'Hexadecimal' : 'HEXADECIMAL'
}


#Declara la lista de los tokens y concatenamos la lista de las palabras reservadas
tokens= ['NUMERO','EOF','ID']+list(reservadas.values())


#Indicarle que carácteres deben ser ignorados
t_ignore=' \t'

"""
@description: Reconoce los tokens de tipo NUMERO, esta función será llamada cuando se encuentre un token correspondiente al patrón
@date: 15/8/2023
"""
def t_NUMERO(t):
    r'\d+'  #Patrón para identifica los números enteros positivos 
    try:
        global num_count
        num_count+=1
        t.value = int(t.value)
    except ValueError:
        print("Ha ocurrido un error %d", t.value)
        t.value=0
    return t


"""
@description: Reconoce los tokens que son palabras reservadas, esta función será llamada cuando se encuentre un token correspondiente al patrón
@date: 15/8/2023
"""

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    try:
        t.type = reservadas.get(t.value,'ID')
        if t.value=="Romano":
            global roman_count
            roman_count+=1   
        elif t.value=="Hexadecimal":
            global hex_count
            hex_count+=1  
        elif t.value=="Binario":
            global bin_count
            bin_count+=1  
        elif t.value=="Octal":
            global oct_count
            oct_count+=1   
    except ValueError:
        print("Ha ocurrido un error %d", t.value)
        t.value=0
    return t

"""
@description: Para carácteres que no están contemplados dentro de algún token
@date: 15/8/2023
"""
def t_error(t):
    print("caracter ilegal'%s'" % t.value[0])
    t.lexer.skip(1)


"""
@description: Actualiza el número de línea 
@date: 15/8/2023
"""
def t_LINEA(t):
    r'\n+'
    t.lexer.lineno+=len(t.value) #t.value contiene el valor del token actual. Es una cadena que puede tener 1 o más \n 



"""
@description: Identifica el carácter final del documento
@date: 15/8/2023
"""

def t_EOF(t):
    r'\$'
    return t




#Construyendo el analizador
lexer = lex.lex()



"""
Programa principal

"""


nombre_archivo = "entrada.txt"  
contenido_archivo = leer_archivo(nombre_archivo)
print("*"*40)
print("Lectura e impresión del archivo txt")
print(contenido_archivo)
print("*"*40)


#Variable para almacenar los datos de la tabla de información principal
datos=[]


print("\n"*2)
print("*"*40)
print("Información del analizador léxico")
print("*"*40)
lexer.input(contenido_archivo)
for tok in lexer:
    datos.append([tok.type,tok.value, tok.lineno])


#Encabezados de la tabla de información principal
encabezados=["Tipo de Token","Valor","Número de línea"]

#Generar la tabla primaria
tabla = tabulate(datos,encabezados, tablefmt="grid")

print(tabla)

print("\n"*2)
print("*"*40)
print("Información secundaria")
print("El token NUMERO aparece %d veces en el archivo de entrada" %num_count)
print("El token ROMANO aparece %d veces en el archivo de entrada" %roman_count)
print("El token OCTAL aparece %d veces en el archivo de entrada" %oct_count)
print("El token HEXADECIMAL aparece %d veces en el archivo de entrada" %hex_count)
print("El token BINARIO aparece %d veces en el archivo de entrada" %bin_count)



"""
@description: Obtiene y ordena los datos para realizar las operaciones
@params: contenido_archivo. Cadena de texto a leer
@date: 15/8/2023
@return: arreglo_operaciones. Arreglo a retornar

"""

def obtenerOperaciones(contenido_archivo):
    expresion_regular = r'(\d+Romano|\d+Binario|\d+Octal|\d+Hexadecimal|\d+Aleatorio)'
    arreglo_operaciones = re.findall(expresion_regular, contenido_archivo)
    return arreglo_operaciones

print("\n"*2)
print("*"*40)
print("Información del analizador léxico")
print("*"*40)
resultado_arreglo_operaciones=obtenerOperaciones(contenido_archivo)
print(resultado_arreglo_operaciones)


"""
@description: Procesa el arreglo_operaciones para generar una salida
@date: 15/8/2023
@params: arreglo_operaciones
"""
def realizarConversiones(arreglo):
    resultados=[]
    for elemento in arreglo:
        match = re.match(r'(\d+)(\w+)', elemento)
        if match:
            numero = match.group(1)
            conversion = match.group(2)
            resultado=convertir(numero, conversion)
        else:
            resultado="Operación desconocida"
        resultados.append(resultado)
    return resultados


#Resultados de conversión
print("\n"*2)
print("*"*40)
print("Resultados de la conversión")
print("*"*40)
resultados_conversion=realizarConversiones(resultado_arreglo_operaciones)
print(resultados_conversion)