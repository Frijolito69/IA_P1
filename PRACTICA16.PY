#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ coding: utf-8 _*_
autos=['VOLKSWAGEN', 'AUDI', 'PEUGEOT', 'MERCEDEZ', 'NISSAN', 'TOYOTA', 'FERRARI', 'BMW', 'SUBARU'] #Declaramos una lista de marcas de carro
autos.sort()#usamos sort para acomodar en orden alfabetico
print(autos)#imprimimos para ver el resultado
autosr=['VOLKSWAGEN', 'AUDI', 'PEUGEOT', 'MERCEDEZ', 'NISSAN', 'SUBARU'] #Declaramos una lista de marcas de carro
print(sorted(autosr))#usamos sorted para hacer el ajuste en orden alfabetico pero solo temporalmente durante esta linea
autosr.sort(reverse=True)#aplicamos sort reverse para mostrar el efecto de reverse y la temporalidad de sorted
print(autosr)#imprimimos reverse para ver el resultado
