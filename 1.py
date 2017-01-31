# -*- coding: utf-8 -*-
print "proyecto numero 1"

class p:
	def z(self):
		empleados = int(raw_input("cuantos empleados:"))
		global salario
		salario = 535600
		#salario2 = 1071200
		global transporte
		transporte = 63600
		global mes
		mes = 30
		sal = 1
		neto2 = 0
		neto3 = 0
		contador = 0
		numero = 0
		numero2 = 0
		lista = [empleados, salario, neto2, neto3, contador, numero, numero2]
		return lista
		

	def b(self, empleados, neto2, neto3, contador, numero, numero2):
		valor2 = 0
		par2 = 0
		aren2 = 0
		par2 = 0
		trabajo2 = 0
		nombre4 = 0
		menor = 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
		for i in range(empleados):
			nombre = str(raw_input("nombre del empleado:"))
			dias = int(raw_input("dias trabajados:"))
			sal = int(raw_input("cuantos salarios se gana:"))

			while  sal == 0:
				print "por favor marque los salarios indicados"
				sal = int(raw_input("cuantos salarios se gana:"))

			valor = salario * sal
			valor2 = valor / mes
			print "el valor de un dia es:", valor2
			trabajo = valor2 * dias
			print "el valor de los dias trabajados son:", trabajo
			trans = float(transporte) / float(mes)
			trans2 = float(trans) * float(dias)
			print "el auxilio de transporte de los dias trabajados:",  trans2
			seguro = salario * 0.4
			seguro2 = seguro / dias
			seguro4 = seguro2 * dias
			print "el decuento del seguro social es:", seguro4
			neto = trabajo + trans2 + seguro4
			print "el sueldo neto del empleado es:", neto
			print "-----------------------------------------"
			par2 = par2 + trans2
			trabajo2 = trabajo2 + neto
			aren2 = aren2 + seguro4 
			#print trabajo2
			if neto > numero:
				numero = neto
				nombre2 = nombre 
			if neto < menor:
				menor = neto
				nombre4 = nombre
		lista = [trabajo2, par2, aren2, numero, nombre2, menor, nombre4]
		return lista
itachi = p()
numero = itachi.z()
lista = itachi.b(numero[0], numero[1], numero[2], numero[3], numero[4], numero[5])

print "la suma de los suledos netos son:", lista[0]
#print "la cantidadde sueldos pagados son:", lista[2]
print "total de auxilio de transporte:", lista[1]
print "el total de descuento de seguro sicial:", lista[2] 
print "el salario mas alto es:", lista[3]
print "el nombre del empleado que gana mas es:", lista[4]
print "el salario mas bajo es:", lista[5]
print "el nombre del empleado que gana menos de todos es:", lista[6]
		
				




			
	

		
				
			
			
			







 
		
				
				
		
		
		
		
		
				
				






		
