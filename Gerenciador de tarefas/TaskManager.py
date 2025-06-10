# --- Variáveis Globais ---
taskList = {} 
ID_counter = 1 

# --- Definição das Funções ---

def addTask(tasks_dict, task_id, task_description):
    tasks_dict[task_id] = task_description
    print(f"Tarefa '{task_description}' (ID: {task_id}) adicionada com sucesso!")

def removeTask(tasks_dict, task_id):
    try:
        removed_task = tasks_dict.pop(task_id)
        print(f"Tarefa '{removed_task}' (ID: {task_id}) removida com sucesso!")
    except KeyError:
               print(f"Erro: ID {task_id} não encontrado na lista de tarefas.")

def viewTasks(tasks_dict):
    print("\n--- SUAS TAREFAS ---")
    if not tasks_dict:
        print("Você não tem nenhuma tarefa.")
    else:
        for task_id, description in tasks_dict.items():
            print(f"ID: {task_id} - Tarefa: {description}")
    print("--------------------\n")

# --- Loop Principal do Programa ---

while True:
    # Menu
    print("Gerenciador de Tarefas\n")
    print("OPÇÕES:")
    print("1. Adicionar Tarefa")
    print("2. Remover Tarefa")
    print("3. Visualizar Tarefas")
    print("4. Sair")

    try:
        option = int(input("\nESCOLHA UMA OPÇÃO: "))

        if option == 1:
            task_text = input("Digite a tarefa a ser adicionada: ")
            addTask(taskList, ID_counter, task_text)
            ID_counter += 1

        elif option == 2:
            try:
                id_to_remove = int(input("Digite o ID da tarefa a ser removida: "))
                removeTask(taskList, id_to_remove)
            except ValueError:
                print("Erro: O ID deve ser um número.")
                
        elif option == 3:
            viewTasks(taskList)

        elif option == 4:
            print("Saindo do programa. Até mais!")
            break 

        else:
            print("Opção inválida! Por favor, escolha um número de 1 a 4.")

    except ValueError:
        print("Entrada inválida! Por favor, digite apenas o número da opção.")
