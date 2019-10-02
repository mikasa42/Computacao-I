## Trabalho 2 computacao
## Juliana Barros de Sousa
## DRE: 119029876

def abrir (nome):                                         #funcao para testar se existe arquivo, abre ou cria

    for letras in nome:
        if ".txt" in nome:
            nome = nome [0:len(nome) - 4]

    try:
        arquivo = open (nome +'.txt', 'r+')

    except FileNotFoundError:
        arquivo = open (nome + '.txt', 'w')
        arquivo.close()
        arquivo = open (nome + '.txt', 'r+')

    return arquivo


def abrirCriar ():                                     #funcao para criar selecao que indica ao usuario se ela existe ou foi criada
    nome = input ("entre com o nome da Seleção desejado: ")
    print()

    for letras in nome:                                #tirar .txt caso o usuario insira
        if ".txt" in nome:
            nome = nome [0:len(nome) - 4]
    try:
        arquivo = open (nome +'.txt', 'r+')
        print ("essa seleção já existe! Para acessá-la, escolha a opção 5 do menu")

    except FileNotFoundError:
        arquivo = open (nome + '.txt', 'w')
        arquivo.close()
        arquivo = open (nome + '.txt', 'r+')
        print ("Seleção criada com sucesso!")
    return arquivo


def infoJog ():                                     #coleta as informacoes e retorn um dicionario do jogador

    nome = input ("digite o nome do jogador que deseja inserir: ")
    idade = input ("digite a idade do jogador: ")
    time = input ("digite o time do jogador: ")
    print ("(0) Goleiro\n(1) Atacante\n(2) Zagueiro\n(3) Lateral\n(5)Meio-Campo\n")
    posicao = input ("digite o numero correspondente a posição do jogador: ")
    gols = input ("digite a quantidade de gols do jogador: ")
    
    if posicao == '0':
        posicao = 'Goleiro'

    elif posicao == '1':
        posicao = 'Atacante'

    elif posicao == '2':
        posicao = 'Zagueiro '
    
    elif posicao == '3':
        posicao = 'Lateral'

    elif posicao == '4':
        posicao = 'Meio-Campo'

    string = nome.lower() + ';'+ idade.lower() + ';'+ time.lower() + ';'+ posicao.lower() + ';'+ gols.lower()
    return string



def stringInfo (Dicio):                          #transforma dicionario em string
    string = ''
    for i in Dicio:
        aux = Dicio[i] + ';'
        string = string + aux
    
    string = string [0:-1]
    return string


def imprimir (arquivo):                  #imprime arquivo 
    linhas = arquivo.readlines()
    for i in linhas:
        print (i, end = "")

def imprimirLista (lista):
    for linhas in lista:
        print (linhas)

def CriarLista (arquivo):             #retorna uma lista em que cada elemento é uma linha do arquivo
    lista = []
    linhas = arquivo.readlines()

    for i in linhas:
        i = i[:len(i)-1]
        lista += [i]

    cont = 1
    trocou = True
    while (trocou):
        trocou = False
        for pos in range (len(lista)-cont):
            if lista [pos] > lista [pos+1]:
                aux = lista [pos]
                lista [pos] = lista [pos +1]
                lista [pos+1] = aux
                trocou = True
        cont += 1
    
    return lista



def converteDicio (lista):                #transforma lista em uma lista de dicionarios
    listaNova = []
    dicio = {'nome': '', 'idade': '', 'time': '', 'posicao': '', 'gols': ''}
    nome = ''
    idade = ''
    time = ''
    posicao = ''
    gols = ''

    for elem in lista:
        inicio = 0
        pontoVirg = 0

        for cont in range (len(elem)):
            if ( elem[cont] == ";"):
                if (pontoVirg == 0):
                    nome = elem [inicio:cont]
                    inicio = cont +1
                    pontoVirg += 1

                elif (pontoVirg == 1):
                    idade = elem [inicio:cont]
                    inicio = cont +1
                    pontoVirg += 1

                elif (pontoVirg == 2):
                    time = elem [inicio:cont]
                    inicio = cont +1
                    pontoVirg += 1

                elif (pontoVirg == 3):
                    posicao = elem [inicio:cont]
                    inicio = cont +1
                    pontoVirg += 1


        dicio = {'nome': nome, 'idade': idade, 'time': time, 'posicao': posicao, 'gols': elem[cont:len(elem)]}
        listaNova += [dicio]

    return listaNova



def acharJog (nome,lista):                #acha o jogador em uma lista de dicionarios

    resultado  = -1
    achei = False
    for pos in range (len (lista)):
        if (lista [pos]['nome'] == nome):
            resultado = pos
            achei = True

    if achei == False:
        print ("Sinto muito, jogador não encontrado")

    return resultado

def comparaIdade (listaSelecoes,idade):               #procura por jogadores com idade menor do que a desejada
    listaInfo = []
    Dicio = {'pais':'', 'nome':'', 'idade': '', 'time':'', 'posicao': '', 'gols':''}

    for elem in listaSelecoes:
        arq = open (elem +'.txt','r+')
        arq = CriarLista(arq)
        arq = converteDicio(arq)
        for linha in arq:
            if ( linha['idade'] < idade):
                nome = linha['nome']
                idade1 = linha['idade']
                time = linha['time']
                posicao = linha['posicao']
                gols = linha['gols']
                pais = elem
                Dicio = {'pais':pais, 'nome':nome, 'idade': idade1, 'time':time, 'posicao': posicao, 'gols':gols}
                listaInfo += [Dicio]

    return listaInfo


def apagarLinha (nomeArq,linha):      #recebe arquivo, e escreve caso a linha nao seja a que o usuario quer apagar
    
    aux = open (nomeArq,'r+')
    linhas = aux.readlines()
    aux = open (nomeArq,'w')
    cont = 0
    for i in linhas:
        if (cont != linha):
            aux.write(i)
        cont += 1

    aux.close()
    return aux

def stringInfo (Dicio):              #transforma dicionario em string
    aux = ''
    string = ''

    for cont in range (len(Dicio)):
        for elem in Dicio:
            aux = Dicio[elem][cont]
            string += aux,';'

    return string

def listaPos (lista):                #ordena segundo as posicoes

    aux = ""
    trocou = True
    while trocou:
        trocou = False
        for cont in range (len(lista) - 1):
            key  = "posicao"
            if (lista[cont]["posicao"] == "zagueiro" and lista[cont +1]["posicao"] == "goleiro"):
                    print ('passando ',lista[cont][key])
                    print (lista[cont+1][key])
                    print ('trocou')
                    trocou = True
                    aux = lista[cont]
                    lista[cont] = lista[cont+1]
                    lista[cont+1] = aux
            elif (lista[cont]["posicao"] == "lateral" and lista[cont +1]["posicao"] == "goleiro"):
                    print ('passando ',lista[cont][key])
                    print (lista[cont+1][key])
                    print ('trocou')
                    trocou = True
                    aux = lista[cont]
                    lista[cont] = lista[cont+1]
                    lista[cont+1] = aux
            elif (lista[cont]["posicao"] == "meio-campo" and lista[cont +1]["posicao"] == "goleiro"):
                    print ('passando ',lista[cont][key])
                    print (lista[cont+1][key])
                    print ('trocou')
                    trocou = True
                    aux = lista[cont]
                    lista[cont] = lista[cont+1]
                    lista[cont+1] = aux
            elif (lista[cont]["posicao"] == "atacante" and lista[cont +1]["posicao"] == "goleiro"):
                    print ('passando ',lista[cont][key])
                    print (lista[cont+1][key])
                    print ('trocou')
                    trocou = True
                    aux = lista[cont]
                    lista[cont] = lista[cont+1]
                    lista[cont+1] = aux


            elif (lista[cont]["posicao"] == "lateral" and lista[cont +1]["posicao"] == "zagueiro"):
                    print ('passando ',lista[cont][key])
                    print (lista[cont+1][key])
                    print ('trocou')
                    trocou = True
                    aux = lista[cont]
                    lista[cont] = lista[cont+1]
                    lista[cont+1] = aux
            elif (lista[cont]["posicao"] == "meio-campo" and lista[cont +1]["posicao"] == "zagueiro"):
                    print ('passando ',lista[cont][key])
                    print (lista[cont+1][key])
                    print ('trocou')
                    trocou = True
                    aux = lista[cont]
                    lista[cont] = lista[cont+1]
                    lista[cont+1] = aux
            elif (lista[cont]["posicao"] == "atacante" and lista[cont +1]["posicao"] == "zagueiro"):
                    print ('passando ',lista[cont][key])
                    print (lista[cont+1][key])
                    print ('trocou')
                    trocou = True
                    aux = lista[cont]
                    lista[cont] = lista[cont+1]
                    lista[cont+1] = aux


            elif (lista[cont]["posicao"] == "meio-campo" and lista[cont +1]["posicao"] == "lateral" ):
                    print ('passando ',lista[cont][key])
                    print (lista[cont+1][key])
                    print ('trocou')
                    trocou = True
                    aux = lista[cont]
                    lista[cont] = lista[cont+1]
                    lista[cont+1] = aux
            elif (lista[cont]["posicao"] == "atacante" and lista[cont +1]["posicao"] == "lateral" ):
                    print ('passando ',lista[cont][key])
                    print (lista[cont+1][key])
                    print ('trocou')
                    trocou = True
                    aux = lista[cont]
                    lista[cont] = lista[cont+1]
                    lista[cont+1] = aux


            elif (lista[cont]["posicao"] == "atacante" and lista[cont +1]["posicao"] == "meio-campo"):
                    print ('passando ',lista[cont][key])
                    print (lista[cont+1][key])
                    print ('trocou')
                    trocou = True
                    aux = lista[cont]
                    lista[cont] = lista[cont+1]
                    lista[cont+1] = aux

            elif lista[cont]['posicao'] == lista[cont+1]['posicao']:              #ordena por ordem alfabetica caso as chaves tenham valores iguais
                if lista[cont]['nome']> lista[cont+1]['nome']:
                    aux = lista[cont]
                    lista[cont] = lista[cont+1]
                    lista[cont+1] = aux
                    trocou = True

    return lista
        
def ordenaEscolha (lista,ordem):                 #funcao para ordenar segundo uma das chaves do dicionario
    
    aux = ''
    cont2 = 1
    trocou = True

    while(trocou):
        trocou = False
        
        for cont in range (len(lista)-cont2):
            if lista[cont][ordem] > lista[cont+1][ordem]:
                aux = lista[cont]
                lista[cont] = lista[cont+1]
                lista[cont+1] = aux
                trocou = True
                    
            elif lista[cont][ordem] == lista[cont+1][ordem]:              #ordena por ordem alfabetica caso as chaves tenham valores iguais
                if lista[cont]['nome']> lista[cont+1]['nome']:
                    aux = lista[cont]
                    lista[cont] = lista[cont+1]
                    lista[cont+1] = aux
                    trocou = True
        cont2+=1

    return lista

def procuraNosArq (ListaArqNomes,tipo,procura):       #procura em todas as selecoes uma indo especifica 
    listaInfo = []
    Dicio = {'pais':'', 'nome':'', 'idade': '', 'time':'', 'posicao': '', 'gols':''}
    
    for elem in ListaArqNomes:
        arq = open (elem +'.txt','r+')
        arq = CriarLista(arq)
        arq = converteDicio(arq)
        for linha in arq:
            if ( linha[tipo] == procura):
                nome = linha['nome']
                idade = linha['idade']
                time = linha['time']
                posicao = linha['posicao']
                gols = linha['gols']
                pais = elem
                Dicio = {'pais':pais, 'nome':nome, 'idade': idade, 'time':time, 'posicao': posicao, 'gols':gols}
                listaInfo += [Dicio]

    return listaInfo



def menu ():
    print ('-'*30, 'MENU', '-'*30)
    print (' '*20,'BANCO DE DADOS DA COPA DO MUNDO',' '*10, '\n')
    print ('Selecione o número da opção desejada:')
    print ('1) Criar Seleção')
    print ('2) Acrescentar jogador à seleção existente')
    print ('3) Apagar jogador de seleção')
    print ('4) Atualizar numero de gols de um jogador')
    print ('5) Consultar jogadores e suas posições de uma seleção')
    print ('6) Consultar os jogadores que têm uma idade menor que uma determinada idade')
    print ('7) Consultar os jogadores de determinado time')
    print ('8) Consultar lista com os artilheiros dos times')
    print ('9) SAIR DO MENU')





def main ():
    armazena = abrir('selecoes')
    listaArmazena = CriarLista (armazena)
    opcao = 0

    while (opcao != 9):
        menu ()
        opcao = int (input())
        print ()

        if (opcao == 1):    #cria selecao e armazena seu nome em selecoes.txt
            print()
            nome = input ("insira o nome da selecao que deseja criar: ")

            if ".txt" in nome:                      #tira '.txt' do nome se tiver
                nome = nome [0:len(nome) - 4]
            
            try:                                        #teste para saber se selecao existe
                aberto = open (nome +'.txt', 'r+')
                abriu = 1
                print ("essa selecao ja existe!")
            
                if nome not in listaArmazena:         #caso a selecao exista e nao esteja no arquivo selecoes
                    armazena.seek(0,2)
                    armazena.write(nome.lower()+'\n')

            except FileNotFoundError:             #se nao existir, cria
                aberto = open (nome + '.txt', 'w')
                aberto = open (nome +'.txt', 'r+')
                armazena.seek(0,2)
                armazena.write(nome.lower()+'\n')
                print ("selecao criada com sucesso!")

            armazena.close()
            armazena = open('selecoes.txt','r+')

        elif (opcao == 2):                         #adciona jogadores em selecoes existentes
            nome = input ("em qual selecao: ")
            nome = nome.lower()
            for letras in nome:
                if ".txt" in nome:
                    nome = nome [0:len(nome) - 4]
            
            abriu = 0
            try:                                        #teste para saber se selecao existe
                aberto = open (nome +'.txt', 'r+')
                abriu = 1
            except FileNotFoundError:
                print ("selecao nao encontrada, selecione uma que exista")

            if abriu == 1:
                info = infoJog ()                       #info armazena a string com as informacoes do jogador
                aberto.seek(0,2)
                aberto.write (info + '\n' ) 
                aberto.close()
                print ("jogador adcionado com sucesso!")


        elif (opcao == 3):                    #apaga jogador de selecao
            escolha = input ("De qual seleção você deseja apagar um jogador?: ")
            for letras in escolha:
                if ".txt" in escolha:
                    escolha = escolha [0:len(nome) - 4]

            abriu = 0
            try:
                aberto = open (escolha +'.txt', 'r+')
                abriu = 1
                print ("achou")
            
            except FileNotFoundError:         #teste para saber se selecao existe
                print ("selecao nao encontrada, selecione uma que exista")

            if abriu == 1:
                apagar = input ("Qual jogador você deseja apagar?: ")
                lista = CriarLista(aberto)                  #cria lista apartir de um arquivo
                lista = converteDicio (lista)            #transforma cada elemento da lista em um dicionario
                nome = aberto.name                           #salva o nome do arquivo
                linha = acharJog(apagar, lista)           #acha o jogador em uma lista de dicioarios
                
                if linha != -1 : 
                    apagar = apagarLinha (nome,linha)
                    print ("jogador apagado! Para conferir a seleçao, escolha a opcao 5!")
                
                else:
                    print ("jogador não encontrado!")


        elif (opcao == 4):             #atualiza o numero de gols
            selecao = input ("de qual selecao é o jogador?: ")
            
            abriu = 0
            
            for letras in selecao:                         #tira '.txt' caso o usuario tenha colocado
                if ".txt" in selecao:
                    selecao = selecao [0:len(nome) - 4]
            try:
                aberto = open (selecao +'.txt', 'r+')       #testa para ver se o arquivo existe
                abriu = 1

            except FileNotFoundError:         
                print ("selecao nao encontrada, selecione uma que exista")

            if abriu == 1:            
                jogador = input ("de qual jogador você deseja atualizar o numero de gols?: ")
            
                lista = CriarLista(aberto)
                lista1 = converteDicio (lista)
                linha = acharJog (jogador,lista1)      #acha linha do jogador
            
            if (linha == -1):
                print ("jogador nao encontrado, selecione um que existe")

            else:                        #se linha for diferente de -1, o jogador esta na lista da selecao
                novoGols = input ("qual o numero de gols atualizado do jogador?: ")
            
                linhas = aberto.readlines()
                aberto = open(selecao + '.txt' ,'w')
                aberto.seek(0,0)
                
                cont = 0
                pontoVirg = 0
                novaLinha = ' ' 
                while (pontoVirg<4) and (cont<len(lista)):      #reescreve a linha tirando o que vem depois do 3 ponto virgula

                    for letras in lista[linha]:
                        if letras == ';':
                            if pontoVirg == 3:
                                novaLinha = lista[linha][:cont+1] + novoGols + '\n'
                            else: 
                                pontoVirg += 1
                        cont += 1
                
                for cont2 in range (len(lista)):
                    if cont2 != linha:
                        aberto.write(lista[cont2] + '\n')

                    else:
                        aberto.write(novaLinha)

                
                aberto.close()
                print ("numero de gols atualizado com sucesso")
            

        elif (opcao == 5):               #mostra informacoes de jogadores de uma selecao
            seleca = input("de qual selecao voce deseja ver os jogadores?: ")
            
            for letras in seleca:                         #tira '.txt' caso o usuario tenha colocado
                if ".txt" in seleca:
                    seleca = seleca [0:len(nome) - 4]
            try:
                aberto = open (seleca +'.txt', 'r+')       #testa para ver se o arquivo existe
                abriu = 1

            except FileNotFoundError:
                print ("selecao nao encontrada, selecione uma que exista")

            if abriu == 1:
                lista = CriarLista(aberto)
                print(lista)
                listDicio = converteDicio(lista)
                print (listDicio)
            aux = ''
            cont = 1
            trocou = True
            
            aux = listaPos(listDicio)
            print ()
            print ("NOME",' '*10,'POSICAO')
            
            for elem in aux:
                nome1 = elem['nome']
                posicao1 = elem['posicao']
                print (nome1,' '*10,posicao1)

        elif (opcao==8):
            
            listaArt = []
            dicio = {'nome': '', 'pais': '', 'gols': ''}

            for ele in listaArmazena:
                arq = open (ele + '.txt', 'r+')
                lista = CriarLista(arq)
                lista = converteDicio (lista)
                lista = ordenaEscolha(lista,'gols')
                nome = lista [len(lista)-1] ['nome']
                gols = lista [len(lista)-1] ['gols']

                dicio = {'nome':nome, 'pais':ele, 'gols': gols}
                listaArt += [dicio]

            print ('lista',listaArt)
            listaArt = ordenaEscolha (listaArt,'gols')
            print (listaArt)
            print ('                          LISTA DE ARTILHEIROS')
            print ("NOME", ' '*10, 'PAIS', ' '*10, 'gols', ' '*10)
            for elem in listaArt:
                nome1 = elem['nome']
                gols1 = elem['gols']
                pais1 = elem['pais']
                print (nome1,' '*10,pais1,' '*10,gols1)


        elif (opcao == 7):
            time = input ("de qual time voce deseja ver os jogadores?: ")
            info = procuraNosArq (listaArmazena,'time',time)
            print(info)
            info = listaPos(info)
            print(info)
            print ()
            print ("NOME",' '*10,'POSICAO',' '*10,'PAIS')
            for elem in info:
                nome1 = elem['nome']
                posicao1 = elem['posicao']
                pais1 = elem['pais']
                print (nome1,' '*10,posicao1,' '*10,pais1)



        elif (opcao==6):
            idade = input("abaixo de qual idade você deseja ver quais jogadores estão?: ")
            jogs = comparaIdade(listaArmazena,idade)
            print (jogs)
            jogs = ordenaEscolha(jogs,'idade')
            print (jogs)
            print ("NOME", ' '*10, 'PAIS', ' '*10, 'IDADE', ' '*10)
            for elem in jogs:
                nome1 = elem['nome']
                idade1 = elem['idade']
                pais1 = elem['pais']
                print (nome1,' '*10,pais1,' '*10,idade1)


        elif (opcao == 9):            
            print ('obrigada por utilizar o programa!')

        else:
            print ("Opcao invalida, escolha alguma do menu")


        print ()
main()

