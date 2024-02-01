from typing import Set, Tuple
import heapq


class Nodo:
    """
    Implemente a classe Nodo com os atributos descritos na funcao init
    """

    def __init__(self, estado: str, pai: 'Nodo' or None, acao: str, custo: int):
        """
        Inicializa o nodo com os atributos recebidos
        :param estado: str, representacao do estado do 8-puzzle
        :param pai: Nodo, referencia ao nodo pai, (None no caso do nó raiz)
        :param acao: str, acao a partir do pai que leva a este nodo (None no caso do nó raiz)
        :param custo: int, custo do caminho da raiz até este nó
        """
        self.estado = estado
        self.pai = pai
        self.acao = acao
        self.custo = custo

    # eq para se a classe dos objetos é a mesma
    def __eq__(self, other):  # ==
        if isinstance(other, Nodo):
            return self.estado == other.estado
        return False

    def __lt__(self, other):  # <
        if isinstance(other, Nodo):
            return self.custo < other.custo
        return False

    def __le__(self, other):  # <=
        if isinstance(other, Nodo):
            return self.custo <= other.custo
        return False

    # hash representação numérica do objeto
    def __hash__(self):
        return hash(self.estado)

    # representação do objeto nodo em string para visualização
    def __repr__(self):
        return f"Nodo(Estado={self.estado}, Pai={self.pai}, Acao={self.acao}, Custo={self.custo})"


def testa_movimentos(estado: str) -> list[str]:
    # função que recebe uma string do jogo e devolve as direções possíveis do vazio atual
    vazio = estado.index('_')
    direcoes = ['acima', 'abaixo', 'esquerda', 'direita']

    if vazio >= 6 and vazio <= 8:
        direcoes.remove('abaixo')

    if vazio == 2 or vazio == 5 or vazio == 8:
        direcoes.remove('direita')

    if vazio == 0 or vazio == 3 or vazio == 6:
        direcoes.remove('esquerda')

    if vazio >= 0 and vazio <= 2:
        direcoes.remove('acima')

    return direcoes


def sucessor(estado: str) -> Set[Tuple[str, str]]:
    """
    Recebe um estado (string) e retorna um conjunto de tuplas (ação, estado atingido)
    para cada ação possível no estado recebido.
    Tanto a ação quanto o estado atingido são strings também.
    :param estado:
    :return:
    """
    # pegar a posição do vazio na string
    vazio = estado.index('_')
    dimensao = 3  # cada dimensão do tabuleiro tem 3 lugares
    # definindo os tipos de movimento
    movimentos = {
        'acima': -dimensao,  # trocar de posição com o 3 posições anteriores no string
        'abaixo': dimensao,  # troca de posição com o 3 posições a frente na string
        'esquerda': -1,  # troca de posição como 1 posição anterior no string
        'direita': 1  # troca de posição com o 1 posição a frente no string
    }

    direcoes = testa_movimentos(estado)  # temos a str com as direções possíveis do estado
    sucessores = set()  # criando o conjunto que vou retornar as tuplas

    for direcao in direcoes:  # para cada direção possível, generalizando os movimentos na string
        novo_vazio = vazio + movimentos[direcao]  # pos do novo _ é dele + a direção que estamos no for
        estado_lista = list(estado)  # transf o estado stf em uma lista para ser muitooo mais fácil
        aux = estado_lista[novo_vazio]  # guardo o elemento que vai trocar com o vazio
        estado_lista[novo_vazio] = '_'  # bota o novo vazio no lugar certo
        estado_lista[vazio] = aux  # troca como o elemento salvo
        novo_estado_retorno = ''.join(estado_lista)  # converte para str
        sucessores.add((direcao, novo_estado_retorno))  # adiciona esse novo estado em sucessores

    return sucessores


def expande(nodo: Nodo) -> Set[Nodo]:
    """
    Recebe um nodo (objeto da classe Nodo) e retorna um conjunto de nodos.
    Cada nodo do conjunto é contém um estado sucessor do nó recebido.
    :param nodo: objeto da classe Nodo
    :return:
    """
    if nodo is None:
        return set()
    lista_sucessores = sucessor(nodo.estado)
    nodos_sucessores = set()
    for acao, novo_estado in lista_sucessores:
        novo_nodo = Nodo(novo_estado, nodo, acao, nodo.custo + 1)
        nodos_sucessores.add(novo_nodo)

    return nodos_sucessores


def hamming_distance(estado):
    """
    retorna a heuristica de um determinado estado
    """
    hamming = 0
    objetivo = '12345678_'
    for i in range(len(estado)):
        if estado[i] != objetivo[i]:
            hamming += 1
    return hamming


def astar_hamming(estado: str ) -> list[str] or None:
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Hamming e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    """
    estado_final = '12345678_'
    nodo_raiz = Nodo(estado, None, None, 0)
    frontier = []
    explored = set()
    heapq.heappush(frontier, nodo_raiz)
    while frontier:
        current_node = heapq.heappop(frontier)
        if current_node.estado == estado_final:
            path = []
            while current_node.pai is not None:
                path.append(current_node.acao)
                current_node = current_node.pai
            return path[::-1]
        explored.add(current_node.estado)
        nodos_expandidos = expande(current_node)
        for nodo in nodos_expandidos:
            if nodo.estado not in explored:
                nodo.custo = current_node.custo + 1 + hamming_distance(nodo.estado)
                heapq.heappush(frontier, nodo)
    return None

def manhattan_distance(estado):
    """
    retorna a heuristica de um determinado estado
    """
    manhattan = 0
    objetivo = '12345678_'
    for i in range(len(estado)):
        if estado[i] != objetivo[i]:
            dx = abs(i % 3 - objetivo.index(estado[i]) % 3)
            dy = abs(i // 3 - objetivo.index(estado[i]) // 3)
            manhattan += dx + dy
    return manhattan

def astar_manhattan(estado: str) -> list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Manhattan e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    estado_final = '12345678_'
    nodo_raiz = Nodo(estado, None, None, 0)
    frontier = []
    explored = set()
    heapq.heappush(frontier, nodo_raiz)
    while frontier:
        current_node = heapq.heappop(frontier)
        if current_node.estado == estado_final:
            path = []
            while current_node.pai is not None:
                path.append(current_node.acao)
                current_node = current_node.pai
            return path[::-1]
        explored.add(current_node.estado)
        nodos_expandidos = expande(current_node)
        for nodo in nodos_expandidos:
            if nodo.estado not in explored:
                nodo.custo = current_node.custo + 1 + manhattan_distance(nodo.estado)
                heapq.heappush(frontier, nodo)
    return None


# opcional,extra
def bfs(estado: str) -> list[str]:
    """
    Recebe um estado (string), executa a busca em LARGURA e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError


# opcional,extra
def dfs(estado: str) -> list[str]:
    """
    Recebe um estado (string), executa a busca em PROFUNDIDADE e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError


# opcional,extra
def astar_new_heuristic(estado: str) -> list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = sua nova heurística e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError
