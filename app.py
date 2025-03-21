import os
restaurantes=[{"nome": "Safados Picantes", "categoria": "Apimentados", "ativo":False},
              {"nome": "Tempero Tarado", "categoria": "Salgado", "ativo":True}, 
              {"nome": "Cuzinh0 Doce", "categoria": "Doces", "ativo":False}
              ]

# Todos os Def, são onde está definindo cada variavel.

# Nome do programa.
def exibir_nome_do_programa():
    print(" 😏𝓢𝓪𝓯𝓪𝓭𝓲𝓷𝓱𝓸𝓼 𝓖𝓸𝓵𝓾𝓼𝓸𝓼😏" )

# Opções:
  
def exibir_opções():
    print("𝙊 𝙧𝙚𝙨𝙩𝙖𝙪𝙧𝙖𝙣𝙩𝙚 𝙢𝙖𝙞𝙨 𝙥𝙞𝙘𝙖𝙣𝙩𝙚 𝙙𝙚 𝙈𝙞𝙣𝙖𝙨❗\n")
    print("1 - Cadastro")
    print("2 - Lista Restaurante")
    print("3 - Ativar Restaurante")
    print("4 - Sair")

# Cada Def tem uma função:
  
def subtitulo(texto):
    os.system("cls")
    print(texto)
    print()
    
def menu_principal():
    input("\n Digite qualquer tecla para voltar ao menu principal.")
    main()
 
def cadastrar_novo_restaurante():
    os.system("cls")
    subtitulo("Cadastro de Novos Restaurantes Safadinhos😏")
    nome_do_restaurante = input("Digite o nome do Restaurante Safadinho que você deseja cadastrar.")
    restaurantes.append(nome_do_restaurante)
    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso!")
    menu_principal()
    main()
   
def listar_restaurante():
    os.system("cls")
    subtitulo("Listando os Restaurantes")
    
    for restaurante in restaurantes:
        nome_restaurantes = restaurante["nome"]
        print(f" - {nome_restaurantes}")                                         

    menu_principal()
    main()

 
def opcao_invalida():
    subtitulo('Opção Inválida!')
    menu_principal()

def encerrando_programa():
    os.system('cls')
    print('Encerrando o programa')
# Escolher Opções do programa.

def escolher_opcao():
    try:
        opcao_escolhida= int(input("Escolha alguma das opções acima."))
        print(f"Você escolheu a opção: {opcao_escolhida}")
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurante()
        elif opcao_escolhida == 3:
            print("Ativar Restaurantes")
        elif opcao_escolhida == 4:
            encerrando_programa()
        else:
            opcao_invalida()
    except:
            opcao_invalida()
       
def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opções()
    escolher_opcao()

if __name__ == '__main__':
    main()