w = float("inf")

# -- Funções Auxiliares --


def transicao_esta_habilitada(marcacao, t, A_in):
    """Verifica se há fichas suficientes em todos os lugares para disparar a transição t."""
    for lugar in range(len(marcacao)):
        # Se o lugar já tem fichas infinitas (w), ele sempre ignora a validação
        if marcacao[lugar] == w:
            continue

        # Se o lugar tiver menos fichas do que a matriz de entrada (A_in) exige, a transição é bloqueada
        if marcacao[lugar] < A_in[lugar][t]:
            return False

    return True


def disparar(marcacao_atual, t, A_in, A_out):
    """Calcula a nova marcação após o disparo da transição t. Cálculo: x' = x - A_in[:, t] + A_out[:, t]"""

    # Criamos a lista que guardará a marcação resultante após o disparo
    nova_marcacao = []

    for lugar in range(len(marcacao_atual)):
        # w absorve qualquer alteração: infinito continua sendo infinito
        if marcacao_atual[lugar] == w:
            nova_marcacao.append(w)
        else:
            # O cálculo do próximo estado do lugar atual. Nova marcação = atual - consumo + produção
            fichas = marcacao_atual[lugar] - A_in[lugar][t] + A_out[lugar][t]
            nova_marcacao.append(fichas)

    return nova_marcacao


def expandir_marcacao(marcacao, A_in, A_out):
    """Dado x, retorna lista de (t, x') para cada transição habilitada."""
    resultado = []
    for t in range(len(A_in[0])):
        if transicao_esta_habilitada(marcacao, t, A_in):
            resultado.append((t, disparar(marcacao, t, A_in, A_out)))
    return resultado


def tem_ancestral_menor(marcacao_ancestral, marcacao_nova):
    """
    Retorna True se o ancestral for menor ou igual à marcação nova em todos os lugares,
    indicando que a rede manteve estabilidade ou cresceu.
    """
    for fichas_ancestral, fichas_nova in zip(marcacao_ancestral, marcacao_nova):
        # Se antes era infinito (w) e agora caiu para um número finito, não é menor/igual
        if fichas_ancestral == w and fichas_nova != w:
            return False

        # Se as fichas do ancestral forem maiores do que as da nova em qualquer lugar, não é menor/igual
        if (
            fichas_ancestral != w
            and fichas_nova != w
            and fichas_ancestral > fichas_nova
        ):
            return False

    # Se passou pelas checagens sem retornar False, o ancestral é realmente menor ou igual
    return True


def aplicar_w(no_novo, caminho_ancestral):
    """
    Sobe o histórico de pais do nó novo. Se encontrar um ancestral menor,
    substitui por 'w' os lugares onde o número de fichas aumentou.
    """
    resultado = list(no_novo)

    for ancestral in caminho_ancestral:
        # Se este ancestral do passado for menor ou igual ao estado atual
        if tem_ancestral_menor(ancestral, resultado):
            # Varre os lugares para achar onde houve o aumento de fichas
            for lugar in range(len(resultado)):
                # Se o valor atual for maior que o do ancestral, cravamos o infinito (w)
                if (
                    ancestral[lugar] != w
                    and resultado[lugar] != w
                    and ancestral[lugar] < resultado[lugar]
                ):
                    resultado[lugar] = w

    return resultado


# -- Árvore de Cobertura (BFS) --


def arvore_de_cobertura(x0, A_in, A_out):
    """Constrói a árvore de cobertura e retorna a lista de transições (x, t, x')."""
    # Guarda tuplas no formato: (marcação, índice_do_nó_pai)
    nos = [(tuple(x0), None)]
    visitados = {tuple(x0)}
    fila = [0]  # Guarda os índices dos nós que precisam ser explorados
    arestas = []

    while fila:
        idx_atual = fila.pop(0)
        marcacao_atual = list(nos[idx_atual][0])

        # Reconstrói a linha de pais direta do nó atual de volta até a raiz (usado na regra do w)
        caminho_ancestral = []
        ponteiro = idx_atual
        while ponteiro is not None:
            caminho_ancestral.append(nos[ponteiro][0])
            ponteiro = nos[ponteiro][1]

        # Varre os ramos habilitados a partir do estado atual
        for t, nova in expandir_marcacao(marcacao_atual, A_in, A_out):
            # Aplica a regra de cobertura comparando com o histórico de pais
            nova_com_w = aplicar_w(nova, caminho_ancestral)
            nova_tuple = tuple(nova_com_w)

            # Registra o disparo na lista de saída do seu trabalho: (origem, transição, destino)
            arestas.append((nos[idx_atual][0], t, nova_tuple))

            # Se for uma marcação inédita, adiciona na fila para expandir seus filhos depois
            if nova_tuple not in visitados:
                visitados.add(nova_tuple)
                novo_idx = len(nos)
                nos.append((nova_tuple, idx_atual))
                fila.append(novo_idx)

    return arestas


# -- Exibição --


def imprimir_arvore(lista_arestas):
    """Formata e imprime as transições da árvore."""

    def formatar_vetor(marcacao):
        # Substitui o valor matemático 'inf' pela letra 'w' na hora de mostrar na tela
        partes = ["w" if valor == w else str(valor) for valor in marcacao]
        return "(" + ", ".join(partes) + ")"

    print("\n-- Árvore de Cobertura Encontrada --")
    for origem, transicao, destino in lista_arestas:
        origem_formatada = formatar_vetor(origem)
        destino_formatada = formatar_vetor(destino)

        # t+1 ajusta o índice de programação (0, 1, 2) para o nome real da transição (t1, t2, t3)
        print(f"  {origem_formatada}  --t{transicao+1}-->  {destino_formatada}")
