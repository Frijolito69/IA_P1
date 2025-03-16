LISTA=['VOLKSWAGEN', 'AUDI', 'PEUGEOT', 'MERCEDEZ', 'NISSAN'] #Declaramos una LISTA de marcas de carro
marca=input('Elije una marca para buscar en la lista')#LEEMOS UNA ENTRADA DE DATO QUE DE EL USUARIO
if marca in LISTA:#SI ESTA EN LA LISTA ENTONCES MOSTRAMOS EL SIGUIENTE MENSAJE
    print('La marca esta en la lista')
else:#SI NO ESTA EN LA LISTA MOSTRAMOS EL SIGUIENTE MENSAJE
    print('La marca no esta en la lista')