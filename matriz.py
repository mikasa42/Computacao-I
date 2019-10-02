
#nome: mikaela alves quinta 10h
def identidade (matriz):
 
	
	for i in range (len(matriz)):
		for j in range (len(matriz)):
			if (i == j):
				matriz [i][j] = 1
			else:
				matriz[i][j] = 0
	return matriz

def recebeMatriz(n):
	
	matriz = criaMatriz(n)
	
	for i in range (n):
		for j in range (n):
			matriz [i][j] = int(input())
	return matriz



def criaMatriz (n):

	matriz = [0]*n
	
	for i in range (n):
		matriz[i] =[0]*n
	return matriz 

def exibeMatriz(matriz):
	for i in range (len(matriz)):
		for j in range (len(matriz)):
			print (matriz[i][j], end = ' ')

		print( )
def main():
	print("Qual operação deseja fazer ? ")
	print("[1]- zerar sua matriz ")
	print("[2]-imprimir uma matriz quadrada  ")
	print("[3]-fazer uma matriz identidade  ")
	print("[4]- trocar duas linhas de uma matriz posicao ")
	print("[5]- i")
	opera = int(input())
	if (opera == 1):
		x = int(input("digite o numero da ordem  da matriz"))
		mat = criaMatriz(x)
		exibeMatriz(mat)
	elif (opera == 3):
		
		x = int(input("digite o numero da ordem  da matriz"))
		m = identidade(recebeMatriz(x))
		exibeMatriz(m)
		

main()

