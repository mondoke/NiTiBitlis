#! python3
# iiii - Facilita burlarse de los boludos: Ficiliti birlirisi di lis bilidis

import pyperclip

entrada = pyperclip.paste()
salida = ''
vocales = ['a', 'e', 'o', 'u']
def convertir(may):
    if may:
        return 'I'
    else:
        return 'i'

for i in range(len(entrada)):
    char = entrada[i]       #Agarra el caracter
    mayus = char.isupper()  #Ver si es mayúscula
    #Cambiar:
    if entrada[i-1].lower() != 'q' or char.lower() !='u':
        if char.lower() in vocales:
            salida += convertir(mayus)
        else:
            salida += char
    else:
        salida +=char
        
pyperclip.copy(salida)
print('Ni hiy qui birlirsi dil qui piinsi distinti')
