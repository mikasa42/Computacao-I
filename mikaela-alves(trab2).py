def abrirArquivo(nomeSelecao):
                                        #Esta funcao tenta abrir os arquivos das selecoes solicitadas
  try:
    arquivo = open(nomeSelecao +'.txt','r+')
    return arquivo
  except:
      #Caso não tenha essa selecao, essa funcao chama criar selecao para cria -la e continuar o programa 
    print('Nao existe essa selecao, deseja cria-la?\n')
    print('Escolha uma das opcoes a seguir')
    print('[1] - Se deseja criar esta selecao ')
    print('[2] - Se deseja sair do programa')
    operaOpcao = int(input())
    if(operaOpcao == 1):
      criarSelecao(nomeSelecao)
    else:
        print('Obrigado por usar nosso sistema, digite 6 para sair')
        # pensar numa forma de sair do programa daqui
def criarSelecao(nomeSelecao):
                                        #Essa funcao cria uma selecao e adiciona o nome da selecao em um aquivo selecoes.txt
  try:
    arquivo = open(nomeSelecao +'.txt','r+')
    print('Selecao ja existente')
    arquivo.close()
  except:
    arquivo = open(nomeSelecao +'.txt','w')
    arquivo = open('Selecoes.txt','a')
    nomeSelecao += '\n'
    arquivo.write(nomeSelecao+'.txt')
    print('Nova selecao criada')
    arquivo.close()

def adicionarJogador(nomeSelecao):
  abrirArquivo(nomeSelecao)
  arquivo = abrirArquivo(nomeSelecao)
  arquivo = open(nomeSelecao+'.txt','a')
                                    #funcao que adciona jogador, em uma determinada funcao
  a = 1
  Jogadores = []
  nome = input('Digite o nome do jogador:\n')
  idade = int(input('Digite a idade do jogador:\n'))
  posicao = input('Digite a posicao do jogador:\n')
  time = input('Digite o time do jogador:\n')
  gols = int(input('Digite os gols marcados na copa por esse jogador:\n'))
                                    #Grava os dados em um dicionario para facilitar a gravação dos dados no arquivo
  Jogador = {'Nome':nome,'Idade':idade,'Posicao':posicao,'Time':time,'Gols':gols,'Selecao':nomeSelecao}
  Jogadores += [Jogador]
  a = 0
  print('Deseja adicionar mais algum jogador ?')
  print('[1] - Caso deseje adicionar mais um jogador ')
  print('[2] - Caso deseje sair')
  a = int(input())
  if(a == 1):
    adicionarJogador(nomeSelecao)
  if(a == 2):
      print('lista de jogadores adicionados')
      print(Jogadores)
      for i in range(len(Jogadores)):
        print(
            Jogadores[i]['Nome'] +' ,'+
            str(Jogadores[i]['Idade']) +' ,'+
            Jogadores[i]['Posicao']+' ,'+
            Jogadores[i]['Time']+' ,'+
            str(Jogadores[i]['Gols'])+ ',' +
            Jogadores[i]['Selecao']+
            
      '\n')
                                    #Escrevendo no arquivo, de forma que fique apenas os valores no arquivo 
  for i in range(len(Jogadores)):
    arquivo.write(
      Jogadores[i]['Nome'] +';'+
      str(Jogadores[i]['Idade']) +';'+ 
      Jogadores[i]['Posicao']+';'+
      Jogadores[i]['Time']+';'+
      str(Jogadores[i]['Gols'])+';'+
      Jogadores[i]['Selecao']+
      
      '\n')
    arquivo.close()
def excluirJogador():
    nomeSelecao = input('Digite o nome da seleção do jogador\n')
    nomeJogador = input('Digite o nome do jogador\n')
    try:
        arquivo = open(nomeSelecao+'.txt','r+')
    except FileNotFoundError:
        print('Essa selecao nao existe')
    print('Parou aqui')
    listaJogadores = arquivo.readlines()
    jogadores = []
    print(listaJogadores)
    for linha in listaJogadores:
        linha = linha[:-1] + ';'
        nome = ''
        idade = 0
        time = ''
        posicao = ''
        gols = 0
        jogador = {'Nome':nome,'Idade':idade,'Posicao':posicao,'Time':time,'Gols':gols,'Selecao':nomeSelecao}
        pontoVirgula = 1
        index = 0
        while(pontoVirgula < 6):
            letra = ''
            while(linha[index] != ';'):
                letra += linha[index]
                index +=1
                if(pontoVirgula == 1):
                    nome = letra
                if(pontoVirgula == 2):
                    idade = int(letra)
                if(pontoVirgula == 3):
                    posicao = letra
                if(pontoVirgula == 4):
                    time = letra
                if(pontoVirgula == 5):
                    gols = int(letra)
            pontoVirgula +=1
            index +=1

    jogador = {'Nome':nome,'Idade':idade,'Posicao':posicao,'Time':time,'Gols':gols,'Selecao':nomeSelecao}
    jogadores += [jogador]   
    listaNova = []
    naoAchei = False
    for i in range (len(jogadores)):
        if(jogadores[i]['Nome'] == nomeJogador):
            i = i+1
            naoAchei = True
            print('Jogador deletado do sistema!')
        else:
            listaNova += [jogadores[i]]
    if(naoAchei == False):
        print('Nao existe esse jogador')
    print(listaNova)
      # if(jogador['Nome'] != nomeJogador):
       # print('Nao existe esse jogador')
      #salvando os dados depois do dicionario atualizado
    arquivo = open(nomeSelecao + '.txt','w')
    for jogador in (listaNova):
        arquivo.write(
            listaNova[i]['Nome'] +';'+
            str(listaNova[i]['Idade']) +';'+ 
            listaNova[i]['Posicao']+';'+
            listaNova[i]['Time']+';'+
            str(listaNova[i]['Gols'])+';'+
            Jogadores[i]['Selecao']+
                '\n')
    arquivo.close ()
def atualizarJogador():
    nomeSelecao = input('Digite o nome da seleção do jogador\n')
    nomeJogador = input('Digite o nome do jogador\n')
    try:
        arquivo = open(nomeSelecao+'.txt','r+')
    except FileNotFoundError:
        print('Essa selecao nao existe')
    print('Parou aqui')
    listaJogadores = arquivo.readlines()
    jogadores = []
    print(listaJogadores)
    for linha in listaJogadores:
        linha = linha[:-1] + ';'
        nome = ''
        idade = 0
        time = ''
        posicao = ''
        gols = 0
        jogador = {'Nome':nome,'Idade':idade,'Posicao':posicao,'Time':time,'Gols':gols,'Selecao':nomeSelecao}
        pontoVirgula = 1
        index = 0
        while(pontoVirgula < 6):
            letra = ''
            while(linha[index] != ';'):
                letra += linha[index]
                index +=1
                if(pontoVirgula == 1):
                    nome = letra
                if(pontoVirgula == 2):
                    idade = int(letra)
                if(pontoVirgula == 3):
                    posicao = letra
                if(pontoVirgula == 4):
                    time = letra
                if(pontoVirgula == 5):
                    gols = int(letra)
            pontoVirgula +=1
            index +=1

    jogador = {'Nome':nome,'Idade':idade,'Posicao':posicao,'Time':time,'Gols':gols,'Selecao':nomeSelecao}
    jogadores += [jogador]   
    listaNova = []
    naoAchei = False
    for i in range (len(jogadores)):
        if(jogadores[i]['Nome'] == nomeJogador):
            jogadores[i]['Gols'] = int(input('Digite o saldo de gols atual'))
            listaNova += [jogadores[i]]
            naoAchei = True
            print('Jogador atualizado no sistema!')
        else:
            listaNova += [jogadores[i]]
    print(listaNova)
    if(naoAchei == False):
        print('Nao existe esse jogador')
      #salvando os dados depois do dicionario atualizado
    arquivo = open(nomeSelecao + '.txt','w')
    for jogador in (listaNova):
        arquivo.write(
            listaNova[i]['Nome'] +';'+
            str(listaNova[i]['Idade']) +';'+ 
            listaNova[i]['Posicao']+';'+
            listaNova[i]['Time']+';'+
            str(listaNova[i]['Gols'])+';'+
            Jogadores[i]['Selecao']+
                '\n')
    arquivo.close ()
def consultaPais():
    nomeSelecao = input('Digite o nome da seleção do jogador\n')
    try:
        arquivo = open(nomeSelecao+'.txt','r+')
    except FileNotFoundError:
        print('Essa selecao nao existe')
    print('Parou aqui')
    listaJogadores = arquivo.readlines()
    jogadores = []
    print(listaJogadores)
    for linha in listaJogadores:
        linha = linha[:-1] + ';'
        nome = ''
        idade = 0
        time = ''
        posicao = ''
        gols = 0
        jogador = {'Nome':nome,'Idade':idade,'Posicao':posicao,'Time':time,'Gols':gols,'Selecao':nomeSelecao}
        pontoVirgula = 1
        index = 0
        while(pontoVirgula < 6):
            letra = ''
            while(linha[index] != ';'):
                letra += linha[index]
                index +=1
                if(pontoVirgula == 1):
                    nome = letra
                if(pontoVirgula == 2):
                    idade = int(letra)
                if(pontoVirgula == 3):
                    posicao = letra
                if(pontoVirgula == 4):
                    time = letra
                if(pontoVirgula == 5):
                    gols = int(letra)
            pontoVirgula +=1
            index +=1

        jogador = {'Nome':nome,'Idade':idade,'Posicao':posicao,'Time':time,'Gols':gols,'Selecao':nomeSelecao}
        jogadores += [jogador]
    print(jogadores)
    listaOrdenada = []
    condicao = 1
    while len(listaOrdenada) < len(jogadores) and condicao < 6:
      if condicao == 1:
        comparador = 'goleiro'
      elif condicao == 2:
          comparador = 'zagueiro'
      elif condicao == 3:
          comparador = 'lateral'
      elif condicao == 4:
          comparador = 'meio-campo'
      elif condicao == 5:
          comparador = 'atacante'
      cont = 0
      while cont < len(jogadores):
        if (jogadores[cont]["Posicao"] == comparador):
                listaOrdenada +=[jogadores[cont]]
        cont += 1
      condicao += 1
    print(listaOrdenada)
         #colocando em ordem em ordem alfabetica
    cont = 0
    aux = ""
    trocou = True
    while trocou:
        trocou = False
        for cont in range (len(listaOrdenada) - 1):
            if (listaOrdenada[cont]['Posicao'] == listaOrdenada[cont+1]['Posicao']):              #ordena por ordem alfabetica caso as chaves tenham valores iguais
                if (listaOrdenada[cont]['Nome']> listaOrdenada[cont+1]['Nome']):
                    aux = listaOrdenada[cont]
                    listaOrdenada[cont] = listaOrdenada[cont+1]
                    listaOrdenada[cont+1] = aux
                    trocou = True
    print(listaOrdenada)
def consultaIdade():
    
    arquivo = open('selecoes.txt','r')
    paises = arquivo.readlines()
    pais = []
    cont = 0
    inicio = 0
    for cont in  paises:
        print(cont)
        for i in range (len(cont)):
            if('\n' in cont):
                pais += cont[:-1]         
    print(pais)
    listaTodosJogadores = ''
    aux = 0
    for aux in pais:
        arquivo = open(aux,'r')
        listaTodosJogadores = listaTodosJogadores +'\n' + arquivo.readlines()

    limiteIdade = int(input('Digite o limite de idade dos jogadores selecionados'))
    jogadores = []
    print(listaTodosJogadores)
    for linha in listaTodosJogadores:
        linha = linha[:-1] + ';'
        nome = ''
        idade = 0
        time = ''
        posicao = ''
        gols = 0
        jogador = {'Nome':nome,'Idade':idade,'Posicao':posicao,'Time':time,'Gols':gols,'Selecao':selecao}
        pontoVirgula = 1
        index = 0
        while(pontoVirgula < 6):
            letra = ''
            while(linha[index] != ';'):
                letra += linha[index]
                index +=1
                if(pontoVirgula == 1):
                    nome = letra
                if(pontoVirgula == 2):
                    idade = int(letra)
                if(pontoVirgula == 3):
                    posicao = letra
                if(pontoVirgula == 4):
                    time = letra
                if(pontoVirgula == 5):
                    gols = int(letra)
                    selecao = pais[i]
            pontoVirgula +=1
            index +=1

        jogador = {'Nome':nome,'Idade':idade,'Posicao':posicao,'Time':time,'Gols':gols,'Selecao':selecao}
        jogadores += [jogador]
    print(jogadores)
    listaNova = []
    for i in range (len(jogadores)):
        if(jogadores[i]['Idade'] <= limiteIdade):
            listaNova += [jogadores[i]]
    cont = 0
    aux = ""
    trocou = True
    while trocou:
        trocou = False
        for cont in range (len(listaOrdenada) - 1):              #ordena por ordem alfabetica caso as chaves tenham valores iguais
                if (listaNova[cont]['Idade']< listaNova[cont+1]['Idade']):
                    aux = listaOrdenada[cont]
                    listaNova[cont] = listaNova[cont+1]
                    listaNova[cont+1] = aux
                    trocou = True
    print(listaNova)
    
        
        
def main():
  operaMenu = 1
  print("Ola, quais das opcoes voce deseja")
  while(operaMenu != 6):
    
    print("[1] - criar selecao")
    print("[2] - adicionar jogador ")
    print("[3] - excluir jogador")
    print("[4] - atualizar jogador ")
    print("[5] - tipos de consulta")
    print("[6] - Se deseja sair ")
  
    operaMenu = int(input())
    if(operaMenu == 1):
      opcao =-1
      print('[1] - Uma selecao')
      print('[2] - Varias selecoes')
      opcao = int(input())
      if(opcao == 2):
        varias = int(input('Quantas selecoes?\n'))
        for i in range (varias):
          nomeSelecao = input('Digite os nome da selecao :\n')
          criarSelecao(nomeSelecao)
      elif(opcao == 1):
          nomeSelecao = input('Digite o nome da selecao\n')
          criarSelecao(nomeSelecao)
    elif(operaMenu == 2):
        nomeSelecao = input('Digite o nome da seleção do jogador\n')
        adicionarJogador(nomeSelecao)
    elif(operaMenu == 3):
        excluirJogador()
    elif(operaMenu == 4):
         atualizarJogador()
    #Nessa parte criei um novo menu para os tipos de consulta
    elif(operaMenu == 5):
                  print('[1] - Por pais')
                  print('[2] - Por idade')
                  print('[3] - Por time')
                  print('[4] - Por artilheiros')
                  opcao = int(input())
                  if(opcao == 1):
                    consultaPais()
                  elif(opcao == 2):
                    consultaIdade()
                  elif(opcao == 3):
                    consultaTime(nomeTime)
                  elif(opcao == 4):
                    consultaArtilheiro(nomeArtilheiro)
                  
main()
