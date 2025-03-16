#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ coding: utf-8 _*_

autos=['VOLKSWAGEN', 'AUDI', 'PEUGEOT', 'MERCEDEZ', 'NISSAN', 'TOYOTA', 'FERRARI', 'BMW', 'SUBARU'] #Declaramos una lista de marcas de carro
guardalista=autos.pop(-2) #Eliminamos BMW con el metodo pop 
del autos[3]   #Eliminamos MERCEDEZ CON EL METODO "del"
autos.remove('NISSAN') #Eliminamos NISSAN con el metodo "remove"

print( autos) #Imprimimos los valores seleccionados de la lista haciendo uso de posiciones negativas
print('La marca eliminada con el metodo pop es:',guardalista) #Imprmimos el valor que se guardo con la funcion pop