#Lista que armazena as tarefas
lista_tarefas = []

#Adiciona uma tarefa
def adicionar(nova_tarefa):
    lista_tarefas.append(nova_tarefa)

#Exclui uma tarefa
def excluir(tarefa_id):
    for index in range(0,lista_tarefas):
        pegar_tarefa = lista_tarefas[index]
        if tarefa_id == pegar_tarefa:
            del lista_tarefas[index]
            return

#Pega uma tarefa
def PegarTarefa(tarefa_id):
    for tarefa in lista_tarefas:
        if tarefa.id == tarefa_id:
            return tarefa

#Edita uma tarefa
def editar(tarefa):
    for index in range(0,len(lista_tarefas)):
        pegar_tarefa = lista_tarefas[index]
        if tarefa.id == pegar_tarefa.id:
            lista_tarefas[index] = tarefa

#Imprime todas as tarefas
def Imprime():
    for tarefa in lista_tarefas:
        tarefa.print()