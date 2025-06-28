def adicionar_tarefa(tarefas, descricao):
    """Adiciona uma nova tarefa à lista com prioridade."""
    if descricao != "":
        print("Escolha a prioridade da tarefa:")
        print("1. Alta")
        print("2. Média")
        print("3. Baixa")
        prioridade = input("Digite o número da prioridade: ")

    if prioridade == "1":
            prioridade_texto = "Alta"
        elif prioridade == "2":
            prioridade_texto = "Média"
        elif prioridade == "3":
            prioridade_texto = "Baixa"
        else:
            prioridade_texto = "Baixa"

        nova_tarefa = {
            "descricao": descricao,
            "concluida": False,
            "prioridade": prioridade_texto
        }
        tarefas.append(nova_tarefa)
        print(f"\n✅ Tarefa '{descricao}' adicionada com prioridade '{prioridade_texto}'!")
    else:
        print("\n❌ A descrição da tarefa não pode ser vazia.")

def listar_tarefas(tarefas):
    """Lista todas as tarefas com status e prioridade."""
    print("\n--- Sua Lista de Tarefas ---")
    if len(tarefas) == 0:
        print("Nenhuma tarefa na lista. Adicione uma!")
    else:
        for i in range(len(tarefas)):
            if tarefas[i]["concluida"]:
                status = "✅"
            else:
                status = "◻️"
            print(f"{i + 1}. {status} [{tarefas[i]['prioridade']}] {tarefas[i]['descricao']}")
    print("--------------------------")

def marcar_como_concluida(tarefas, indice):
    """Marca uma tarefa como concluída com base no índice."""
    indice_real = indice - 1
    if indice_real >= 0 and indice_real < len(tarefas):
        if tarefas[indice_real]["concluida"]:
            print(f"\n⚠️ A tarefa '{tarefas[indice_real]['descricao']}' já está concluída.")
        else:
            tarefas[indice_real]["concluida"] = True
            print(f"\n✅ Tarefa '{tarefas[indice_real]['descricao']}' marcada como concluída!")
    else:
        print("\n❌ Índice inválido.")


def exibir_menu():
    """Exibe o menu de opções para o usuário."""
    print("\n--- MENU ---")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Marcar Tarefa como Concluída")
    print("4. Remover Tarefa")
    print("0. Sair")

def main():
    """Função principal que executa o loop do programa."""
    # A lista de tarefas (nosso vetor) é criada vazia aqui.
    # Ela existirá apenas enquanto o programa estiver em execução.
    lista_de_tarefas = []

    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            descricao = input("Digite a descrição da nova tarefa: ")
            adicionar_tarefa(lista_de_tarefas, descricao)
        elif escolha == '2':
            listar_tarefas(lista_de_tarefas)
        elif escolha == '3':
            listar_tarefas(lista_de_tarefas)
            try:
                indice = int(input("Digite o número da tarefa para marcar como concluída: "))
                marcar_como_concluida(lista_de_tarefas, indice)
            except ValueError:
                print("\n❌ Entrada inválida. Por favor, digite um número.")
        elif escolha == '4':
            listar_tarefas(lista_de_tarefas)
            try:
                indice = int(input("Digite o número da tarefa para remover: "))
                remover_tarefa(lista_de_tarefas, indice)
            except ValueError:
                print("\n❌ Entrada inválida. Por favor, digite um número.")
        elif escolha == '0':
            print("\nObrigado por usar o Gerenciador de Tarefas. Até mais!")
            break
        else:
            print("\n❌ Opção inválida. Por favor, tente novamente.")

# Garante que a função main() só será executada quando o script for rodado diretamente
if __name__ == "__main__":
    main()