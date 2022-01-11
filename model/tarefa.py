class Tarefa():
    def __init__(self,id,descricao,status):
        self.id = id
        self.descricao = descricao
        self.status = status

    def print(self):
        print(f'{self.id}- {self.descricao}-{self.status}')