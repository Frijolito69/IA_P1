#Elimina el diccionario teclado1 entero . De teclado2 elimina las claves
#'Categoría' y 'Precio'. Muestra la última clave ('Modelo') que queda en la consola
teclado1 = {#DECLARAMOS UN DICCIONARIO
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

teclado2 = {#DECLARAMOS UN DICCIONARIO
	'Categoría': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99'
}

del teclado1 #ELIMINAMOS EL DICCIONARIO TECLADO 1
del teclado2['Categoría'] #ELIMINAMOS EN EL TECLADO 2 LA CATEGORIA
del teclado2['Precio'] #ELIMINAMOS EN EL DICCIONARIO 2 EL PRECIO
print(teclado2['Modelo']) #IMPRIMIMOS EL MODELO