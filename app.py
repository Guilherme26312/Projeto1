import os
restaurantes=[{"nome": "Picantes", "categoria": "Apimentados", "ativo":False},
              {"nome": "Delicias Salgadas", "categoria": "Salgado", "ativo":True}, 
              {"nome": "Delicias Doces", "categoria": "Doces", "ativo":False}
              ]

# Todos os Def, são onde está definindo cada variavel.

# Nome do programa.
def exibir_nome_do_programa():
    """Essa função exibe o nome do Programa."""
    print("𝓒𝓸𝓶𝓲𝓭𝓮𝔁" )

# Opções:
def exibir_opções():
    """Essa função  exibir as opção para o usuário."""
    print("A Melhor Rede de Restaurantes de toda Minas Gerais\n")
    print("1 - Cadastro")
    print("2 - Lista Restaurante")
    print("3 - Alternar estado do Restaurante")
    print("4 - Sair")

# Cada  Def tem uma função:  
def subtitulo(texto):
    """Essa função é responsável por exibir os subtítulos."""
    os.system("cls")
    linha = "-" * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()    
    
def menu_principal():
    """Essa função é responsável por voltar para o menu principal"""
    input("\n Digite qualquer tecla para voltar ao menu principal.")
    main()
 
def cadastrar_novo_restaurante():
    """Essa função é responsável por Cadastrar um novo Restaurante."""
    os.system("cls")
    subtitulo("Cadastro de Novos Restaurantes")
    nome_do_restaurante = input("Digite o nome do Restaurante que você deseja cadastrar.")
    categoria = input(f"Digite o nome da categoria do restaurante {nome_do_restaurante}: ")
    dados_do_restaurante ={"nome": nome_do_restaurante, "categoria": categoria, "ativo": False}
    restaurantes.append(dados_do_restaurante)
    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso!")
    menu_principal()
    main()
   
def listar_restaurante():
    """Essa função é responsável por exibir os restaurantes cadastrados para o usuário."""
    os.system("cls")
    subtitulo("Listando os Restaurantes")
    
    for restaurante in restaurantes:
        nome_restaurantes = restaurante["nome"]
        categoria = restaurante["categoria"]
        ativo = "ativo" if restaurante["ativo"] else "desativo"
        print(f" - {nome_restaurantes.ljust(20)} | {categoria.ljust(20)} | {ativo}")                                         
        
    menu_principal()
    main()

def alternar_estado_restaurante():
    """Essa função é responsável por Alternar o Estado do Restaurante."""
    subtitulo("Alterando Estado do Restaurante")
    nome_do_restaurante = input("Digite o nome do restaurante que deseja alterar o estado.")
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if nome_do_restaurante == restaurante["nome"]:
            restaurante_encontrado = True
            restaurante["ativo"] = not restaurante["ativo"]
            mensagem = f"O restaurante {nome_do_restaurante} foi ativado com sucesso"  if restaurante["ativo"] else f"O restaurante {nome_do_restaurante} foi desativo com sucesso"
            print(mensagem)
            
            if not restaurante_encontrado:
                print("O restaurante não foi encontrado.")
                
    menu_principal()        
 
def opcao_invalida():
    """Essa função é responsável por alertar o usuário que a opção é inválida."""
    subtitulo('Opção Inválida!')
    menu_principal()

def encerrando_programa():
    """Essa função é responsável por encerrar o programa."""
    os.system('cls')
    print('Encerrando o programa')\
# Escolher Opções do programa.

def escolher_opcao():
    """ESsa função é responsável pela seleção do usuário."""
    try:
        opcao_escolhida= int(input("Escolha alguma das opções acima."))
        print(f"Você escolheu a opção: {opcao_escolhida}")
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurante()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            encerrando_programa()
        else:
            opcao_invalida()
    except:
            opcao_invalida()
       
def main():
    """Essa função é responsável por iniciar o programa."""
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opções()
    escolher_opcao()

if __name__ == '__main__':
    main()