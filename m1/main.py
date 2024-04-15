#Ítalo de Andrade Teles Ocimar Lima
import time
import os
import getpass

def excluir_arquivo():

    listar_arquivo()
    nome_arquivo=input("insira o nome do arquivo que deseja excluir: ")
    print("=-=-=-=-=-=-=-=-=-=") 
    caminho_arquivo=os.path.join("arquivos",nome_arquivo)
    if os.path.exists(caminho_arquivo):
        os.remove(caminho_arquivo)
        print("!!!Arquivo excluído com sucesso!!!")
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= \n")
    else:
        print("O arquivo não existe ou não pode ser encontrado.")
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= \n")

def listar_arquivo():

    path=r"arquivos"
    if os.path.isdir(path):

        conteudo = os.listdir(path)

        print(f"arquivos: \n")
        for item in conteudo:
            print(item)
            print("\n")
            time.sleep(1)

def ler_arquivo():
    listar_arquivo()
    nome_arquivo=input("insira qual arquivo deseja ler: ")
    print("=-=-=-=-=-=-=-=-=-=") 
    caminho_arquivo = os.path.join("arquivos", nome_arquivo)
    try:
        with open(caminho_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
    except FileNotFoundError:
        print("Arquivo não encontrado.")

def execução_mestre(permissão_ler, permissão_escrever, permissão_excluir):
    while True:

        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("funções disponíveis:")
        print("0-listar arquivos")
        print("1-ler")
        print("2-editar")
        print("3-excluir")
        print("4-sair")
        escolha_fc = int(input("qual função você deseja realizar?: "))
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        if escolha_fc == 0:
            time.sleep(1)
            listar_arquivo()
        elif escolha_fc == 1:
            if permissão_ler==1:
                time.sleep(1)
                ler_arquivo()
            else:
                time.sleep(1)
                print("!!você não tem permissão para executar esta função!!")
       
        elif escolha_fc == 2:
            if permissão_escrever==1:
                print("...em desenvolvimento...")
            else:
                print("!!você não tem permissão para executar esta função!!")
        
        elif escolha_fc == 3:
            if permissão_excluir==1:
                excluir_arquivo()
            else:
                print("!!você não tem permissão para executar esta função!!")
       
        elif escolha_fc == 4:
            print("tchau!! :3 ...")
            break
        else:
            print("Escolha inválida. Por favor, escolha uma opção válida.")

def definir_permissões(nome_usuario):
    global permissão_leitura
    global permissão_escrever
    global permissão_excluir    
    with open('permissoes.txt','r') as permissoes_arquivo:
        linhas = permissoes_arquivo.readlines()
        for linha in linhas:
            partes = linha.strip().split(':')
            if partes[0] == nome_usuario:
                permissões = partes[1].strip().split(',')
                permissão_leitura, permissão_escrever, permissão_excluir= map(int, permissões)
                break

    return permissão_leitura, permissão_escrever, permissão_excluir
              
def logar_usuario(nome_usuario, senha):
    with open('usuarios.txt', 'r') as login_arquivo:
        linhas = login_arquivo.readlines()
        for linha in linhas:
            partes = linha.strip().split(',')
            usuario = None
            senha_usuario = None
            for parte in partes:
                if 'usuario' in parte:
                    usuario = parte.split(':')[1].strip()
                elif 'senha' in parte:
                    senha_usuario = parte.split(':')[1].strip()
            if usuario == nome_usuario and senha_usuario == senha:
                definir_permissões(nome_usuario)
                return True
        return False

def cadastrar_usuario():
    usuario = input("Insira o seu perfil de usuário: ")
    senha = getpass.getpass(prompt='insira a sua senha: ', stream=None)
    senha2 = getpass.getpass(prompt='insira novamente a sua senha: ', stream=None)
    while senha != senha2:
        print("=-=-=-=-=-=-=-=-=-=-=-=")
        print("!! AS SENHAS DIGITADAS NÃO CORRESPONDEM TENTE NOVAMENTE !!")
        print("=-=-=-=-=-=-=-=-=-=-=-=")
        senha = getpass.getpass(prompt='insira a sua senha: ', stream=None)
        senha2 = getpass.getpass(prompt='insira novamente a sua senha: ', stream=None)  
    print("=-=-=-=-=-=-=-=-=-=-=-=")
    print("!! CADASTRO REALIZADO COM SUCESSO !!")
    print("=-=-=-=-=-=-=-=-=-=-=-=")
    
    with open('usuarios.txt', 'a') as arquivo:
        arquivo.write(f"usuario: {usuario}, senha: {senha}\n")
    with open('permissoes.txt', 'a') as arquivo:
        arquivo.write(f"{usuario}: {0}, {0}, {0}\n")

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#

while True:

    permissão_leitura=0
    permissão_escrever=0
    permissão_excluir=0
    print("=-=-=-=-=-=-=-=")
    print("1 - Logar")
    print("2 - Cadastrar")
    print("3 - Sair")
    print("=-=-=-=-=-=-=-=")
    escolha = int(input("Insira a sua escolha: "))
    if escolha == 3:
        print("TCHAU :3")
        break          
    elif escolha == 2:
        cadastrar_usuario()
        
    elif escolha == 1:
        while True:
            usuario_login = input("Insira o seu usuário: ")
            senha_login = getpass.getpass(prompt='insira a sua senha: ', stream=None)            
            login_valido = logar_usuario(usuario_login, senha_login)
            if login_valido:
                print("=-=-=-=-=-=-=-=-=-=-=-=-=-=")
                print("!!LOGIN BEM SUCEDIDO!!")
                execução_mestre(permissão_leitura,permissão_escrever,permissão_excluir)
            else:
                print("Usuário ou senha incorretos!")
                tentar_novamente = input("Deseja tentar novamente? (s/n): ")
                if tentar_novamente.lower() != 's':
                    break
            break
    else:
        print("Escolha inválida. Por favor, escolha uma opção válida.")