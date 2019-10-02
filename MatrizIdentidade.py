def criarMatriz(x):
	matriz = [[0]*x for i in range (x)]
	return matriz

def printarMatriz (matriz):
  for indiceLinha in range (len (matriz)):
    for indiceColuna in range (len (matriz)):
      print (matriz [indiceLinha][indiceColuna], end = '\t')
    print ()


def transformarEmIdentidade (matriz):
  for indiceLinha in range (len (matriz)):
    for indiceColuna in range (len (matriz)):
      if (indiceLinha == indiceColuna):
        matriz [indiceLinha][indiceColuna] = 1
      else:
        matriz [indiceLinha][indiceColuna] = 0
def preencherMatriz(matriz):
  numCentroMatriz =(len(matriz))//2 + (len(matriz))%2
  for cont in range(numCentroMatriz):
    for linha in range(cont, len(matriz) - cont):
      for coluna in range(cont, len(matriz) - cont):
        matriz[linha][coluna] = cont + 1
        







def main ():

  indice = int(input('Digite a ordem da matriz \n'))
  matriz = criarMatriz(indice)

  matriz [2][2] = 2
  printarMatriz (matriz)
  print ()
  print ()
  preencherMatriz (matriz)
  printarMatriz (matriz)

main()
