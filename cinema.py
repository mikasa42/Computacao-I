sala = [[0,0,0],[0,0,0],[0,0,0]]

sala[2][1]
def alterarSala(sala,assento):
	alfabeto = 'abcdefghij'
	letra = assento[0]
	num = int(assento[1:len(assento)-1])
	
	for indice in range(len(alfabeto)):
		if alfabeto[indice] == letra:
			letra = indice
	
	if (sala[letra][num-1] == 1):
		resposta = -1
	else:
		sala[letra][num-1] = 1
		resposta = 0
	return resposta


	


def exibirSala(sala):
	letra = 'abcdefghij'
	for indice in range(len(sala)):
		print('  ' + str(indice + 1), end = '\t')
	print()
	for coluna in range(len(sala)):
		print(letra[coluna], end = ' ')
		for linha in range(len(sala[coluna])):
			print(sala[coluna][linha], end = '\t')
		print()
	return

exibirSala(sala)
alterarSala(sala,"b2\n")
exibirSala(sala)


#def main():
#main():
