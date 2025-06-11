tarefas = []            # Lista principal de tarefas: armazena todas as tarefas atuais
historico = []          # Pilha para desfazer tarefas: guarda o histórico de tarefas adicionadas
fila_execucao = []      # Fila para executar tarefas na ordem de inserção

def adicionar_tarefa(tarefa):  # Função que adiciona uma nova tarefa
    tarefas.append(tarefa)     # Adiciona à lista principal
    historico.append(tarefa)   # Empilha no histórico (para desfazer)
    fila_execucao.append(tarefa)  # Enfileira para execução
    print(f"Tarefa '{tarefa}' adicionada!\n")  # Confirmação ao usuário

def desfazer_ultima_tarefa():  # Função que desfaz a última tarefa adicionada
    if historico:             # Verifica se há tarefas no histórico
        ultima = historico.pop()         # Desempilha a última tarefa
        tarefas.remove(ultima)           # Remove da lista principal
        fila_execucao.remove(ultima)     # Remove da fila de execução
        print(f"Tarefa '{ultima}' desfeita!\n")  # Confirmação ao usuário
    else:
        print("Nenhuma tarefa para desfazer.\n")  # Caso não haja histórico

def atender_tarefa():       # Função que atende a próxima tarefa na fila
    if fila_execucao:         # Verifica se a fila não está vazia
        feita = fila_execucao.pop(0)  # Desenfileira a próxima tarefa
        tarefas.remove(feita)         # Remove da lista principal
        print(f"Tarefa '{feita}' atendida!\n")  # Confirmação ao usuário
    else:
        print("Nenhuma tarefa para atender.\n")  # Caso a fila esteja vazia

def mostrar_tarefas():      # Função que exibe todas as tarefas atuais
    print("\n📋 Lista de Tarefas:")  # Cabeçalho da lista
    for i, t in enumerate(tarefas):  # Itera sobre as tarefas
        print(f"{i + 1}. {t}")      # Exibe índice e descrição
    print()  # Linha em branco para espaçamento

while True:  # Loop principal do programa
    print("1. Adicionar Tarefa")     # Opção de adicionar
    print("2. Desfazer Última Tarefa")  # Opção de desfazer
    print("3. Atender Tarefa (modo fila)")  # Opção de atender
    print("4. Mostrar Tarefas")      # Opção de mostrar
    print("5. Sair")                # Opção de sair

    opcao = input("Escolha uma opção: ")  # Lê a escolha do usuário

    if opcao == '1':                   # Se a opção for 1
        tarefa = input("Digite a tarefa: ")  # Pede descrição
        adicionar_tarefa(tarefa)      # Chama função para adicionar
    elif opcao == '2':                 # Se a opção for 2
        desfazer_ultima_tarefa()       # Chama função para desfazer
    elif opcao == '3':                 # Se a opção for 3
        atender_tarefa()              # Chama função para atender
    elif opcao == '4':                 # Se a opção for 4
        mostrar_tarefas()             # Chama função para mostrar
    elif opcao == '5':                 # Se a opção for 5
        print("Saindo do programa...")  # Mensagem de saída
        break                         # Encerra o loop
    else:
        print("Opção inválida!\n")  # Entrada inválida
