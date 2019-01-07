"""
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
Centro de Informática (CIn) (http://www.cin.ufpe.br)
Graduando em Sistemas de Informação
IF968 - Programação 1

Autora: Izabella Priscylla da Costa Nascimento (ipcn)
Email: ipcn@cin.ufpe.br
Data: 22-05-2018
Copyright(c) 2018 Izabella Priscylla da Costa Nascimento
"""

from datetime import *


def lerUsuario():
    """Função para ler o usuário e retorna o dicionário contento o cadastros dos usuários, com senha e nível do usuário"""
    arq=open("usuarios.txt","r")
    lista=[]
    dicionario={}
    adicionar=""
    texto = arq.read()
    adicionar2 = ""
    texto2 = ""
    for caractere in texto:
        if caractere!=" ":
            adicionar2+=caractere
        else:
            texto2+=descriptografar(adicionar2)
            adicionar2=""
    for linha in texto2.split('\n'):
        adicionar = ""
        lista=[]
        for elemento in linha:
            if (elemento != ";")and (elemento!="\n"):
                adicionar+=elemento
            else:
                lista.append(adicionar)
                adicionar=""
        if lista:
            lista.append(adicionar)
            dicionario[lista[0]] = (lista[1], lista[2])
        lista=[]
    arq.close()
    return(dicionario)


def gravarArquivo(dicionario):
    """Função para gravar o dicionario no arquivo"""
    arq=open("usuarios.txt","w")
    string=""
    for x in dicionario:
        string+=x+";"+dicionario[x][0]+";"+dicionario[x][1]+"\n"
    stringNova=""
    for caractere in string:
        stringNova += str(criptografar(caractere)) + " "
    arq.write(stringNova)
    arq.close()


def buscarNivelLogin(bancoDeDados,usuario):
    """Função para buscar o nível do usuário"""
    nivel=bancoDeDados[usuario][1]
    return nivel


def nivelUsuario():
    """Funçao para adicionar o nível do usuário"""
    nivel=int(input("1 - Bibliotecário\n"
                    "2 - Atendente\n"
                    "3 - Visitante "))
    print("")
    if (nivel==1):
        nivel="Bibliotecário"
    elif (nivel==2):
        nivel="Atendente"
    elif (nivel==3):
        nivel="Visitante"
    else:
        print("Opção não encontrada, digite novamente.\n")
        print("Para qual nível deseja modificar?")
        return nivelUsuario()
    return nivel


def adicionarUsuario(bancoDeDados):
    """Função para adicionar um novo usuário do bando de dados"""
    login = input("\nDigite o login do usuário: ")
    achou = False
    for x in bancoDeDados:
        if login == x:
            achou = True
    if achou == False:
        senha=input("Didite a senha: ")
        print("")
        bancoDeDados[login] = (senha,"Visitante")
        log(usuario, "adicionou_usuário")
    else:
        print("\nLogin já cadastrado.\n")
    return bancoDeDados


def removerUsuario(bancoDeDados):
    """Função para remover um usuário do bando de dados"""
    login = input("\nDigite o login do usuário: ")
    print("")
    if login in bancoDeDados:
        bancoDeDados.pop(login)
        log(usuario, "removeu_usuário")
    else:
        print("Usuário não consta no sistema.\n")
    return bancoDeDados


def modificarNivelUsuario(bancoDeDados):
    """Função para modificar o nível do usuário"""
    print("")
    usuario=input("Qual usuário deseja modificar? ")
    print("")
    print("Para qual nível deseja modificar?")
    bancoDeDados[usuario]=(bancoDeDados[usuario][0],nivelUsuario())
    log(usuario, "modificou_nível_de_usuário")
    return bancoDeDados


def lerElemento():
    """Função para ler os elementos e retorna o dicionário contento o cadastros dos elementos com ISBN, título, autor,
    número de chamada, edição,acervo, ano de publicação"""
    arq=open("elementos.txt","r")
    lista=[]
    dicionarioElementos={}
    adicionar=""
    texto = arq.read()
    adicionar2=""
    texto2=""
    for caractere in texto:
        if caractere!=" ":
            adicionar2+=caractere
        else:
            texto2+=descriptografar(adicionar2)
            adicionar2=""
    for linha in texto2.split('\n'):
        adicionar = ""
        for elemento in linha:
            if (elemento != ";")and (elemento!="\n"):
                adicionar+=elemento
            else:
                lista.append(adicionar)
                adicionar=""
        if lista:
            lista.append(adicionar)
            dicionarioElementos[lista[0]]=(lista[1],lista[2],lista[3],lista[4],lista[5],lista[6])
        lista=[]
    arq.close()
    return(dicionarioElementos)


def gravarElementoArquivo(dicionarioElementos):
    """Função para gravar o dicionario dos elementos no arquivo"""
    arq=open("elementos.txt","w")
    string=""
    for x in dicionarioElementos:
        string+=x+";"+dicionarioElementos[x][0]+";"+dicionarioElementos[x][1]+";"+dicionarioElementos[x][2]+";"+dicionarioElementos[x][3]+";"+dicionarioElementos[x][4]+";"+dicionarioElementos[x][5]+"\n"
    stringNova=""
    for caractere in string:
        stringNova+=str(criptografar(caractere)) +" "
    arq.write(stringNova)
    arq.close()


def adicionarElemento(bancoDeDadosElementos):
    """Função para adicionar livros"""
    ISBN = input("\nDigite o ISBN: ")
    achou = False
    for x in bancoDeDadosElementos:
        if ISBN == x:
            achou = True
    if achou == False:
        titulo=input("Digite o título do livro: ")
        autor=input("Digite o autor do livro: ")
        numeroDeChamada=input("Digite o número de chamada do livro: ")
        edicao=input("Digite a edição do livro: ")
        acervo=input("Digite o acervo do livro: ")
        anoDePublicacao=input("Digite o ano de publicação do livro: ")
        print("")
        bancoDeDadosElementos[ISBN] = (titulo,autor,numeroDeChamada,edicao,acervo,anoDePublicacao)
        log(usuario, "adicionou_elemento")
    else:
        print("\nISBN já cadastrado.\n")
    return bancoDeDadosElementos


def removerElemento(bancoDeDadosElementos):
    """Função para remover livro"""
    ISBN = input("\nDigite o ISBN: ")
    print("")
    if ISBN in bancoDeDadosElementos:
        bancoDeDadosElementos.pop(ISBN)
        log(usuario, "removeu_elemento")
    else:
        print("\nLivro não cadastrado no sistema.")
    return bancoDeDadosElementos


def buscarElemento(bancoDeDadosElementos):
    """Função buscar livro"""
    opcao=int(input("\nComo deseja buscar o livro?\n"
                    "1 - ISBN\n"
                    "2 - Título\n"
                    "3 - Autor "))
    print("")
    if opcao==1:
        ISBN=input("Digite o ISBN: ")
        if ISBN in bancoDeDadosElementos:
            return ISBN
        else:
            return False
    elif opcao==2:
        titulo=input("Digite o título: ")
        for atributo in bancoDeDadosElementos.items():
            if atributo[1][0]==titulo:
                return atributo[0]
        return False
    elif opcao==3:
        autor = input("Digite o título: ")
        achou=False
        for atributo in bancoDeDadosElementos.items():
            if atributo[1][1] == autor:
                return atributo[0]
        return False
    else:
        print("Opção não encontrada, digite novamente.")
        buscarElemento(bancoDeDadosElementos)

def atualizarElemento(bancoDeDadosElementos,usuario):
    """Função para atualizar os livros"""
    opcao=buscarElemento(bancoDeDadosElementos)
    if opcao==False:
        print("\nElemento não cadastrado no sistema.\n")
    else:
        atualizar=int(input("\n-------O que deseja atualizar?------\n"
                            "1 - Título\n"
                            "2 - Autor\n"
                            "3 - Número de chamada\n"
                            "4 - Edição\n"
                            "5 - Acervo\n"
                            "6 - Ano de Publicação "))
        if (atualizar<1)or(atualizar>6):
            print("\nOpção não encontrada, digite novamente.")
            return atualizarElemento(bancoDeDadosElementos,usuario)
        elementosDaChave = list(bancoDeDadosElementos[opcao])
        elementosDaChave[atualizar-1] = input("\nDigite o novo atributo: ")
        print("")
        bancoDeDadosElementos[opcao]=tuple(elementosDaChave)
        log(usuario,"atualizou_elemento")
    return bancoDeDadosElementos


def log(usuario,acao):
    """Função log"""
    arq=open("log.txt","a")
    tempo = datetime.today()
    dia=str(tempo.day)
    mes=str(tempo.month)
    if len(dia)==1:
        dia="0"+dia
    if len(mes)==1:
        mes="0"+mes
    lista=[]
    arq.write(usuario + " " + acao + " em " +dia+"-"+mes+"-"+str(tempo.year) + " as "
              + str(tempo.hour) + ":" + str(tempo.minute) + ":" + str(tempo.second)+"\n")
    arq.close()


def tipoBuscaLog():
    """Função para saber qual parâmetro buscar o log"""
    opcao=int(input("\nComo deseja buscar o log?\n"
                    "1 - Data de execução\n"
                    "2 - Usuário "))
    if opcao==1:
        data=input("\nDidite a data: (dd-mm-aaa)")
        print("")
        return data
    elif opcao==2:
        usuario = input("\nDigite o usuário: ")
        print("")
        return usuario
    else:
        print("\nOpção não encontrada, digite novamente.")
        return tipoBuscaLog()


def buscarLog():
    """Função para buscar o log"""
    arq=open("log.txt","r")
    lista=[]
    adicionar=""
    opcao=tipoBuscaLog()
    for string in arq.readlines():
        for caractere in string:
            if (caractere != " ") and (caractere != "\n"):
                adicionar += caractere
            else:
                lista.append(adicionar)
                adicionar = ""
        if opcao==lista[3]:
            print(""+lista[0]+" "+lista[1]+" "+lista[2]+" "+lista[3]+" "+lista[4]+" "+lista[5])
        elif opcao==lista[0]:
            print(""+lista[0]+" "+lista[1]+" "+lista[2]+" "+lista[3]+" "+lista[4]+" "+lista[5])
        lista=[]
    print("")
    arq.close()


def lerChaves(caminho):
    """Função para ler as chaves"""
    arq=open(caminho+".txt","r")
    lista=[]
    string = ""
    for caractere in arq.read():
        if caractere!=" ":
            string+=caractere
        else:
            lista.append(int(string))
            string=""
    lista.append(int(string))
    arq.close()
    return lista[0],lista[1]


def criptografar(x):
    """Função para criptografar"""
    chave1Publica,chave2Publica= lerChaves("chavePublica")
    y = ord(x)**chave1Publica%chave2Publica
    return y


def descriptografar(y):
    """Função para descriptografar"""
    chave1Privada,chave2Privada=lerChaves("chavePrivada")
    x = chr(int(y)**chave1Privada%chave2Privada)
    return x


def ordenarElementos(bancoDeDadosElementos):
    """Função para ordenar os elementos"""
    lista=[]
    for chave in bancoDeDadosElementos:
        lista.append(int(chave))
    ordenado=sorted(lista)
    arq=open("impressaoelementos.txt","w")
    for x in ordenado:
        arq.write("ISBN: "+str(x)+", Título: "+bancoDeDadosElementos[str(x)][0]+", Autor: "
                  +bancoDeDadosElementos[str(x)][1]+", Número de chamada: "+bancoDeDadosElementos[str(x)][2]+", Edição: "
                  +bancoDeDadosElementos[str(x)][3]+", Acervo: "+bancoDeDadosElementos[str(x)][4]+", Ano de Publicação:"
                  +bancoDeDadosElementos[str(x)][5])
        arq.write("\n")
    arq.close()


def buscarNaTela(bancoDeDadosElementos):
    """Função para imprimir na tela a busca do elemento"""
    ISBN=buscarElemento(bancoDeDadosElementos)
    if (ISBN!=False):
        print("\nISBN: " + ISBN +"\nTítulo: " + bancoDeDadosElementos[ISBN][0] +"\nAutor: " + bancoDeDadosElementos[ISBN][1] +
              "\nNúmero de chamada: " + bancoDeDadosElementos[ISBN][2] +"\nEdição: " + bancoDeDadosElementos[ISBN][3] +
              "\nAcervo: " + bancoDeDadosElementos[ISBN][4] +"\nAno de publicação: " + bancoDeDadosElementos[ISBN][5])
        print("")
        log(usuario, "buscou_elemento")
    else:
        print("\nLivro não cadastrado no sistema.\n")


def mainNivelBibliotecario():
    """Função menu do usuário maior nível"""
    opcao=int(input("-------O que deseja fazer?-------\n"
                    "1 - Adicionar usuário\n"
                    "2 - Remover Usuário\n"
                    "3 - Modificar nível do usuário\n"
                    "4 - Remover livro\n"
                    "5 - Adicionar livro\n"
                    "6 - Atualizar livro\n"
                    "7 - Buscar livro\n"
                    "8 - Buscar nos logs\n"
                    "9 - Logout "))
    return opcao


def mainNivelAtendente():
    """Função menu do usuário de nível intermediário """
    opcao=int(input("-------O que deseja fazer?-------\n"
                    "1 - Adicionar livro\n"
                    "2 - Atualizar livro\n"
                    "3 - Buscar livro\n"
                    "4 - Logout "))
    return opcao


def mainNivelVisitante():
    """Função menu do usuário de nível visitante"""
    opcao=int(input("-------O que deseja fazer?-------\n"
                    "1 - Buscar livro\n"
                    "2 - Logout "))
    return opcao


def login(bancoDeDados):
    """Função para logar"""
    continuar = False
    while continuar == False:
        login=input("Digite o login: ")
        senha=input("Digite a senha: ")
        print("")
        if login in bancoDeDados:
            if senha==bancoDeDados[login][0]:
                usuario=login
                log(usuario, "logou")
                return usuario
            else:
                print("Senha não corresponde ao usuário.\n")
        else:
            print("Login não cadastrado no banco de dados.\n")


opcao=0
bancoDeDados = lerUsuario()
bancoDeDadosElementos=lerElemento()
continuarGeral=True


while(continuarGeral==True):
    """Laço para encerrar o programa"""
    verificar=int(input("\nO que deseja fazer? \n"
                    "1 - Login\n"
                    "2 - Sair do progama "))
    print("")
    if verificar==1:
        usuario=login(bancoDeDados)
        nivel=buscarNivelLogin(bancoDeDados,usuario)
        if nivel=="Bibliotecário":
            continuar=True
            while continuar==True:
                """Laço para encerrar o nível do bibliotecário"""
                opcao=mainNivelBibliotecario()
                if opcao==1:
                    bancoDeDados = adicionarUsuario(bancoDeDados)
                elif opcao==2:
                    removerUsuario(bancoDeDados)
                elif opcao==3:
                    modificarNivelUsuario(bancoDeDados)
                elif opcao==4:
                    removerElemento(bancoDeDadosElementos)
                elif opcao==5:
                    adicionarElemento(bancoDeDadosElementos)
                elif opcao==6:
                    atualizarElemento(bancoDeDadosElementos,usuario)
                elif opcao==7:
                    buscarNaTela(bancoDeDadosElementos)
                elif opcao==8:
                    buscarLog()
                elif opcao==9:
                    log(usuario, "deslogou")
                    continuar=False
                else:
                    print("\nOpção não encontrada, digite novamente.\n")
        elif nivel=="Atendente":
            continuar = True
            while continuar == True:
                """Laço para encerrar o nível do atendente"""
                opcao=mainNivelAtendente()
                if opcao==1:
                    adicionarElemento(bancoDeDadosElementos)
                elif opcao==2:
                    atualizarElemento(bancoDeDadosElementos)
                elif opcao==3:
                    buscarNaTela(bancoDeDadosElementos)
                elif opcao==4:
                    log(usuario, "deslogou")
                    continuar=False
                else:
                    print("\nOpção não encontrada, digite novamente.\n")
        else:
            continuar = True
            while continuar == True:
                """Laço para encerrar o nível do visitante"""
                opcao=mainNivelVisitante()
                if opcao==1:
                    buscarNaTela(bancoDeDadosElementos)
                elif opcao==2:
                    log(usuario, "deslogou")
                    continuar=False
                else:
                    print("\nOpção não encontrada, digite novamente.\n")
    elif verificar==2:
        continuarGeral=False
    else:
        print("Opção não encontrada, digite novamente.")

gravarArquivo(bancoDeDados)
gravarElementoArquivo(bancoDeDadosElementos)
ordenarElementos(bancoDeDadosElementos)
