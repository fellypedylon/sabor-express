import os

restaurantes = [{'nome' : 'Praça', 'categoria' : 'Japonesa', 'ativo' :False},
                {'nome' : 'Pizza Suprema', 'categoria' : 'Pizza', 'ativo' :True},
                {'nome' : 'Cantina', 'categoria' : 'Italiano', 'ativo' :False}]


def exibir_nome_do_programa():
  print ("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░""")


def exibir_opcoes():
    print ('1. Cadastrar restaurante')
    print ('2. Listar restaurante')
    print ('3. Alternar estado do restaurante')
    print ('4. Sair\n')

def finalizar_app ():
    exibir_subtitulo('Finalizar o app')
def finalizar_app():
    exibir_subtitulo('Finalizando o app...')
    raise SystemExit # Levanta uma exceção para sair do loop principal


def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal ')
    main()

def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu_principal()
    input('Digite uma tecla para voltar ao menu principal ') # Não chama main() recursivamente

def exibir_subtitulo(texto):
    os.system('cls')
    # Limpa a tela do console (funciona em Windows, Linux e macOS)
    os.system('cls' if os.name == 'nt' else 'clear')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    '''Essa função é responsável por cadastrar um novo restaurante
    
    Inputs:
    - Nome do restaurante
    - Categoria

    Output:
    - Adiciona um novo restaurante à lista de restaurantes

    
    '''

    exibir_subtitulo('Cadastro de novos restaurantes\n')
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do Restaurante{nome_do_restaurante}: ')
    # TODO: verificar se o restaurante já existe
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listando restaurantes')
    
    
    
    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
    print(f'{"Nome do restaurante".ljust(22)} | {"Categoria".ljust(20)} | Status')
    for restaurante in restaurantes:
      nome_restaurante = restaurante ['nome']
      categoria = restaurante ['categoria']
      ativo = 'ativado' if restaurante ['ativo'] else 'desativado'
      print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
      
      print(f'- {nome_restaurante.ljust(22)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    exibir_subtitulo('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante ['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)

    if not restaurante_encontrado:
      print('O restaurante não foi encontrado')



    voltar_ao_menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input ('Escolha uma opção: '))
        # opcao_escolhida == int(opcao_escolhida)

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
            print ('Cadastrar restaurante')
        elif opcao_escolhida == 2:
            listar_restaurantes ()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app ()
        else:
            opcao_invalida  ()
    
            opcao_invalida()
    except ValueError: # Captura apenas erros de conversão para int
        opcao_invalida()

def main ():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()
def main():
    # Limpa a tela do console ao iniciar
    os.system('cls' if os.name == 'nt' else 'clear')
    # Loop principal do programa
    while True:
        try:
            exibir_nome_do_programa()
            exibir_opcoes()
            escolher_opcao()
        except SystemExit:
            break # Sai do loop quando SystemExit é levantado por finalizar_app()

if __name__ == '__main__':
    main ()