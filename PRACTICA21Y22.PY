edad = int(input('¿Cuál es tu edad?\n'))
if edad <= 0:
	print('Nadie puede tener esa edad.')
elif edad >= 1 and edad <= 17:
	print('Eres menor de edad.')
elif edad >= 18 and edad <= 45:
	print('Eres un adulto.')
elif edad >= 46 and edad <= 99:
	print('Eres un adulto mayor.')
elif edad >= 100 and edad <= 120:
	print('FELICIDADES, HA VIVIDO MUCHO USTED.')
else:
	print('Edad no válida.')