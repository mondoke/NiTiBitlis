#! python3
# iiii - Facilita burlarse de los boludos: Ficiliti birlirisi di lis bilidis

import pyperclip

entrada = pyperclip.paste()
salida = ''
vocales = ['a', 'e', 'o', 'u']
vocalesTilde = ['á', 'é', 'ó', 'ú']

#Devuelve la letra a la que quiero convertir, respetando la mayúscula
def convertir(may, letra):
    if may:
        return letra.upper()
    else:
        return letra.lower()

for i in range(len(entrada)):
    char = entrada[i]       #Agarra el caracter
    mayus = char.isupper()  #Ver si es mayúscula
    #Cambiar:
    if entrada[i-1].lower() != 'q' or char.lower() !='u': #Esto es para las QUE pero no los Qatar
        if char.lower() in vocales:
            salida += convertir(mayus, 'i')
        elif char.lower() in vocalesTilde:
            salida += convertir(mayus, 'í')
        else:
            salida += char
    else:
        salida +=char
        
pyperclip.copy(salida)
print('Ni hiy qui birlirsi dil qui piinsi distinti')
