###
# 03 - Quantifiers
# Los cuantificadores se utilizan para especificar cuántas ocurrencias de un carácter o grupo de caracteres se deben encontrar en una cadena.
###

import re


# *: Puede aparecer 0 o más veces
texto = 'aaaba'
patron= r'a*'

rta = re.findall(patron, texto)
print(rta)

# +: Una a mas veces

text1 = 'ddd aaa ccc aaa manzana pera  '
patron1 = 'a+'

rta1 = re.findall(patron1, text1)
print(rta1)

# ?: Cero o una vez
text = "aaabacb"
pattern = "a?b"
matches = re.findall(pattern, text)
print(matches)

# Ejercicio: Haz opcional que aparezca un +34 en el siguiente texto
phone = "+34 688999999"

# {n}: Exactamente n veces
text = "aaaaaa         aa   aaaa"
pattern = "a{3}"
matches = re.findall(pattern, text)

print(matches)

# {n, m}: De n a m veces
text = "u uu uuu u"
pattern = r"\w{2,3}"
matches = re.findall
(pattern, text)
print(matches)

# Encuentra las opalabras de mas de 4 a 6 letras

texto2 = 'ala cada arbol perrot gato leon mandarina cocacola'
patron2= r'\b\w{4,6}\b'

rta3 = re.findall(patron2, texto2)
print(rta3)



# Encuentra las opalabras de mas  6 letras

texto2 = 'ala cada arbol perrot gato leon mandarina cocacola'
patron2= r'\b\w{6,}\b'

rta3 = re.findall(patron2, texto2)
print(rta3)