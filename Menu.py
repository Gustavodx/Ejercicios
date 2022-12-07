while True:
		print("") 
		print("Menu de recomendaciones")
		print("   1. Literatura")
		print("   2. Cine")
		print("   3. Musica")
		print("   4. Videojuegos")
		print("   5. Salir")

		print("Elija una opcion entre los numeros indicados: ")
		op = int(input())
	
		if op==1:
			print("Lecturas recomendables:")
			print(" + Esperandolo a Tito y otros cuentos de fúbol (Eduardo Sacheri)")
			print(" + El juego de Ender (Orson Scott Card)")
			print(" + El sueño de los heroes (Adolfo Bioy Casares)")
		elif op==2:
			print("Peículas recomendables:")
			print(" + Matrix (1999)")
			print(" + El último samuray (2003)")
			print(" + Cars (2006)")
		elif op==3:
			print("Discos recomendables:")
			print(" + Despedazado por mil partes (La Renga, 1996)")
			print(" + Bufalo (La Mississippi, 2008)")
			print(" + Gaia (Mago de Oz, 2003)")
		elif op==4:
			print("Videojuegos clasicos recomendables")
			print(" + Dia del tentaculo (LucasArts, 1993)")
			print(" + Terminal Velocity (Terminal Reality/3D Realms, 1995)")
			print(" + Death Rally (Remedy/Apogee, 1996)")
		elif op==5:
			print("Gracias, vuelva pronto")
		else:
			print("Opcion no valida")
		print("Presione enter para continuar")
		input()
		if op==5: break