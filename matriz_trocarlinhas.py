def criarMatriz(tamanho):
	matriz = []
	for cont in range( tamanho):
		matriz += [[0] * tamanho]
	matriz[2][1] = 3
	matriz[1][3] = 2
	print(matriz)
	return matriz
def printarMatriz(matriz):
	for linha in range(len(matriz)):
		for coluna in range(len(matriz)):
			print(matriz[linha][coluna], end = '\t')
			#arquivo.write(str(matriz[linha][coluna]) + ' ')
	#	arquivo.write('\n')  
		print()
def trocarLinhas(matriz,x,y):
	aux = matriz[y] 
	matriz[y] = matriz[x]
	matriz[x] = aux
	return matriz
		
def main():
	matriz = criarMatriz(4)
	printarMatriz(matriz)
	print()
	matriz = trocarLinhas(matriz,2,1)
	printarMatriz(matriz)

	return 0
main()
