from model.tabela_dao import lista_tarefas
lista_colaborador_tarefas = []

#Adiciona
def adicionar_colaboradores(tarefa_id,colaborador):
    for index in range(0,len(lista_tarefas)):
        pegar_tarefa = lista_tarefas[index]
        if tarefa_id == pegar_tarefa.id:
            lista_colaborador_tarefas.append(colaborador)

#Imprime       
def ListarColaboradoresTarefa(tarefa_id):
    for index in range(0,len(lista_tarefas)):
        pegar_tarefa = lista_tarefas[index]
        if tarefa_id == pegar_tarefa.id:
            for colaboradores in lista_colaborador_tarefas:
                colaboradores.print()