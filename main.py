tarefas = []

def criar_item (tarefas, item):
    tarefas.append(item)
    print('O item foi adicionado!')

def remover_item (tarefas, item):
    if item in tarefas:
        tarefas.remove(item)
        print('O item foi removido!')
    else:
        print('Item não encontrado.')

def alterar_item (tarefas, item_nov, item_ant):
    for i in range(len(tarefas)):
        if tarefas[i] == item_ant:
            tarefas[i] = item_nov
            print('Item alterado')
            return tarefas
while True:

    lista_tarefas = []
    print('1-Criar tarefa;')
    print('2-Remover tarefa;')
    print('3-Substituir tarefa;')
    print('4-Exibir a lista;')
    print('5-Sair;')

    esc = input('Escolha uma opção:')

    if esc == '1':
        item = input ('Digite o item que quer adicionar: \n')
        criar_item(lista_tarefas, item)
    elif esc == '2':
        item = input ('Digite o item que quer remover: \n')
        remover_item(lista_tarefas, item)
    elif esc == '4':
        for i in range(len(tarefas)):
            print(tarefas[i])


