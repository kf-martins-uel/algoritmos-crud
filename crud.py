tarefas: list[dict] = [] 
"""
Lista de tarefas\n
Cada tarefa é um dict com chaves titulo, desc e custo.
O ID da tarefa será o seu indice na lista de tarefas.
"""

def adicionarTarefa(tarefa: dict):
    """Adiciona uma tarefa"""
    tarefas.append(tarefa)

#[i for i, val in enumerate(d) if all(val.get(k) == v for k, v in busca.items())]
def buscarTarefa(buscaParametros: dict) -> list[dict]:
    """Retorna uma lista com os ID correspondentes às tarefas que batem com os paramêtros da busca."""
    indices = [i for i, val in enumerate(tarefas) if all(val.get(k) == v for k, v in buscaParametros.items())]
    if indices:
        return indices
    return []

def buscarTarefaID(id: int) -> dict:
    """Retora um dict correspondente ao id da tarefa. Caso não exista, retora um dict vazio."""
    if id > len(tarefas):
        return {}
    return tarefas[id]

def listarTarefas() -> list[dict]:
    """Retorna a lista de tarefas."""
    return tarefas

def deletarTarefa(tarefa: dict):
    """Remove a primeira ocorrência da tarefa dentro da lista de tarefas. Não faz busca, será removido exatamente a tarefa dada."""
    tarefas.remove(tarefa)

def deletarTarefaID(tarefaID: int):
    """Remove o item da lista de tarefas. Isso faz com que todos os ID depois da tarefa seja diminuido em 1."""
    tarefas.pop(tarefaID)

def atualizarTarefa(tarefaID: int, novaTarefa: dict):
    """Atualiza a tarefa de acordo com o ID."""
    tarefas[tarefaID] = novaTarefa

