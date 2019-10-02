#questao 1

def baska(a,b,c,):
    import math
    delta = (b*b)-(4*a*c)
    if(delta>=0):
        valor = 0
        raiz = math.sqrt(delta)
        print(raiz)
        print('primeira raiz',(-b+ raiz)/(2*a))
        print('Segunda raiz', (-b-raiz)/(2*a))
    elif(delta<0):
        valor = 1
    return valor
def nob(a,b):
    valor1=0
    valor2=0
    for i in range(len(a)):
        valor1+=int(a[i])
    for j in range(len(b)):
        valor2+=int(b[j])
    resposta = valor1 + valor2
    return  resposta
def pi():
    soma = 0
    i = 1
    valor = 1

    while(valor > 0.00000005):
        valor =(1/i)-(1/(i+2))
        soma = soma+ abs(valor)
        print('isso é a soma ',soma)
        i+=4
    pi = 4*soma
    return pi
def main():
    a = int(input('Digite a \n'))
    b = int(input('Digite b \n'))
    c = int(input('Digite c\n'))
    resposta = baska(a,b,c)
    if(resposta == 0):
        print('nao tem raizes complexas')
    elif(resposta == 1):
        print("tem raizes complexas")
    print(nob('72','99'))
    print( 'esse e o pi',pi())
main()
