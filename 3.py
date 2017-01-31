# -*- coding: utf-8 -*-
print "proyecto 2"

class itachi:
	def naruto(self):
		cuanto = int(raw_input("cuantas personas:"))
		contador = 0
		nombre2 = 0
		numero = 0
		contador3 = 0
		contador4 = 0
		numero2 = 0
		nombre3 = 0
		contador2 = 0
		contador1 = 0
		numero3 = 0
		#menor1 = 9999999999999999999999
		for i in range(cuanto):
			nombre = str(raw_input("nombre de la persona:"))
			edad = int(raw_input("edad de la persona:"))
			if i == 0:
				numero2 = edad
				nombre3 = nombre
			if edad < numero2:
				numero2 = edad
				#nombre3 = nombre
			estatura = int(raw_input("estatura de la persona:"))
			if estatura > numero:
				numero = estatura
				nombre2 = nombre
			peso = int(raw_input("peso de la persona:"))
			sexo = int(raw_input("por favor si es masculino marque 1 si es femenino marque 2:"))
			print "-----------------------------------------------------------------------------"
			while sexo == 0 or sexo > 2:
				sexo = int(raw_input("por favor marque como se le indica arriba:"))
			
			if sexo == 1:
				contador1 = contador1 + 1
				#print contador1
				contador = contador + edad
			
			elif sexo == 2:
				numero3 = numero3 + peso 
				contador2 = contador2 + 1
				contador3 = contador3 + edad
				contador4 = contador4 + peso
				
		lista = [contador, nombre2, numero, contador3, contador4, numero2, nombre3, contador2, contador1, numero3]
		return lista


	def hinata(self, lista):
		contador = lista[0]
		numero = lista[2]
		nombre2 = lista[1]
		contador3 = lista[3]
		contador4 = lista[4]
		numero2 = lista[5]
		nombre3 = lista[6]
		contador2 = lista[7]
		contador1 = lista[8]
		numero3 = lista[9]
		total = contador + contador3
		por = contador2 + contador1
		por1 = por / 100
		if contador2 == 0:
			print "no hay mujeres"
		else:
			subtotal = contador1 + contador2
			total1 = total / subtotal
			total2 = numero3 / contador2
			print "el promedio de la edad de todos:", total1
			print "el peso promedio de las mujeres son:", total2
			
			
		lista = [numero, nombre2, numero2, nombre3, contador1, por1]
		return lista

sasuke = itachi()
lista = sasuke.naruto()
vector = sasuke.hinata(lista)
print "la estatura mas alta es:", vector[0]
print "nombre de la persona mas alta es:", vector[1]
print "edad mas joven:", vector[2]
print "nombre del mas joven:", vector[3]
print "la cantidad de hombres son:", vector[4]
#print "el porcentaje de personas son:", vector[5]


		

