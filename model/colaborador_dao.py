#Guarda todos os dados dos colaboradores
lista_colaboradores = []

#Adiciona um novo colaborador
def adicionar(novo_colaborador):

    #Insere o ID do colaborador
    novo_id = len(lista_colaboradores)+1
    novo_colaborador.id = novo_id

    #Insere o colaborador na lista.
    lista_colaboradores.append(novo_colaborador)


#Edita dados dos colaboradores
def pegar(id):
    for colaborador in lista_colaboradores:
        if colaborador.id == id:
            return colaborador

def editar(colaborador):
    for i in range(0,len(lista_colaboradores)):
        pegar_colaborador = lista_colaboradores[i]
        if colaborador.id == pegar_colaborador.id:
            lista_colaboradores[i]= colaborador

#Exclui um colaborador
def excluir(id_colaborador):
    for index in range(0,len(lista_colaboradores)):
        pegar_colaborador = lista_colaboradores[index]
        if id_colaborador == pegar_colaborador.id:
            del lista_colaboradores[index]

#Imprime todos os colaboradores
def imprime():
    for colaborador in lista_colaboradores:
        colaborador.print()