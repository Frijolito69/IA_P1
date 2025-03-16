def colores(*args):#DEFINIMOS UNA FUNCION DE COLORES CON ARGUMENTOS
	print('El color', args[1], 'es mi favorito.', 'El color', args[0], 'tambien.')

def suma(*args):#DEFINIMOS UNA FUNCION PARA UNA SUMA CON ARGUMENTOS
	resultado = args[0] + args[1] + args[2] + args[3] + args[4]#REALIZAMOS LA SUMA CON EL ARGUMENTO
	print('El resultado de sumar estos cinco números es:', resultado)

colores('rojo', 'azul') #LLAMAMOS A LA FUNCION COLORES CON LOS ARGUMENTOS DESEADOS
suma(5, 7, 45, 57, 3, 8)#LLAMAMOS A LA FUNCION SUMA CON LOS ARGUMENTOS DESEADOS