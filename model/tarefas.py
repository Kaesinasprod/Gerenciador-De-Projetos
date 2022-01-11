class ColaboradoresTarefa():
    def __init__(self,projeto_id,colaborador_id,colaborador):
        self.projeto_id = projeto_id
        self.colaborador_id = colaborador_id
        self.colaborador = colaborador


    def print(self):
        print(f'{self.projeto_id}-{self.colaborador_id}-{self.colaborador}')