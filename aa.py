for i in range(empleados):
			nombre = str(raw_input("nombre del empleado:"))
			dias = int(raw_input("dias trabajados:"))
			sal = int(raw_input("cuantos salarios gana 1 o 2:"))
			mes = 30
			while mes == 0:
				mes = int(raw_input("cuantos salarios gana 1 o 2:"))
			if mes == 1:
				valor = salario /  mes
			print "el valor de un dia es:", valor
				#producto = 2
			elif mes == 2:
				valor2 = salario2 / mes