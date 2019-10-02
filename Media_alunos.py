#03/09
#mikaela 
#programa sobre a media dos alunos

p1 = int(input('Digite a nota da p1\n'))

p2 = int(input('Digite a nota da p2\n'))

p3 = int(input('Digite a nota da p3\n'))

aulas = int(input('Digite o num de aulas\n'))
faltas = int(input('Digite o numero de faltas\n'))

media = (p1 +p2 +p3)/3
porc = (faltas *100)/aulas

if(media>=7):
	print('Aprovado')
elif(media>=3):
	if(porc<75):
		print('Prova final')
	else:
		print('Reprovado por falta')
elif(media<3):
	if(porc<75):
		print('Reprovado por media')
	else:
		print('Reprovado por media e por falta')
