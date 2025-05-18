import crud

tarefaExemplo = {
    'titulo':'Comprar arroz',
    'desc': 'Ir no mercado tal e comprar arroz tal',
    'custo': -20.00
}

def adcionarTarefa():
    print("==== CRIANDO TAREFA ====\n")
    titulo = input('Digite o título: ')
    desc = input('Digite a descrição: ')
    custo = input('Digite o custo (postivo para ganhos e negativo para perdas): ')
    crud.adicionarTarefa({'titulo': titulo, 'desc': desc, 'custo': float(custo) if custo.isnumeric() else custo})

def listarTarefas():
    print('==== TODAS TAREFAS ====')
    for i, tarefa in enumerate(crud.tarefas):
        print(f"ID {i}: {tarefa['titulo']}\nDescrição: {tarefa['desc']}\nCusto: {tarefa['custo']}\n")
    print()

def buscarTarefa():
    print('==== BUSCAR TAREFA ====')
    print('Digite pelo menos um parâmentro de busca.')
    
    idtarefa = input('Digite o id da tarefa: ')
    if idtarefa and idtarefa.isnumeric():
        tarefa = crud.buscarTarefaID(int(idtarefa))
        if tarefa:
            print(f"\nID {idtarefa}: {tarefa['titulo']}\nDescrição: {tarefa['desc']}\nCusto: {tarefa['custo']}")
        else:
            print("Tarefa não encontrada. ")
        return

    busca = {}
    titulo = input('Digite o título: ')
    if titulo:
         busca['titulo'] = titulo
    desc = input('Digite a descrição: ')
    if desc:
         busca['desc'] = desc
    custo = input('Digite o custo: ')
    if custo:
         busca['custo'] = custo
    print('\nParamêtros de busca: ', busca)

    print('\nTarefas encontradas: ')
    tarefas = crud.buscarTarefa(busca)
    for i in tarefas:
        print(f"ID {i}: {crud.tarefas[i]['titulo']}    Custo: {crud.tarefas[i]['custo']: >8.2f}")

def atualizarTarefa():
    print('==== ATUALIZANDO TAREFA ====')
    
    idtarefa = int(input('Digite o ID da tarefa: '))
    ntarefa = crud.buscarTarefaID(idtarefa) 

    print(f'-- Tarefa --')
    print(f'\nID: {idtarefa}\nTítulo: {ntarefa["titulo"]}\nDescição: {ntarefa["desc"]}\nCusto: {ntarefa["custo"]}')
    print("\nDeixe em branco para continuar o mesmo valor.\n")

    titulo = input('Digite o novo título: ')
    if titulo:
         ntarefa['titulo'] = titulo
    desc = input('Digite a nova descrição: ')
    if desc:
         ntarefa['desc'] = desc
    custo = input('Digite o novo custo: ')
    if custo:
         ntarefa['custo'] = custo
    crud.atualizarTarefa(idtarefa, ntarefa)

def deletarTarefa():
    print('==== DELETAR TAREFA ====')
    print('\nAtenção! Remover uma tarefa faz com que os ID das tarefas alterem.\n')
    idtarefa = input('Digite o id da tarefa: ')
    if idtarefa and idtarefa.isnumeric():
        tarefa = crud.buscarTarefaID(int(idtarefa))
        if tarefa:
            print(f"\nID {idtarefa}: {tarefa['titulo']}\nDescrição: {tarefa['desc']}\nCusto: {tarefa['custo']}")
            c = input("Tem certeza de que deseja deletar a tarefa? [S]/[N]").lower()
            if c == 's':
                 crud.deletarTarefaID(idtarefa)

def imprimirMenu():
    print("==== GERENCIADOR DE TAREFAS COM CUSTO ====")
    print("1. Criar tarefa")
    print("2. Listar tarefas")
    print("3. Buscar tarefa")
    print("4. Atualizar tarefa")
    print("5. Deletar tarefa")
    print("\n0. Sair")

if __name__ == "__main__":
    # crud.adicionarTarefa(tarefaExemplo)
    while True:
          imprimirMenu()
          op = input('> ')
          match op:
                case '1':
                      adcionarTarefa()
                case '2':
                      listarTarefas()
                case '3':
                      buscarTarefa()
                case '4':
                      atualizarTarefa()
                case '5':
                      deletarTarefa()
                case '0':
                      break
                case _: 
                      print('Faça uma escolha')
    print('Finalizado')