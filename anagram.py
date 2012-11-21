class Anagrama:
	
	def __init__(self, s1, s2):
		"""
		Autor:   NicolasM
		Fecha:   2012/10/14
		Detalle: Esta clase recibe 2 cadenas y devulve true si estas cadenas 
		son un anagrama
		"""
		self.s1 = s1
		self.s2 = s2
	
	def isAnagram(self):	
		"""
	        Autor:   NicolasM
	        Fecha:   2012/10/14
	        Detalle: compara una cadena y retorna True si es un anagrama
	
	        Parametros:
	         - No aplica.
	        Retorno:
	         - Boolean
    		"""
		str1_list = list(self.s1)
		str1_list.sort()
		str2_list = list(self.s2)
		str2_list.sort()

		return (str1_list == str2_list)
	
if __name__ == '__main__':

	cadena1 = raw_input("Ingrese la primer palabra: ")
	cadena2 = raw_input("Ingrese la segunda palabra: ")

	anagrama = Anagrama(cadena1,cadena2)
	if anagrama.isAnagram():
		print "Es un anagrama"
	else:
		print "No es un anagrama"	
	input("Presione cualquier tecla para salir")	
