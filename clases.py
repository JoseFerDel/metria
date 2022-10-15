import math

class Cuadrado:
	def __init__ (self, lado, unidad):
		self.lado = lado
		self.unidad = unidad

	def area(self):
		areavar = self.lado * self.lado
		print(f'\nCuadrado de {self.lado} {self.unidad} de LADO.')
		print(f'\nEl area del CUADRADO es de {areavar} {self.unidad} cuadrados.')

class Rectangulo:
	def __init__ (self, base, altura, unidad):
		self.base = base
		self.altura = altura
		self.unidad = unidad

	def area(self):
		areavar = (self.base * self.altura)
		print(f'\nRECTÁNGULO de {self.base} {self.unidad} de BASE y {self.altura} {self.unidad} de ALTURA.')
		print(f'\nEl area del RECTÁNGULO es de {areavar} {self.unidad} cuadrados.')

class Triangulo:
	def __init__ (self, base, altura, unidad):
		self.base = base
		self.altura = altura
		self.unidad = unidad

	def area(self):
		areavar = (self.base * self.altura) / 2
		print(f'\nTRIÁNGULO de BASE {self.base} {self.unidad} y ALTURA {self.altura} {self.unidad}.')
		print(f'\nEl area del TRIÁNGULO es de {areavar} {self.unidad} cuadrados.')

class Rombo:
	def __init__(self, dmayor, dmenor, unidad):
		self.dmayor = dmayor
		self.dmenor = dmenor
		self.unidad = unidad
		
	def area(self):
		areavar = (self.dmayor * self.dmenor) / 2
		print(f'ROMBO con DIAGONAL MAYOR de {self.dmayor} {self.unidad} y DIAGONAL MENOR de {self.dmenor} {self.unidad}.')
		print('Formula --> A = DIAGONAL MAYOR x DIAGONAL MENOR / 2')
		print(f'El area del ROMBO es de {areavar} {self.unidad} cuadrados.')

class Romboide:
	def __init__(self, base, altura, unidad):
		self.base = base
		self.altura = altura
		self.unidad = unidad

	def area(self):
		areavar = (self.base * self.altura)
		print(f'\nROMBOIDE de {self.base} {self.unidad} de BASE y {self.altura} {self.unidad} de ALTURA.')
		print(f'\nEl area del romboide es de {areavar} {self.unidad} cuadrados.')

class Trapecio:
	def __init__(self, bmayor, bmenor, altura, unidad):
		self.bmayor = bmayor
		self.bmenor = bmenor
		self.altura = altura
		self.unidad = unidad

	def area(self):
		areavar = ((self.bmayor + self.bmenor) * self.altura) / 2
		print(f'\nTRAPECIO de {self.bmayor} {self.unidad} de BASE MAYOR, {self.bmenor} {self.unidad} de BASE MENOR y {self.altura} {self.unidad} de ALTURA.')
		print('Formula --> A = ((BASE MAYOR + BASE MENOR) x ALTURA) / 2')
		print(f'El area del TRAPECIO es de {areavar} {self.unidad} cuadrados.')

class Circulo:
	def __init__(self, radio, unidad):
		self.radio = radio
		self.unidad = unidad

	def area(self):
		areavar = (math.pi * (self.radio ** 2))
		print(f'\nCIRCULO de {self.radio} {self.unidad} de RADIO.')
		print('Formula --> A = pi x RADIO al cuadrado')
		print(f'El area del CIRCULO es de {areavar} {self.unidad} cuadrados.')
