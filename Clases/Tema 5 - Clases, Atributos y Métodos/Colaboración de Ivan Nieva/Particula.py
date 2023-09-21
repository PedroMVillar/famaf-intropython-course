#Defino la clase Particula 

class Particula:
	#Este es el constructor.
	#Con __ estoy encapsulado los atributos, 
	#solo son visibles desde adentro de la clase.
	def __init__(self):   
		self.__masa    = 1   
		self.__carga   = -1
		self.__spin    = 0.5
		self.__energia = 500

	#Defino varios métodos para la clase Particula.
	
	def cambiaEnergia(self, delta):
		self.__energia = self.__energia + delta 	

	def cambiaSpin(self):
		self.__spin = -self.__spin

	def mostrarParticula(self):
		print("masa: ", self.__masa)
		print("carga: ", self.__carga)
		print("spin: ", self.__spin)
		print("energia: ", self.__energia)
		

#Instancio dos objetos del tipo particula.
p1 = Particula()
p2 = Particula()

#Muestro a p1
p1.mostrarParticula()

'''Notemos que las modificaciones que puedo hacer solo
se pueden realizar con los metodos definidos en la clase.
Con esto notemos que la masa no puede modificarse, todas las particulas creadas
van a tener masa = 1. Sin embargo si puedo cambiar el spin porque tengo un
metodo para ello.
'''
#Cambio el spin de p2, su energia y la muestro, notemos que toda particula nueva tiene spin
#0.5 y energia 500 por defecto. 
print("")
print("Veamos la particula 2")
p2.cambiaSpin()
p2.cambiaEnergia(100)
p2.mostrarParticula()

#Pero, si quiero cambiar la masa no puedo hacerlo pues no tengo un método para ello
#y ademas está encapsulada por lo que no puedo verla desde afuera de la clase.
#notemos eso con lo siguiente:
print("")
print("Intento cambiar el spin y la masa")
p2.masa = 1000
p2.spin = 1000
p2.__spin=1000
p2.mostrarParticula()

#Vemos que no funciona.
#Tampoco si hiciera esto:
print("")
print("Intento cambiar nuevmente el spin y la masa")
p2.__masa = 1000
p2.__spin=1000
p2.mostrarParticula()

#para poder cambiar el valor de la masa o cualquier
#otro atributo necesito tener metodos para ello.
#defino la version 2 de Particula.

class Particula2:
	def __init__(self):   
		self.__masa    = 0     
		self.__carga   = 0  
		self.__spin    = 0  
		self.__energia = 0
	

	#Defino varios métodos para setear los atributos.
	def setMasa(self,masa):
		self.__masa = masa

	def setCarga(self,carga):
		self.__carga = carga
	
	def setSpin(self,spin):
		if((spin == 0.5 or spin == -0.5)):
			self.__spin = spin
		else:
			print("Valor invalido de spin")

	def setEnergia(self,energia):
		self.__energia = energia
			
						
	#Otros métodos utiles	
	def cambiaSpin(self):
		self.__spin = -self.__spin

	def mostrarParticula2(self):
		print("masa: ", self.__masa)
		print("carga: ", self.__carga)
		print("spin: ", self.__spin)
		print("energia: ", self.__energia)

	

#instancio
print("")
print("Nueva version")
p3 = Particula2()
p3.mostrarParticula2()
p3.setMasa(1)
p3.setSpin(0.57)
p3.mostrarParticula2()
