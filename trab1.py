# primeiro trabalho de computação I
def multiplicacao(a,b):
    resposta = 0
    if(a == 0):
        resposta = 0
    elif(b == 0):
        resposta = 0
    elif(b == 1):
        resposta = a
    else:
        resposta = a + multiplicacao(a, b - 1)
    return resposta

def divisao(a,b):
    resto = 0
    quoci = 0
    if(a == 0 or b == 0):
        return('Operacao incorreta')
    while(a>=b):
        resto = a-b
        a = resto
        quoci +=1
    print('Resto = ',resto,'Quociente =',quoci)
    return quoci
def mdc(a,b):
    maior = 0
    c = 0
    if(a>b):
        maior = a
        c = b
    else:
        maior = b
        c = a
    resto = 1
    if(a == 0 or b == 0):
        return 'Operacao incorreta'

    while(c<maior):
        if(resto == 0):
            return maior
        resto = maior%c
        maior = c
        c = resto

def fib(n):
    if (n == 1):
        resposta = 0
    elif (n == 2):
        resposta = 1
    else:
        resposta = fib(n - 1) + fib(n - 2)
    return resposta

def primos(n):
    print('Esses sao os numeros primos')
    for cont in range(2, n + 1):
        from time import sleep
        sleep(1)
        resp = 0
        for i in range(2, cont):
            if (cont % i == 0):
                resp += 1
        if (resp == 0):
            print(cont)
def main():
    operador = 0
    while(operador>=0):
        from time import sleep
        sleep(1)
        print('* * * * * * * * * * * * * * * * * * *')
        print('*      MENU                         *')
        print('* Escolha uma das opcoes abaixo     *')
        print('* 1 - Multiplicacao                 *')
        print('* 2 - divisao                       *')
        print('* 3 - Fibbonacci                    *')
        print('* 4 - MDC                           *')
        print('* 5 - Numeros primos                *')
        print('* 6 - Sair                          *')
        print('* * * * * * * * * * * * * * * * * * *\n')
        operador = int(input())
        if(operador == 6):
            operador = -1
        elif(operador == 1):
            print('Digite os numeros que deseja multiplicar')
            a = int(input('Digite o primeiro numero\n'))
            b = int(input('Digite o segundo numero\n'))
            print('Resposta = ', multiplicacao(a,b))
        elif (operador == 2):
            print('Digite os numeros que deseja dividir de forma inteira')
            a = int(input('Digite o primeiro numero\n'))
            b = int(input('Digite o segundo numero\n'))
            print('Resposta =',divisao(a,b))

        elif(operador == 3):
            n = int(input('Digite o numero da sequencia\n'))
            print('Resposta =',fib(n))
        elif (operador == 4):
            print('Digite os numeros que deseja saber o mdc')
            a = int(input('Digite o primeiro numero\n'))
            b = int(input('Digite o segundo numero\n'))
            print('Resposta =', mdc(a,b))

        elif(operador == 5):
            n = int(input('Digite o intervalo\n'))
            primos(n)


main()