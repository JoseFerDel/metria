import clases

# Diccionario de opciones de menú:
def menu():
	opciones = {
		1 : 'CUADRADO',
		2 : 'RECTÁNGULO',
		3 : 'TRIÁNGULO',
		4 : 'ROMBO',
		5 : 'ROMBOIDE',
		6 : 'TRAPECIO',
		7 : 'CIRCULO'
		}

# Debido a las 3 minillas simples puedo poner todas las líneas en un solo print y estas 
# se alinearán tal como las ponga, en este caso pegadas al princio de línea. 
# Esto no parece afectar a las reglas de indentación.   
	print(f'''*************************
1 -- {opciones[1]}
2 -- {opciones[2]}
3 -- {opciones[3]}
4 -- {opciones[4]}
5 -- {opciones[5]}
6 -- {opciones[6]}
7 -- {opciones[7]}
*************************\n''')

	select = input('Selecciona figura geométrica (1-7): ')
	
	# Comprueba que se ha seleccionado un número entre 1 y 7, si es así pregunta la unidad de medidad, si no, repete pregunta.
	if (int(select) > 0) or (int(select) < 8):
		# Muestra la forma escogida tomando como clave del diciconario "opciones" la respuesta del usuario guardada en "select".
		print(f'La forma escogida es {opciones[int(select)]}.\n')
		unidad = input('Selecciona unidad de medida: ')
	else:
		print('Opción no admitida.')
		print('Selecciona un número del 1 al 7 para seleccionar una figura')
		menu()
		

	if int(select) == 1: # CUADRADO
		print('Formula area ---> A = LADO x LADO')
		lado = input('Introduce la medida del LADO del CUADRADO: ')
		forma = clases.Cuadrado(int(lado), unidad)
		forma.area()

	elif int(select) == 2: # RECTÁNGULO
		print('Formula area ---> A = base x altura')
		base = input('Introduce la medida de la BASE del RECTÁNGULO: ')
		altura = input('Introduce la medida de la ALTURA del RECTÁNGULO: ')
		forma = clases.Rectangulo(int(base), int(altura), unidad)
		forma.area()

	elif int(select) == 3: # TRIÁNGULO
		print('Formula area --> A = (BASE x ALTURA) / 2')
		base = input('\nIntroduce la medida de la BASE del TRIÁNGULO: ')
		altura = input('Introduce la medida de la ALTURA del TRIÁNGULO: ')
		forma = clases.Triangulo(int(base), int(altura), unidad)
		forma.area()

	elif int(select) == 4: # ROMBO
		print('Formula area --> A = (diagonal mayor x diagonal menor) / 2')
		dmayor = input('Introduce la medida de la DIAGONAL MAYOR: ')
		dmenor = input('Introduce la medida de la DIAGONAL MENOR: ')
		forma = clases.Rombo(int(dmayor), int(dmenor), unidad)
		forma.area()

	elif int(select) == 5: # ROMBOIDE
		print('Formula area ---> A = BASE x ALTURA')
		base = input('Introduce la medida de la BASE del ROMBOIDE: ')
		altura = input('Introduce la medida de la ALTURA del ROMBOIDE: ')
		forma = clases.Romboide(int(base), int(altura), unidad)
		forma.area()

	elif int(select) == 6: # TRAPECIO
		print('Formula area ---> A = ((BASE MAYOR + BASE MENOR) x ALTURA) / 2')
		bmayor = input('Introduce la medida de la BASE MAYOR del TRAPECIO: ')
		bmenor = input('Introduce la medida de la BASE MENOR del TRAPECIO: ')
		altura = input('Introduce la medida de la ALTURA del TRAPECIO: ')
		forma = clases.Trapecio(int(bmayor), int(bmenor), int(altura), unidad)
		forma.area()

	elif int(select) == 7: # CIRCULO
		print('Formula area ---> A = pi x RADIO al cuadrado')
		radio = input('Introduce la medida del RADIO del CIRCULO: ')
		forma = clases.Circulo(int(radio), unidad)
		forma.area()



