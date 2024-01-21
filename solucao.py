from typing import Set, Tuple

class Nodo:
    """
    Implemente a classe Nodo com os atributos descritos na funcao init
    """
    def __init__(self, estado: str, pai: 'Nodo', acao: str, custo: int):
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
        self.filhos = []

    # função para adicionar filhos a um nodo
    def adicionar_filho(self, filho: 'Nodo'):
        self.filhos.append(filho)

    # eq para se a classe dos objetos é a mesma
    def __eq__(self, other):
        if isinstance(other, Nodo):
            return self.estado == other.estado
        return False

    # hash representação numérica do objeto
    def __hash__(self):
        return hash(self.estado)


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
        estado_lista = list(estado)#transf o estado stf em uma lista para ser muitooo mais fácil
        aux = estado_lista[novo_vazio] #guardo o elemento que vai trocar com o vazio
        estado_lista[novo_vazio] = '_' #bota o novo vazio no lugar certo
        estado_lista[vazio] = aux #troca como o elemento salvo
        novo_estado_retorno = ''.join(estado_lista) #converte para str
        sucessores.add((direcao, novo_estado_retorno))  # adiciona esse novo estado em sucessores

    return sucessores

    

def expande(nodo:Nodo)->Set[Nodo]:
    """
    Recebe um nodo (objeto da classe Nodo) e retorna um conjunto de nodos.
    Cada nodo do conjunto é contém um estado sucessor do nó recebido.
    :param nodo: objeto da classe Nodo
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError


def astar_hamming(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Hamming e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError


def astar_manhattan(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Manhattan e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError

#opcional,extra
def bfs(estado:str)->list[str]:
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

#opcional,extra
def dfs(estado:str)->list[str]:
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

#opcional,extra
def astar_new_heuristic(estado:str)->list[str]:
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
