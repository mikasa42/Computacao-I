# nome : mikaela data :18/04/2019

n=int(input( "Escreva um numero inteiro"))


for num in range(1,n,1):
	if(num%4==0 and num%3!=0):
		print("PIN")

	else:

		print(num)
