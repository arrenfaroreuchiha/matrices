# -*- coding: utf-8 -*-
print "proyecto 3"
print "------------"

class sasuke:
	def entra(self):
		global i, a, b, c
		i = 1
		a = 1
		b = 2
		c = 3
		print "por la compra de mas de 5 productos se le hace un descuento del 5%"
		print "harina pan = $2500-1"
		print "aceite = $3000-2"
		print "bolsa de leche = $2300-3"
		cantidad = int(raw_input("cuantos productos:"))
		return cantidad

	def circula(self, cantidad):
		#global condicional, condicional1, condicional2, condicional3
		condicional = 0
		condicional1 = 0
		condicional2 = 0
		condicional3 = 0
		producto = 4
		contador = 0
		contador1 = 0
		contador2 = 0
		por = 0
		por1 = 0
		por2 = 0
		for i in range(cantidad):
			while producto > 3:
				print "por favor marque el producto con su respectivo numero(1,2,3)"
				producto = int(raw_input("cual producto:"))
			if producto == 1:
				cantidad1 = int(raw_input("cantidad:"))
				contador = contador + cantidad1
				#global condicional
				condicional = 2500 * cantidad1
				por = por + condicional
				producto = 4
				print "-----------------------------------------------"
				
			elif producto == 2:
				cantidad2 = int(raw_input("cantidad:"))
				contador1 = contador1 + cantidad2
				condicional1 = 3000 * cantidad2
				por1 = por1 + condicional1
				producto = 4
				print "-------------------------------------------------"
				
			elif producto == 3:
				cantidad3 = int(raw_input("cantidad"))
				contador2 = contador2 + cantidad3
				condicional2 = 2300 * cantidad3
				por2 = por2 + condicional2
				producto = 4
				print "---------------------------------------------------"
				
				
		lista = [condicional, condicional1, condicional2, contador, contador1, contador2, por, por1, por2]
		return lista
			

	def sale(self, lista):
		condicional = lista[0]
		condicional1 = lista[1]
		condicional2 = lista[2]
		contador = lista[3]
		contador1 = lista[4]
		contador2 = lista[5]
		por = lista[6]
		por1 = lista[7]
		por2 = lista[8]
		total1 = contador + contador1 + contador2
		subtotal = condicional + condicional1 + condicional2
		iva = subtotal * 16 / 100
		total = subtotal + iva
		print "la cantidad de botellas de litro de aceites fueron:", contador1
		print "la cantidad de bolsas de leche que se vendieron fueron:", contador2
		print "la cantidad de bolsas de harina pan que se vendieron fueron:", contador
		print "la cantidad de productos vendidos son:", total1
		print "el subtotal es:", subtotal
		print "el iva es: %d" % iva
		
		if total1 > 5:
			subtotal1 = por * 5 / 100
			subtotal2 = por1 * 5 / 100
			#print "oo", por1
			subtotal3 = por2 * 5 / 100
			total2 = subtotal1 + subtotal2 + subtotal3
			total3 = total - total2
			print "-----------------------------------------------------------"
			print "el descuento por el producto numero 1 es:", subtotal1
			print "el descuento por el producto numero 2 es:", subtotal2
			print "el descuento por el producto numero 3 es:", subtotal3
			print "el descuento total que se le hizo a los productos fue:", total2
			print "el total es:", total3
		else:
			print "no hay descuento del 5%"
			print "el total es: %d" % total
		return
		
			
itachi = sasuke()
obito = itachi.entra()
sakura = itachi.circula(obito)
hinata = itachi.sale(sakura)					

		

	