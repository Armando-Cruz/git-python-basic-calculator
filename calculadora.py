# Funciones
def mostrarMenu():
	"""
		Función que imprime las operaciones a realizar
	"""
	print('---- Calculadora Básica ----')
	print('1. Sumar')
	print('2. Restar')
	print('3. Multiplicar')

sumar = lambda numero1, numero2: numero1 + numero2
restar = lambda numero1, numero2: numero1 - numero2
multiplicar = lambda numero1, numero2: numero1 * numero2


# Ejecución del programa
mostrarMenu()

opcion = input('Opción: ')
# Si no elige opción válida
while (opcion != '1') and (opcion != '2') and (opcion != '3'): 
	opcion = input('Opción: ')
	
numero1 = float(input('Número 1: '))
numero2 = float(input('Número 2: '))

if opcion == '1':
	print(f'{numero1} + {numero2} = {sumar(numero1, numero2)}')
elif opcion == '2':
	print(f'{numero1} - {numero2} = {restar(numero1, numero2)}')
else:
	print(f'{numero1} * {numero2} = {multiplicar(numero1, numero2)}')