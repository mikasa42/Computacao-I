#nome :mikaela alves data:30/05/2019
def CadastrarAluno(Turma):
	
	Nome = input('digite seu nome')
	Idade = int(input('digite sua idade'))
	Notas = [0,0,0]
	for i in range (3):
		Notas[i] = int(input('digite sua nota:'))

	mediaAluno = MediaAluno(Notas)
	
	aluno = {'nome':Nome,'idade':Idade,'Notas':Notas,'media':mediaAluno}

	Turma += [aluno]

	return Turma

	ImprimirAluno(Turma)
def MediaAluno(Notas):

	media = (Notas[0] + Notas[1] + Notas[2])/3

	return media

def ImprimirAluno(Turma):

	for i in range(len(Turma)):
		print(Turma[i]['nome'], '\t', end='')
		print(Turma[i] ['idade'] , '\t', end='' )
		print(Turma[i]['Notas'][0], '\t', end='')
		print(Turma[i]['Notas'][1], '\t', end='')
		print(Turma[i]['Notas'][2], '\t', end='')
		print('%5.2f' % Turma[i]['media'], '\t', end='')
		print()
def main():
	opera=1
	el1 = []
	el2 = []
	print("Ola, quais das opcoes vc deseja")
	while(opera>0):
		opera = -1
		print("[1]")
		print("[2]")
		print("[3]")
		print("[4]")
		print("[5]")
		print("se deseja sair aperte enter")
	
		opera = int(input())

		if(opera == 1):
			turma=-1
			turma = int(input('Qual a turma,[1]- el1 ou[2]- el2'))
			if(turma==1):
				el1 = CadastrarAluno(el1)
			elif(turma==2):
				el2 = CadastrarAluno(el2)
		elif(opera==2):
			turma = int(input('Qual a turma,[1]- el1 ou[2]- el2'))
			if(turma==1):
				ImprimirAluno(el1)
	
			elif(turma==2):
				ImprimirAluno(el2)
				
			
		

main()
