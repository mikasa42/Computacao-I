#aula sobre lista
def criarlista(n):
   lista = []
   for i in range (n):
      lista.append(0)
   return  lista
def imprimelista(lista):
   for i in range(len(lista)):
      print(lista[i], end = ' ')
   print()
def preencherlista(lista):
   for i in range(len(lista)):
      lista[i] = input('Digite o valor\n')
   return lista
def ordenarlista(lista):
    for indice in range(len(lista)-1):
        for i in range (indice+1,len(lista)):
            if(lista[indice]>lista[i]):
               aux=lista[indice]
               lista[indice]= lista[i]
               lista[i]= aux
    return lista
def inverterlista(lista):
   listaAux = []
   for i in range(len(lista) - 1, -1,-1):
      listaAux += [lista[i]]
   return listaAux
def procurarAluno(lista,aluno):
    
    for i in range(len(lista)):
        if(aluno == lista[i]):
            nome = lista[i]
        else:
            nome = ''
    return nome
def primos(n):
     print('Esses sao os numeros primos')
     for cont in range (2,n+1):
        resp = 0
        for i in range(2,cont):
           if(cont%i == 0):
              resp+=1
        if(resp == 0):
           print(cont)
def main(): 
   n = 0
   while(n != 7):
      print('* * * * * * * * * * * * * * * * * * * * *')
      print('* Menu                                  *')
      print('* 1- mostrar uma lista com n elementos  *')
      print('* 2- preencher a lista                  *')
      print('* 3- ordenar uma lista                  *')
      print('* 4- buscar um aluno pelo nome          *')
      print('* 5- inverter a lista                   *')
      print('* 6- numeros primos                     *')
      print('* 7- sair                               *')
      print('* * * * * * * * * * * * * * * * * * * * * ')
      n = int(input())
      if(n == 1):
         n = int(input('Digite o valor de elementos\n'))
         lista = criarlista(n)
         imprimelista(lista)
      elif(n == 2):
         n = int(input('Digite o valor de elementos\n'))
         lista = criarlista(n)
         listaNova = preencherlista(lista)
         imprimelista(listaNova)
      elif(n == 3):
         n = int(input('Digite o valor de elementos\n'))
         lista = criarlista(n)
         listaNova = preencherlista(lista)
         imprimelista(listaNova)
         listaOrdenada = ordenarlista(listaNova)
         imprimelista(listaOrdenada)
      elif(n == 4):
         n = int(input('Digite o numero de alunos\n'))
         if(n !=0 ):
            aluno = input('Digite o nome do aluno desejado\n')
            lista = criarlista(n)
            listaNova = preencherlista(lista)
            nome = procurarAluno(listaNova,aluno)
            if(nome == ''):
               print('O aluno não existe')
            else: 
               print('O nome no aluno e:', nome)
         else:
            print('Operacao incorreta')
      elif(n == 5):
         n = int(input('Digite o valor de elementos\n'))   
         lista = criarlista(n)
         listaNova = preencherlista(lista)
         listanew = inverterlista(listaNova)
         imprimelista(listanew)
      elif(n == 6):
         n = int(input('Digite o intervalo\n'))
         primos(n)         

         
main()
