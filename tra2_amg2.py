# Christian de Lima Couto
# 17 / 06 / 2019
# Banco de dados da copa do mundo
#



def criarSelecao(selecao): 

    try:  # Antes de criar a seleção tentaremos abrir ela para ver se ela existe. Se abrir é porque ela já existe e avisará ao usuario

        arquivo = open(selecao + '.txt', 'r')

        selecao = 'Essa seleção já existe'


    except FileNotFoundError: # Caso não abra ela criará a nova seleção


        arquivo = open(selecao + '.txt', 'w')

        print('\n\nSeleção criada')



    return arquivo, selecao

#####################################################


def escreverNaSelecao(arquivo): # O 'arquivo', é a selecão que eu chamei e desejo escrever os jogadores nela

    cont = 1

    nome = 0

    idade = 0

    time = 0

    posicao = 0

    gols = 0


    print('\nSe quiser parar de escrever digite (-1)')

    print('\nregistre os jogadores com os seguintes daos abaixo')

    while((nome != '-1') and (idade != -1) and (time != '-1') and (posicao != '-1') and (gols != -1)):

        print('\n\n\ndados do jogador ' + str(cont) + ': ')

        print()


        nome = input('\nnome do jogador: ')
    
        if (nome != '-1'):    # A partir daqui cada 'if' será para parar a excecução caso o usuario digite '-1' em qualquer etapa

            idade = int(input('\nidade do jogador: '))

            if (idade != -1):

                time = input('\ntime que o jogador atua: ')

                if(time != '-1'):


                    posicao = input('\nposição do jogador (goleiro, zagueiro, lateral, meio-campo ou atacante): ')

                    if (posicao != '-1'):

                        gols = int(input('\nnúmero de gols na copa: '))

                        if (gols != -1):


                            arquivo.write(nome + ';' + str(idade) + ';' + time + ';' + posicao + ';' + str(gols) + '\n')

        
        cont += 1


    return arquivo


################################################


def selecoes(arquivo):   # Está funcão abrirá o arquivo que guarda todas as seleções
                         # Ela será usada toda vez que uma seleção for criada, para adicionar ela no arquivo com todas


    selecoes = open('selecoes.txt', 'a')

    selecoes.write(arquivo + '.txt' + '\n')

    selecoes.close()



###################################################


def adicionarJogador(arquivo):


    NovaSelecao = open(arquivo + '.txt', 'a') # Chamamos o arquivo da seleção escolhida e adicionamos uma string com dados do jogador no final


    return NovaSelecao, arquivo



#####################################################

def converterArquivo(nome):


    arquivo = open(nome + '.txt', 'r')

    lista = arquivo.readlines() # Transformamos o arquivo escolhido numa lista, com cada elemento sendo a string com dados de cada jogador

    arquivo.close()

    return lista

#####################################################


def criarDicionario(lista): # 'Lista' ê a lista chamada na função acima


    NovaLista = []


    for i in range(len(lista)): # Andaremos por cada elemento da lista, que é uma string com dados de cada jogador


        dicionario = {'nome' : '', 'idade' : -1, 'time' : '', 'posição' : '', 'gols' : -1, 'seleção' : ''}


        string = '' # Toda vez que o for entrar em outro elemto da lista a String volta a ser vazia

        nome = ''

        idade = ''

        time = ''

        posicao = ''

        gols = ''

        selecao = ''

        string += lista[i] # Aqui adicionamos uma letra qie é elemento da lista na string


        cont = 0

        for pos in range(len(string)):

            if (string[pos] == ';'): # A partir daqui andaremos por cada letra da string afim de separar em palavras conforme está no dicionario

                cont += 1

         
            if (cont == 0): # O cont irá controlar onde vai ser adicionado as letras da string, seguindo a ordem do dicionario
                
                if (string[pos] != ';'): # Cada 'if' serve para não adicionar o ';' na nova string
                    
                    nome += string[pos]

          
            elif (cont == 1):
                
                if (string[pos] != ';'):
                    
                    idade += string[pos]

        
            elif (cont == 2):
                
                if (string[pos] != ';'):
            
                    time += string[pos]


            elif (cont == 3):
                
                if (string[pos] != ';'):

                    posicao += string[pos]


            elif (cont == 4):

                if (string[pos] != ';'):

                    gols += string[pos]
            
            elif (cont == 5):
                
                if (string[pos] != ';'):
                    
                    if ((string[pos] != '.') and (string[pos] != 't') and (string[pos] != 'x')):
                        
                        selecao += string[pos]


        # Guardaremos as informações no dicionario   
        
        dicionario = {'nome' : nome, 'idade' : int(idade), 'time' : time, 'posição' : posicao, 'gols' : int(gols), 'seleção' : selecao}

        NovaLista += [dicionario] # Será a lista de dicionarios, e juntará todos os jogadores por causa do for.


    return NovaLista


#####################################################

def buscaJogador(nome, lista): # Estamos chamando o nome do jogador e a lista da seleção em que ele se encontra


    cont = 0

    for pos in range(len(lista)):

        if (lista[pos]['nome'] == nome):

            posicao = pos

            cont += 1



    if (cont == 0): # Se náo tiver nenhum jogador com o nome não somará no cont, e permanecerá no zero

        posicao = 'jogador não encontrado'


    return posicao


#####################################################

def apagarJogador(selecao, lista, posicao): # Está funcão entrará com a função anterior
                                            # Suas chamadas são o nome da seleção, a lista da seleção do jogador e sua posição na lista


    if (posicao == 'jogador não encontrado'):

        arquivo = '\njogador não encontrado'

    else:

        lista = lista[0:posicao] + lista[posicao + 1: ] # Estamos excluindo o jogador que queremos, pois sabemos sua posição

    
        arquivo = open(selecao + '.txt', 'w')

        for elem in range(len(lista)):

            arquivo.write(lista[elem])  # Aqui vamos rescrever o arquivo com cada elemento da nossa nova lista, que não inclui este jogador


        arquivo.close()

  
    return arquivo


#####################################################

def trocarGol(selecao, lista, posicao): # Está função entrara com a função 'buscaJogador'
                                        # Ela chama o nome da seleção, a lista da seleção do jogador, bem como sua posição na lista


    if (posicao == 'jogador não encontrado'):

        arquivo = '\njogador não encontrado'

    else:

        gol = input('\nentre com o novo numero de gols: ')

        lista[posicao]['gols'] = gol


        Novalista = []

        for pos in range(len(lista)):

            Novalista += [lista[pos]['nome'] + ';' + str(lista[pos]['idade']) + ';' + lista[pos]['time'] + ';' + lista[pos]['posição'] + ';' + str(lista[pos]['gols']) + '\n']


        arquivo = open(selecao + '.txt', 'w')

        for elem in range(len(Novalista)): # Apagamos o arquivo e vamos reescrever todas as suas linhas, com a modificação feita nos gols


            arquivo.write(Novalista[elem])

        arquivo.close()


    return arquivo


#####################################################


# Nesta etapa vamos usar funções para separar os jogadores pelas suas posições

#Cada jogador vai estar numa lista com o nome da sua posição


def consultarGoleiro(lista):

    goleiro = []

    for elem in range (len(lista)):

        if (lista[elem]['posição'] == 'goleiro'):

            goleiro += [lista[elem]] # Faremos um lista só com os goleiros

    return goleiro


def consultarZagueiro(lista):

    zagueiro = []

    for elem in range (len(lista)):

        if (lista[elem]['posição'] == 'zagueiro'):

            zagueiro += [lista[elem]] # Faremos uma lista só com zagueiros

    return zagueiro


def consultarLateral(lista):

    lateral = []
    
    for elem in range (len(lista)):

        if (lista[elem]['posição'] == 'lateral'):

            lateral += [lista[elem]] # Faremos um lista só com laterais

    return lateral


def consultarMeioCampo(lista):

    meiocampo = []

    for elem in range (len(lista)):

        if (lista[elem]['posição'] == 'meio-campo'):

            meiocampo += [lista[elem]] # Faremos uma lista só com meio-campo

    return meiocampo


def consultarAtacante(lista):

    atacante = []

    for elem in range (len(lista)):

        if (lista[elem]['posição'] == 'atacante'):

            atacante += [lista[elem]] # Faremos uma lista só com atacantes

    return atacante




def juntaTudo(lista1, lista2, lista3, lista4, lista5): # Esta função chamara as outtas 5 em que cada uma ê uma lista de uma posição


    Tudo = []

    for elem in range(len(lista1)):

        Tudo += [lista1[elem]]

    
    for elem in range(len(lista2)):

        Tudo += [lista2[elem]]


    for elem in range(len(lista3)):

        Tudo += [lista3[elem]]


    for elem in range(len(lista4)):
        
        Tudo += [lista4[elem]]


    for elem in range(len(lista5)):

        Tudo += [lista5[elem]] # Juntamos tudo numa lista, todas ordenadas em sequencia pela posição



    return Tudo

#####################################################

    
def ordenarNome(lista): # Colocaremos os nomes em ordem alfabética

    trocou = True

    cont = 1

    while(trocou):

        trocou = False

        for pos in range(len(lista) -cont): # o Cont é para controlar a quantidade de vezes que vamos percorrer a lista para ordenar


            if(lista[pos]['nome'] > lista[pos +1]['nome']): # Invertemos a posição caso o primeiro elemento venha depois do segundo no alfabeto


                trocou = True

                aux = lista[pos]

                lista[pos] = lista[pos +1]

                lista[pos +1] = aux

        cont += 1

    return lista

#####################################################

def consultarIdade(lista): # Vamos criar uma lista limita aos jogadores abaixo da idade escolhida


    listaIdade = []

    limite = int(input('\nescolha a idade máxima: '))

    for elem in range(len(lista)):

        if (lista[elem]['idade'] <  limite):

            listaIdade += [lista[elem]]

    return listaIdade

#####################################################

def ordenarIdade(lista): # Vamos ordenar a lista pela maior idade até a menor

    trocou = True

    cont = 1

    while (trocou):

        trocou = False


        for pos in range(len(lista) -cont): # O cont vai controlar a quantidade de vezes que percorremos a lista, todas para ordenar

            if (lista[pos]['idade'] <  lista[pos +1]['idade']):

                trocou = True

                aux = lista[pos]

                lista[pos] = lista[pos +1]

                lista[pos +1] = aux

        cont += 1
    

    return lista


###########################

def consultarTime(lista): # Vamos criar uma lista limitadas aos jogadores que pertencem ao time escolhido

    
    listaTime = []

    time = input('\nEscolha o time: ')

    for elem in range(len(lista)):

        if (lista[elem]['time'] == time):

            listaTime += [lista[elem]]

    return listaTime


##############################################

def ordenarGols(lista): # Ordenaremos a lista que chamaremos pela quantidade de gols


    trocou = True

    cont = 1
    
    while(trocou):

        
        trocou = False


        for pos in range(len(lista) -cont): # O cont será para controlar a quantidade de vezes que vamos percorrer a lista


            if (lista[pos]['gols'] < lista[pos +1]['gols']):

                trocou = True

                aux = lista[pos]

                lista[pos] = lista[pos +1]

                lista[pos +1] = aux

        cont += 1

    return lista

#####################################

def listaDeTudo(): # Esta função vai servir para transformarmos todos os jogadores de todas as seleções em elemnetos de uma só lista


    lista = []

    Tudo = open('selecoes.txt', 'r') # Abrir o arquivo que contem o nome de todas as seleções

    equipes = Tudo.readlines() # Cada elemento da lista vai ser o nome de um dos arquivos

    Tudo.close()


    for selecoes in equipes: # Percorremos cada elemto da lista, que vai ser o nome da seleção

        cont = 0

        while(selecoes[cont] != '\n'): # Cada nome termina com '\n', assim quando ler o primeiro '\n' terá completado o noke da seleção que quer chamar
            
            cont += 1

        selecao = selecoes[0:cont] # Cortamos o '\n' do nome


        arquivo = open(selecao, 'r') # Abriremos o arquivo que completa o nome

        lista1 = arquivo.readlines() # Transformamos o arquivo aberto em uma lista com cada elemento sendo as informações dos jogadores


        lista3 = criarDicionario(lista1) # Vamos abrir na forma de dicionario, para avaliar a categoria 'seleção'

   
        arquivo2 = open(selecao, 'w') # Nosso objetivo ê reescrever o arquvio, só que cada elemento acrescentado de selecao.txt no final, sendo selecao a sua seleção


        for elem in range(len(lista1)):
            
            if (lista3[elem]['seleção'] == ''): # Se seleção estiver vazio é pq é a primeira vez que vamos reescrever os elementoa dessa seleção acrescentando mo final

                arquivo2.write(lista1[elem][0:-1] + ';' + selecao + '\n')
        
            else:

                arquivo2.write(lista1[elem]) # Se não estiver vazio é pq já reescrevemos, não sendo necessário acreacentar selecao.txt no final pq já está reescrito


        arquivo2.close()


        arquivo3 = open(selecao, 'r')

        lista2 = arquivo3.readlines()


        for elem in range(len(lista2)):

            lista += [lista2[elem]] # Fazermos uma nova lista que irá juntar todos os elementos de cada lista anterior numa só
                                    # Devido ao primeiro 'for' essa operação vai se repetir com todas as seleções, juntando todos os jogadores numa unica lista


    return lista

###########################################################


def printar(lista, verSelecao):

    if(lista == []):
        
        print('\nNão há jogadores em nenhuma seleção')


    else:
        
        numeroJogadores = len(lista)

        tamanhoNome = []

        maiorNome = 0

        for jogador in range(numeroJogadores):

            tamanhoNome += [len(lista[jogador]['nome'])]

        for verNome in (tamanhoNome):

            if (verNome > maiorNome):

                maiorNome = verNome





        tamanhoTime = []
    
        maiorTime = 0

        for jogador in range(numeroJogadores):

            tamanhoTime += [len(lista[jogador]['time'])]

        for verTime in (tamanhoTime):

            if (verTime > maiorTime):

                maiorTime = verTime


        maiorPosicao = len('meio-campo')

    
        # Achamos os maiores nomes para toda vez que for printar ter o mesmo espaço vazio para cada elemento

        print()

        print('NOME', end = ' ' * maiorNome)
        print('IDADE', end = ' ' * 7)
        print('TIME', end = ' ' * maiorTime)
        print('POSIÇÃO', end = ' ' * maiorPosicao)
        print('GOLS', end = ' ' * 7)


        if(verSelecao == 'sim'):

            print('Seleção', end = ' ')

        print()


        for elem in range(len(lista)):
        
            print()


            for cont in range(6):

                if(cont == 0):

                    print(lista[elem]['nome'], end = ' ' * (maiorNome - (len(lista[elem]['nome'])) + 6))
                
                # Como cada elemneto tem um tamanho, diminuiremos o maiorNome pelo tamanho do nome dauele elemento para termos o mesmo espaço
                # Repetiremos o processo para todos os outros abaixo


                if(cont == 1):

                    print(lista[elem]['idade'], end = ' ' * 7)

                if(cont == 2):

                    print(lista[elem]['time'], end = ' ' * (maiorTime - (len(lista[elem]['time'])) + 6))


                if(cont == 3):

                    print(lista[elem]['posição'], end = ' ' * (maiorPosicao - (len(lista[elem]['posição'])) + 9))

                if(cont == 4):
                
                    print(lista[elem]['gols'], end = ' ' * 7)

                if(verSelecao == 'sim') and (cont == 5):
                    
                    print(lista[elem]['seleção'], end = ' ')

            
            print() 


#####################################################



print('\n############## BANCO DE DADOS ##############')



sessao = 0


while(sessao != 'S'): # Só sairá da sessão se o usuario optar por sair


    print('\nentre com os seguintes comandos conforme a operação que deseja: ')


    print('\nse quer criar  sua própria seleção digite (1)')


    print('\nse quer acrescentar um jogador em uma seleção digite (2)')


    print('\nse quer apagar um jogador digite (3)')


    print('\nse quer atualizar o número de gols de um jogador digite (4)')


    print('\nse quer fazer consultas digite (5)')


    print('\nse quiser sair digite (S)')

    print()

    sessao = input('\nescolha o que deseja: ').upper().strip()





    if (sessao == '1'):


        print('\n\n####sessão de criar seleção####\n\n')

        NomeSelecao = input('escolha o nome da seleção: ')

        selecao, nome = criarSelecao(NomeSelecao)

        if (nome == 'Essa seleção já existe'):

            selecao.close()

            print('\nEsta seleção já existe')

        
        else:

            selecao = escreverNaSelecao(selecao)

            selecoes(nome) # Colocaremos a seleção criada no arquivo que contem todas as seleções

            selecao.close()
            


########


    elif (sessao == '2'):

        print('\n\n####Sessão para adicionar jogador####\n\n')


        selecao = input('\nescolha a selecao: ')
       
        try: # Antes de adicionar o jogador tentaremos ver se a seleção que colocamos existe

            open(selecao + '.txt', 'r')
        
            arquivo, nome = adicionarJogador(selecao)

            arquivo = escreverNaSelecao(arquivo)

            arquivo.close()
        
        except FileNotFoundError:

            print('\nestá seleção não existe')



    elif (sessao == '3'):
        
        print('\n\n####Sessão para apagar um jogador da seleção####\n\n')


        NomeSelecao = input('\nescolha a seleção do jogador: ')

 
        try:

            open(NomeSelecao + '.txt', 'r')

            jogador = input('\nescolha o jogador: ')


            posicao = buscaJogador(jogador, criarDicionario(converterArquivo(NomeSelecao)))

        

            if (posicao == 'jogador não encontrado'):

                print('\njogador não encontrado')

            else:

                print('\ntem certeza que quer deletar o jogador?')

                print('\ntecle (S) para sim ou (N) para não:')

                escolha = input().upper().strip()

            
                if (escolha == 'S'):


                    lista = converterArquivo(NomeSelecao)

                    apagarJogador(NomeSelecao, lista, posicao)


        except FileNotFoundError:

            print('\nEstá seleção não existe')




    elif (sessao == '4'):

        print('\n\n####Sessão mudar numero de gols de um jogador####\n\n')



        NomeSelecao = input('\nescolha a seleção do jogador: ')


        try:

            open(NomeSelecao + '.txt', 'r')

            jogador = input('\nescolha o jogador: ')


            posicao = buscaJogador(jogador, criarDicionario(converterArquivo(NomeSelecao)))

      
            if (posicao == 'jogador não encontrado'):

                print('\njogador não encontrado')

            else:

 
                lista = criarDicionario(converterArquivo(NomeSelecao))

                trocarGol(NomeSelecao, lista, posicao)


        except FileNotFoundError:

            print('\nEstá seleção não existe')




#######


    elif (sessao == '5'):


        escolha = 0

        while(escolha != 'R'): # Manteremos a sessão de consultas até o usuario optar por sair dela


            print('\n########### Bem vido a sessão de consultas########')


            print('\n\nEscolha o que deseja consultar: ')
       
            print('\nSe deseja consultar os jogadores numa posição digite (A)')

            print('\nSe deseja consultar os jogadores abaixo de uma idade digite (B)')

            print('\nSe deseja consultar o jogadores que jogam num time que você escolherá digite (C)')

            print('\nSe deseja ver a lista de artilhieros digite (D)')


            print('\nSe deseja retornar para a sessão anterior digite (R)')


            escolha = input('\nDigite o que deseja: ').upper().strip()




            if (escolha == 'A'):

                selecao = input('\n\nescolha a seleção: \n')

                try:

                    open(selecao + '.txt', 'r')

                    lista = criarDicionario(converterArquivo(selecao))
        

                    print()

                    lista1 = ordenarNome(consultarGoleiro(lista))

                    lista2 = ordenarNome(consultarZagueiro(lista))

                    lista3 = ordenarNome(consultarLateral(lista))

                    lista4 = ordenarNome(consultarMeioCampo(lista))

                    lista5 = ordenarNome(consultarAtacante(lista))


                
                    lista = juntaTudo(lista1, lista2, lista3, lista4, lista5)


                    printar(lista, 'não')

                
                except FileNotFoundError:

                    print('\nEstá seleção não existe')


          

            elif (escolha == 'B'):

                lista = listaDeTudo()


                ver = ordenarIdade(consultarIdade(criarDicionario(lista)))

                printar(ver, 'sim')
                    



            elif (escolha == 'C'):

                lista = listaDeTudo()

                listaDicionario = criarDicionario(lista)


                lista1 = ordenarNome(consultarGoleiro(listaDicionario))

                lista2 = ordenarNome(consultarZagueiro(listaDicionario))

                lista3 = ordenarNome(consultarLateral(listaDicionario))

                lista4 = ordenarNome(consultarMeioCampo(listaDicionario))
                
                lista5 = ordenarNome(consultarAtacante(listaDicionario))

                consulta = juntaTudo(lista1, lista2, lista3, lista4, lista5)


                
                printar(consultarTime(consulta), 'sim')





            elif (escolha == 'D'):

                lista = listaDeTudo()

                listaDicionario = criarDicionario(lista)

                printar(ordenarGols(listaDicionario), 'sim')


            elif (escolha != 'R'):

                print('\noperação inválida')





    elif (sessao == 'S'):

        print()



    else:
        
        print('\noperação inválida')
        
        print()

    print('\n######################################################\n')
