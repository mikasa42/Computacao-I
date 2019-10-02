#exercicio sebre o fatorial

def fat(n):
	resp = 1
	for cont in range(1,n+1):
		resp *= cont
	return resp

def fatrec(n):
	if(n==1):
		resposta = 1
	else:
		resposta = n *fatrec(n-1)
	return  resposta
		
def combinacao(m,n):
	resposta = fatrec(m)/(fatrec(n)*(fatrec(m-n)))
	return resposta
def contador(palavra,letra):
	conta = 0
	for cont in range(1,len(palavra)):
		if(letra == palavra[cont]):
			conta +=1
	return conta

def fib(n):
	if(n==1):
		resposta = 0
	elif(n==2):
		resposta = 1
	else:
		resposta = fib(n-1)+fib(n-2)
	return resposta
def main():
	opera = 1
	while(opera>0):
		print('Menu')
		print('1-fatorial')
		print('2-combinacao')
		print('3-contagem de caracteres ')
		print('4-fibonacci')
		print('5-sair')
		opera = int(input())
		if(opera == 1):
			n = int(input('Digite o numero desejado n \n'))
			print(fatrec(n))
			
		elif(opera == 2):
			m = int(input('Digite o numero desejado n \n'))
			n = int(input('Digite o numero desejado m \n'))
			print(combinacao(m,n))

		elif(opera == 3):
			palavra = input('digite o palavra\n')
			letra = input('Digite a letra desejada\n')
			print(contador(palavra,letra))
		elif(opera == 4):
			num = int(input('Digite o numero na sequecia fibonacci'))
			print(fib(num))
		elif(opera == 5 ):
			print('Volte sempre')
			opera =-1
main()


