
n = int(input('Digite o intervalo \n'))

for cont in range(1,n+1):
    resp = 0
    for i in range(2,cont):
        if(cont%i==0):
            resp+=1
    if(resp == 0 ):
        print(cont, "Este numero é primo")
    else:
        print(cont,'Este numero não é primo')
