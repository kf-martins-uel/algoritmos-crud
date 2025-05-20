# Fluxogramas do programa

---

## Fluxograma das funções do CRUD

### adicionarTarefa(tarefa: dict)

```mermaid
flowchart TD
    A[Início] --> B["Recebe tarefa (dict)"]
    B --> C[Adiciona tarefa à lista tarefas]
    C --> D[Fim]
```

### buscarTarefa(buscaParametros: dict)

```mermaid
flowchart TD
    A[Início] --> B["Recebe buscaParametros (dict)"]
    B --> C[Busca tarefas que correspondem aos parâmetros]
    C --> D{Encontrou tarefas?}
    D -- Sim --> E[Retorna lista de IDs]
    D -- Não --> F[Retorna lista vazia]
```

### buscarTarefaID(id: int)

```mermaid
flowchart TD
    A[Início] --> B[Recebe id]
    B --> C{id é válido?}
    C -- Não --> D[Retorna dict vazio]
    C -- Sim --> E[Retorna tarefa correspondente]
```

### listarTarefas()

```mermaid
flowchart TD
    A[Início] --> B[Retorna lista de tarefas]
```

### deletarTarefaID(tarefaID: int)

```mermaid
flowchart TD
    A[Início] --> B[Recebe tarefaID]
    B --> C[Remove tarefa da lista pelo índice]
    C --> D[Fim]
```

### atualizarTarefa(tarefaID: int, novaTarefa: dict)

```mermaid
flowchart TD
    A[Início] --> B[Recebe tarefaID e novaTarefa]
    B --> C[Atualiza tarefa na lista pelo índice]
    C --> D[Fim]
```
