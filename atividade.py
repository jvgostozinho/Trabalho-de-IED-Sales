pessoas = []

def adicionar_pessoa():
    nome = input("Nome: ")
    cidade = input("Cidade: ")
    tem_transporte = input("Você tem transporte? (s/n): ").lower()

    transporte = {}
    if tem_transporte == 's':
        transporte['modelo'] = input("Modelo do transporte: ")
        transporte['placa'] = input("Placa: ")
        transporte['cor'] = input("Cor: ")
    else:
        transporte = None

    pessoa = {
        'nome': nome,
        'cidade': cidade,
        'transporte': transporte
    }

    pessoas.append(pessoa)
    print("Pessoa adicionada com sucesso!\n")

def ver_pessoas():
    if not pessoas:
        print("Nenhuma pessoa cadastrada.\n")
        return

    print("\n--- Lista de Pessoas ---")
    for i, pessoa in enumerate(pessoas):
        print(f"{i + 1}. Nome: {pessoa['nome']}, Cidade: {pessoa['cidade']}")
        if pessoa['transporte']:
            print(f"   Transporte: Modelo: {pessoa['transporte']['modelo']}, "
                  f"Placa: {pessoa['transporte']['placa']}, "
                  f"Cor: {pessoa['transporte']['cor']}")
        else:
            print("   Transporte: Não possui")
    print()

def excluir_pessoa():
    ver_pessoas()
    if not pessoas:
        return
    try:
        indice = int(input("Digite o número da pessoa que deseja excluir: ")) - 1
        if 0 <= indice < len(pessoas):
            removida = pessoas.pop(indice)
            print(f"Pessoa '{removida['nome']}' removida com sucesso.\n")
        else:
            print("Número inválido.\n")
    except ValueError:
        print("Entrada inválida.\n")

def menu():
    while True:
        print("=== MENU ===")
        print("1. Adicionar pessoa")
        print("2. Ver pessoas")
        print("3. Excluir pessoa")
        print("4. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            adicionar_pessoa()
        elif escolha == '2':
            ver_pessoas()
        elif escolha == '3':
            excluir_pessoa()
        elif escolha == '4':
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

# Executar o menu principal
menu()