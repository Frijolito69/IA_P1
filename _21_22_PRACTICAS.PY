edad = int(input('¿Cuál es tu edad?\n')) #USAMOS INT(INPUT) PARA SOLICITAR UNA ENTRADA DE DATO AL USUARIO
if edad <= 0: #SI EL NUMERO ES MENOR O IGUAL A 0 SE CUMPLE EL MENSAJE SIGUIENTE
	print('Nadie puede tener esa edad.')
elif edad >= 1 and edad <= 17: #SI EL NUMERO ES MAYOR O IGUAL 1 Y MENOR O IGUAL A 17 SE MUESTRA EL MENSAJE SIGUIENTE
	print('Eres menor de edad.')
elif edad >= 18 and edad <= 45: #SI EL NUMERO ES MAYOR O IGUAL 18 Y MENOR O IGUAL A 45 SE MUESTRA EL MENSAJE SIGUIENTE
	print('Eres un adulto.')
elif edad >= 46 and edad <= 99: #SI EL NUMERO ES MAYOR O IGUAL 46 Y MENOR O IGUAL A 99 SE MUESTRA EL MENSAJE SIGUIENTE
	print('Eres un adulto mayor.')
elif edad >= 100 and edad <= 120:
	print('FELICIDADES, HA VIVIDO MUCHO USTED.')#SI EL NUMERO ES MAYOR O IGUAL 100 Y MENOR O IGUAL A 120 SE MUESTRA EL MENSAJE SIGUIENTE
else:#SI NO SE CUMPLE NINGUNA DE LAS CONDICIONES ANTERIORES SE VA DIRECTO AL MENSAJE SIGUIENTE
	print('Edad no válida.')