from model.colaborador_dao import imprime

#Lista que guarda os projetos
lista_projetos = []

#Adiciona um novo Projeto
def adicionar(novo_projeto):
    lista_projetos.append(novo_projeto)

#Edita    
def editar(projeto):
    for index in range(0,len(lista_projetos)):
        pegar_projeto = lista_projetos[index]
        if projeto.id == pegar_projeto.id:
            lista_projetos[index] = projeto

#Pega
def pegarProjeto(projeto_id):
    for projeto in lista_projetos:
        if projeto.id == projeto_id:
            return projeto

#Exclui      
def excluir(projeto_id):
    for index in range(0,len(lista_projetos)):
        pegar_projeto = lista_projetos[index]
        if projeto_id == pegar_projeto.id:
            del lista_projetos[index]
            return

#Imprime
def listarProjetos():
    for projetos in lista_projetos:
        projetos.print()