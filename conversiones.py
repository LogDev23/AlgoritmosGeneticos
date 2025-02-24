import math
import re
#Entrada de Individuos en formato binario separado por comas
indBin = input('Ingrese individuos binarios separados por comas>>> ')

#Obteniendo la Función de activación
fnAdap = input('ingrese la función de adaptación: f(x)= ')

# Obteniendo el Mínimo y Máximo de la función
minMax = input('ingrese el máximo y el mínimo separados por comas>>> ')

# Eliminando posibles espacios en blanco entre cada valor
indSnEsp = indBin.replace(' ', '')
fnAdSnEsp = fnAdap.replace(' ', '')
minMaxSnEsp = minMax.replace(' ', '')

# Creando listas de los datos sin espacios (Parametro para separar; las comas)
lstBinaria = indSnEsp.split(',')
lstMinMax = [int(i) for i in minMaxSnEsp.split(',')]  # Conversión a entero

#Obteniendo 'L'
l = len(lstBinaria[0])

# Validando que todos los individuos tengan la misma longitud
for val in lstBinaria:
    if len(val) != l:
        print('El individuo ' + val + ' no cumple con la longitud del primer elemento')
        break

# Comprobando Máximos y mínimos, siempre en la posición '0' debe ir el máximo
if lstMinMax[0] < lstMinMax[1]:
    temp = lstMinMax[0]
    lstMinMax[0] = lstMinMax[1]
    lstMinMax[1] = temp

# Convirtiendo cada valor binario en decimal y guardándolo en una lista nueva
lstDecimal = []
for ind in lstBinaria:
    dec = int(str(ind), 2)
    lstDecimal.append(dec)

#Imprimiendo el resultado de la conversión 
print('\n' + '>>>>>Los individuos en decimal son:', lstDecimal)

# Convirtiendo de decimal a real
valReal = []  #Creamos una lista para guardar el valor real de los individuos
for vCad in lstDecimal:
    xReal = lstMinMax[1] + vCad * ((lstMinMax[0] - lstMinMax[1]) / ((2 ** l) - 1))  # Fórmula para obtener Xreal
    valReal.append(round(xReal, 3))  # Agregamos los valores reales a una lista y truncamos el resultado a 3 decimales

# Imprimimos el valor real de los individuos
print('\n' + '>>>>>Los Valores reales son:', valReal)

# Definir un diccionario de funciones matemáticas disponibles para eval, devolviendo resultados en grados
math_functions = {
    'sin': lambda x: math.degrees(math.sin(math.radians(x))),
    'cos': lambda x: math.degrees(math.cos(math.radians(x))),
    'tan': lambda x: math.degrees(math.tan(math.radians(x))),
    'sqrt': math.sqrt,
    'log': math.log,
    'exp': math.exp,
    'pi': math.pi,
    'e': math.e
}

# Obtener valor Adaptado
valAdap = []
for ind in valReal:
    # Insertar el operador de multiplicación donde sea necesario
    expr = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', fnAdSnEsp)

    # Reemplaza 'x' por el valor real en la función
    expr = expr.replace('x', str(ind))  # Sustituimos X por el valor real del individuo

    # Evalúa la expresión de manera segura usando las funciones matemáticas
    resultado = eval(expr, {"__builtins__": None}, math_functions)
    valAdap.append(round(resultado, 3))

# Imprime los valores de adaptación
print('\n' + '>>>>>Los valores adaptados son:', valAdap)

# Método de ruleta (ordenar de mayor a menor)
valAdap.sort(reverse= True) #Ordenar la lista de mayor a menor
print('\n' + '>>>>>Ruleta:',valAdap, '\n')
