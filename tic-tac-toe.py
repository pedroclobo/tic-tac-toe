# Pedro Cerqueira Lobo ---- 99115

def eh_tabuleiro(tab):
    """Verifica se o tabuleiro e valido.

    Um tabuleiro e valido se for um tuplo, contendo varios tuplos, cada um com
    exatamente 3 elementos podendo estes ser os inteiros -1, 0 ou 1.

    :param tab: Um tuplo, representa o tabuleiro.
    :return: Um valor logico.
    """
    count = 0

    if isinstance(tab, tuple):
        for tuplo in tab:
            if isinstance(tuplo, tuple):
                for elemento in tuplo:
                    if elemento in (-1, 0, 1) and type(elemento) == int:
                        count = count + 1

    return count == 9


def eh_tabuleiro_cheio(tab):
    """Verifica se o tabuleiro esta cheio.

    Um tabuleiro esta cheio se for um tabuleiro, de acordo com "eh_tabuleiro", e se os
    elementos dos tuplos nele contidos forem os inteiros correspondentes aos jogadores
    (-1 ou 1).

    :param tab: Um tuplo, representa o tabuleiro.
    :return: Um valor logico.
    """
    # Validacao do tabuleiro
    if not eh_tabuleiro(tab):
        raise ValueError("eh_tabuleiro_cheio: argumento invalido")

    count = 0

    for tuplo in tab:
        for elemento in tuplo:
            if elemento in (-1, 1) and type(elemento) == int:
                count = count + 1

    return count == 9


def eh_posicao(pos):
    """Verifica se e uma posicao valida do tabuleiro.

    Uma posicao e valida se corresponder a um inteiro de 1 a 9.

    :param pos: Um inteiro (de 1 a 9), posicao do tabuleiro.
    :return: Um valor logico.
    """
    return type(pos) == int and pos in (1, 2, 3, 4, 5, 6, 7, 8, 9)


def eh_jogador(jog):
    """Verifica se e um jogador valido.

    Um jogador e valido se corresponder ao inteiro -1 ou 1.

    :param jog: Um inteiro (-1 ou 1), corresponde ao jogador.
    :return: Um valor logico.
    """
    # type == int evita que sejam atribuidos valores logicos a jog
    return type(jog) == int and jog in (-1, 1)


def eh_estrategia(estra):
    """Verifica se e uma estrategia valida.

    Uma estrategia e valida se corresponder a uma das seguintes strings:
    "basico", "normal" ou "perfeito".

    :param estra: Uma cadeia de caracteres, corresponde ao nome da estrategia.
    :return: Um valor logico.
    """
    return estra in ("basico", "normal", "perfeito")


def obter_coluna(tab, col_ind):
    """Devolve a coluna com o indice "col_ind".

    Existem 3 colunas no tabuleiro, estando elas numeradas de 1 a 3, da esquerda para a direita.

    :param tab: Um tuplo, representa o tabuleiro.
    :param col_ind: Um inteiro (de 1 a 3), indice da coluna.
    :return: Um tuplo, representacao da coluna.
    """
    if not eh_tabuleiro(tab) or not (type(col_ind) == int and 1 <= col_ind <= 3):
        raise ValueError("obter_coluna: algum dos argumentos e invalido")

    col = ()

    for tuplo in tab:
        col += (tuplo[col_ind-1],)

    return col


def obter_linha(tab, lin_ind):
    """Devolve a linha com o indice "lin_ind".

    Existem 3 linhas no tabuleiro, estando elas numeradas de 1 a 3, de cima para baixo.

    :param tab: Um tuplo, representa o tabuleiro.
    :param lin_ind: Um inteiro (de 1 a 3), indice da linha.
    :return: Um tuplo, representacao da linha.
    """
    if not eh_tabuleiro(tab) or not (type(lin_ind) == int and 1 <= lin_ind <= 3):
        raise ValueError("obter_linha: algum dos argumentos e invalido")

    return tab[lin_ind-1]


def obter_diagonal(tab, diag_ind):
    """Devolve a diagonal com o indice "diag_ind"

    Existem 2 diagonais no tabuleiro, estando elas numeradas de 1 a 2.
    A primeira corresponde a descendente da esquerda para a direita,
    e a segunda a ascendente da esquerda para a direita.

    :param tab: Um tuplo, representa o tabuleiro.
    :param diag_ind: Um inteiro (de 1 a 2), indice da diagonal.
    :return: Um tuplo, representacao da diagonal.
    """
    if not eh_tabuleiro(tab) or not (type(diag_ind) == int and 1 <= diag_ind <= 2):
        raise ValueError("obter_diagonal: algum dos argumentos e invalido")

    diag = ()

    if diag_ind == 1:
        for i in range(3):
            diag += (tab[i][i],)
    else:
        for i in range(3):
            diag += (tab[2-i][i],)

    return diag


def tabuleiro_str(tab):
    """Devolve a representacao visual do tabuleiro.

    :param tab: Um tuplo, representa o tabuleiro.
    :return: Uma cadeia de caracteres, representacao visual do tabuleiro.
    """
    if not eh_tabuleiro(tab):
        raise ValueError("tabuleiro_str: o argumento e invalido")

    str = " "

    # Itera sobre as linhas associando cada elemento da linha ao simbolo correspondente
    for lin in range(1, 4):
        for ind in range(3):
            if obter_linha(tab, lin)[ind] == -1:
                simb = "O"
            elif obter_linha(tab, lin)[ind] == 1:
                simb = "X"
            else:
                simb = " "
            # Para os primeiros 2 indices, adiciona-se " | "
            if ind != 2:
                str += simb + " | "
            # Para o ultimo elemento da linha, " | " e desnecessario
            else:
                str += simb + " "

        # A ultima linha nao recebe "-----------" abaixo
        if lin != 3:
            str += "\n-----------\n" + " "

    return str


def eh_posicao_livre(tab, pos):
    """Verifica se a posicao dada esta livre no tabuleiro.

    :param tab: Um tuplo, representa o tabuleiro.
    :param pos: Um inteiro (de 1 a 9), e a posicao do tabuleiro.
    :return: Um valor logico.
    """
    if not eh_tabuleiro(tab) or not eh_posicao(pos):
        raise ValueError("eh_posicao_livre: algum dos argumentos e invalido")

    return tab[(pos-1)//3][pos % 3-1] == 0


def obter_posicao(tab, pos):
    """Devolve o valor da posicao no tabuleiro.

    :param tab: Um tuplo, representa o tabuleiro.
    :param pos: Um inteiro (de 1 a 9), posicao do tabuleiro.
    :return: Um inteiro, corresponde ao jogador que ocupa a posicao ou a posicao livre (0).
    """
    # (pos-1//3) = linha-1; pos%3-1 = coluna-1
    return tab[(pos-1)//3][pos % 3-1]


def obter_posicoes_livres(tab):
    """Devolve um tuplo com os valores das posicoes livres no tabuleiro.

    :param tab: Um tuplo, representa o tabuleiro.
    :return: Um tuplo, corresponde ao conjunto das posicoes livres no tabuleiro.
    """
    if not eh_tabuleiro(tab):
        raise ValueError("obter_posicoes_livres: o argumento e invalido")

    pos_liv = ()

    for num in range(1, 10):
        if eh_posicao_livre(tab, num):
            pos_liv += (num, )

    return pos_liv


def jogador_ganhador(tab):
    """Devolve o jogador que ganha o jogo.

    :param tab: Um tuplo, representa o tabuleiro.
    :return: Um inteiro (-1, 1), corresponde ao jogador que ganha o jogo,
    0 se nao existe ganhador.
    """

    if not eh_tabuleiro(tab):
        raise ValueError("jogador_ganhador: o argumento e invalido")

    for jog in (-1, 1):
        for lin in range(1, 4):
            # Se um jogador tiver pecas em tres posicoes em linha ou coluna
            if obter_linha(tab, lin) == (jog, jog, jog) \
                    or obter_coluna(tab, lin) == (jog, jog, jog):
                return jog
        for diagonal in range(1, 3):
            # Se um jogador tiver pecas em tres posicoes em diagonal
            if obter_diagonal(tab, diagonal) == (jog, jog, jog):
                return jog

    return 0


def marcar_posicao(tab, jog, pos):
    """Devolve um tabuleiro com a jogada do jogador na posicao indicada.

    :param tab: Um tuplo, representa o tabuleiro.
    :param jog: Um inteiro (-1 ou 1), corresponde ao jogador.
    :param pos: Um inteiro (de 1 a 9), posicao do tabuleiro.
    :return: Um tuplo, tabuleiro com a sua posicao marcada pelo jogador.
    """
    if not eh_tabuleiro(tab) or not eh_jogador(jog) or not eh_posicao(pos) or not eh_posicao_livre(tab, pos):
        raise ValueError(
            "marcar_posicao: algum dos argumentos e invalido")

    # (pos-1//3) = linha-1; pos%3-1 = coluna-1
    nr_lin, nr_col = (pos-1)//3, pos % 3 - 1
    tab_lista = []

    # Converte o tuplo a lista, para que se torne mutavel
    for linha in tab:
        tab_lista += [list(linha)]

    # Muda a posicao a marcar pelo jogador nessa lista
    tab_lista[nr_lin][nr_col] = jog
    tab_final = ()

    # Reconverte a lista para tuplo
    for lin in tab_lista:
        tab_final += (tuple(lin), )

    return tuple(tab_final)


def escolher_posicao_manual(tab):
    """Requesita ao jogador uma posicao para marcar.

    :param tab: Um tuplo, representa o tabuleiro.
    :return: Um inteiro (de 1 a 9), posicao do tabuleiro.
    """
    pos = round(eval(input("Turno do jogador. Escolha uma posicao livre: ")))

    if not eh_posicao(pos) or not eh_posicao_livre(tab, pos):
        raise ValueError(
            "escolher_posicao_manual: a posicao introduzida e invalida")

    return pos


def escolher_posicao_auto(tab, jog, estra):
    """Devolve a posicao a marcar, de acordo com a estrategia selecionada.

    :param tab: Um tuplo, representa o tabuleiro.
    :param jog: Um inteiro (-1 ou 1), corresponde ao jogador.
    :param estra: Uma cadeia de caracteres, corresponde ao nome da estrategia.
    :return: Um inteiro (de 1 a 9), posicao do tabuleiro.
    """
    if not (eh_tabuleiro(tab) and eh_jogador(jog) and eh_estrategia(estra)):
        raise ValueError(
            "escolher_posicao_auto: algum dos argumentos e invalido")

    def vitoria(tab, jog):
        """Devolve a posicao a marcar, face a acao "vitoria".

        Se o jogador tiver duas das suas pecas em linha e uma posicao livre
        entao deve marcar na posicao livre (ganhando o jogo);

        :param tab: Um tuplo, representa o tabuleiro.
        :param jog: Um inteiro (-1 ou 1), corresponde ao jogador.
        :return: Um inteiro (de 1 a 9), posicao do tabuleiro escolhida.
        """
        # Posicoes de cada linha
        # p.e.: a linha 1 contem as posicoes 1, 2 e 3
        l = {1: (1, 2, 3), 2: (4, 5, 6), 3: (7, 8, 9)}
        for lin in range(1, 4):
            # Se o jogador tiver duas pecas na linha "lin"
            if obter_linha(tab, lin).count(jog) == 2 and 0 in obter_linha(tab, lin):
                # Lista de posicoes livres nessa linha
                posics = [pos for pos in
                          obter_posicoes_livres(tab) if pos in l[lin]]
                # Se alguma posicao livre existir nas condicoes anteriores
                if len(posics) != 0:
                    return posics[0]

        # analogo, mas para colunas
        c = {1: (1, 4, 7), 2: (2, 5, 8), 3: (3, 6, 9)}
        for coluna in range(1, 4):
            if obter_coluna(tab, coluna).count(jog) == 2:
                posics = [pos for pos in
                          obter_posicoes_livres(tab) if pos in c[coluna]]
                if len(posics) != 0:
                    return posics[0]

        # analogo, mas para diagionais
        d = {1: (1, 9), 2: (3, 7)}
        for diagonal in range(1, 3):
            if obter_diagonal(tab, diagonal).count(jog) == 2:
                posics = [pos for pos in
                          obter_posicoes_livres(tab) if pos in d[diagonal]]
                if len(posics) != 0:
                    return posics[0]

    def bloqueio(tab, jog):
        """Devolve a posicao a bloquear face a acao "vitoria", por parte do adversario.

        Se o adversario tiver duas das suas pecas em linha e uma posicao livre
        entao deve marcar na posicao livre (para bloquear o adversario).

        :param tab: Um tuplo, representa o tabuleiro.
        :param jog: Um inteiro (-1 ou 1), corresponde ao jogador.
        :return: Um inteiro (de 1 a 9), posicao do tabuleiro escolhida.
        """
        # Bloquear a vitoria corresponde a saber a posicao de vitoria do adversario.
        return vitoria(tab, -jog)

    def bifurcacao(tab, jog):
        """Devolve a posicao a marcar face a acao "bifurcacao".

        Se o jogador tiver duas linhas/colunas/diagonais que se intersetam, onde cada
        uma contem uma das suas pecas
        e se a posicao de intersecao estiver livre,
        entao deve marcar na posicao de intersecao
        (criando duas formas de vencer na jogada seguinte).

        :param tab: Um tuplo, representa o tabuleiro.
        :param jog: Um inteiro (-1 ou 1), corresponde ao jogador.
        :return: Um inteiro (de 1 a 9), posicao do tabuleiro escolhida.
        """

        # Dicionario das bifurcacoes
        # p.e. Se as pecas estao nas posicoes 1 e 6:
        # as bifurcacoes encontram-se nas posicoes 3, 4 e 5.
        bif = {(1, 6): (3, 4, 5), (1, 8): (2, 5, 7), (1, 9): (3, 7),
               (2, 4): (1, 5), (2, 6): (3, 5), (2, 7): (1, 5, 8), (2, 9): (3, 5, 8),
               (3, 4): (1, 5, 6), (3, 7): (1, 9), (3, 8): (2, 5, 9),
               (4, 8): (5, 7), (4, 9): (5, 6, 7),
               (6, 7): (4, 5, 9), (6, 8): (5, 9)}

        for conj_pos in bif:
            # Se o mesmo jogador tem duas linha/colunas/diagonais que se intersetam
            if obter_posicao(tab, conj_pos[0]) == jog and obter_posicao(tab, conj_pos[1]) == jog:
                for pos_a_jogar in bif[conj_pos]:
                    # Verifica se as posicoes de bifurcacao correspondentes estao livres
                    if eh_posicao_livre(tab, pos_a_jogar):
                        return pos_a_jogar

    def bloqueio_de_bifurcacao(tab, jog):
        """Devolve a posicao a bloquear face a acao "bifurcacao", por parte do adversario.

        Se o adversario tiver apenas uma bifurcacao,
        entao o jogador deve bloquear a bifurcacao (escolher a posicao livre da intersecao)
        senao o jogador deve criar um dois em linha para forcar o oponente a defender,
        desde que a defesa nao resulte na criacao de uma bifurcacao para o oponente.

        :param tab: Um tuplo, representa o tabuleiro.
        :param jog: Um inteiro (-1 ou 1), corresponde ao jogador.
        :return: Um inteiro (de 1 a 9), posicao do tabuleiro escolhida.
        """
        def bifurcacao_num(tab, jog):
            """Devolve o numero de bifurcacoes para determinadas posicoes.

            :param tab: Um tuplo, representa o tabuleiro.
            :param jog: Um inteiro (-1 ou 1), corresponde ao jogador.
            :return: inteiro, corresponde ao numero de bifurcacoes disponiveis.
            """
            # Dicionario das bifurcacoes. Analogo a funcao "bifurcacao".
            bif = {(1, 6): (3, 4, 5), (1, 8): (2, 5, 7), (1, 9): (3, 7),
                   (2, 4): (1, 5), (2, 6): (3, 5), (2, 7): (1, 5, 8), (2, 9): (3, 5, 8),
                   (3, 4): (1, 5, 6), (3, 7): (1, 9), (3, 8): (2, 5, 9),
                   (4, 8): (5, 7), (4, 9): (5, 6, 7),
                   (6, 7): (4, 5, 9), (6, 8): (5, 9)}

            num_bif = 0

            # Analogo a funcao "bifurcacao"
            for conj_pos in bif:
                if obter_posicao(tab, conj_pos[0]) == jog and obter_posicao(tab, conj_pos[1]) == jog:
                    for pos_a_jogar in bif[conj_pos]:
                        if eh_posicao_livre(tab, pos_a_jogar):
                            num_bif += 1
            return num_bif

        # Conjunto das posicoes dispoiveis
        pos_conj = ()

        # Se tiver apenas uma bifurcacao, devolve a posicao de bloqueio
        if bifurcacao_num(tab, -jog) == 1:
            return bifurcacao(tab, -jog)

        # Se tiver mais de uma bifurcacao:
        elif bifurcacao_num(tab, -jog) > 1:

            # Para a primeira linha
            for pos in (1, 2, 3):
                # Se a posicao estiver livre e nao for uma bifurcacao adversaria
                # e a linha for apenas ocupada pelo jogador, faz o dois em linha
                if eh_posicao_livre(tab, pos) and sum(obter_linha(tab, 1)) == jog and pos != bifurcacao(tab, -jog):
                    pos_conj += (pos,)
            # Analogo para a segunda linha
            for pos in (4, 5, 6):
                if eh_posicao_livre(tab, pos) and sum(obter_linha(tab, 2)) == jog and pos != bifurcacao(tab, -jog):
                    pos_conj += (pos,)
            # Terceira linha
            for pos in (7, 8, 9):
                if eh_posicao_livre(tab, pos) and sum(obter_linha(tab, 3)) == jog and pos != bifurcacao(tab, -jog):
                    pos_conj += (pos,)

            # Analogo para colunas
            for pos in (1, 4, 7):
                if eh_posicao_livre(tab, pos) and sum(obter_coluna(tab, 1)) == jog and pos != bifurcacao(tab, -jog):
                    pos_conj += (pos,)
            for pos in (2, 5, 8):
                if eh_posicao_livre(tab, pos) and sum(obter_coluna(tab, 2)) == jog and pos != bifurcacao(tab, -jog):
                    pos_conj += (pos,)
            for pos in (3, 6, 9):
                if eh_posicao_livre(tab, pos) and sum(obter_coluna(tab, 3)) == jog and pos != bifurcacao(tab, -jog):
                    pos_conj += (pos,)

            # Analogo para diagonais
            for pos in (1, 5, 9):
                if eh_posicao_livre(tab, pos) and sum(obter_diagonal(tab, 1)) == jog and pos != bifurcacao(tab, -jog):
                    pos_conj += (pos,)
            for pos in (3, 5, 7):
                if eh_posicao_livre(tab, pos) and sum(obter_diagonal(tab, 2)) == jog and pos != bifurcacao(tab, -jog):
                    pos_conj += (pos,)

        # Devolve a menor posicao que satisfaz as condicoes
        if len(pos_conj) != 0:
            return min(pos_conj)

    def centro(tab):
        """Devolve a posicao central se esta estiver inocupada.

        Se a posicao central estiver livre, entao joga na posicao central.

        :param tab: Um tuplo, representa o tabuleiro.
        :return: Um inteiro (5), posicao central do tabuleiro.
        """
        if eh_posicao_livre(tab, 5):
            return 5

    def canto_oposto(tab, jog):
        """Devolve a posicao do canto oposto ao jogado pelo adversario,
        se este estiver inocupado.

        Se o adversario estiver num canto
        e se o canto diagonalmente oposto for uma posicao livre.
        entao joga nesse canto oposto.

        :param tab: Um tuplo, representa o tabuleiro.
        :return: Um inteiro (1,3,7 ou 9), posicao do canto do tabuleiro.
        """
        d = {1: 9, 3: 7, 7: 3, 9: 1}

        for pos in d:
            if obter_posicao(tab, pos) == -jog:
                if eh_posicao_livre(tab, d[pos]):
                    return d[pos]

    def canto_vazio(tab):
        """Devolve a menor posicao de um canto vazio, se este estiver inocupado.

        Se um canto for uma posicao livre, entao jogar nesse canto.

        :param tab: Um tuplo, representa o tabuleiro.
        :return: Um inteiro (1,3,7 ou 9), posicao do canto do tabuleiro.
        """
        for pos in (1, 3, 7, 9):
            if eh_posicao_livre(tab, pos):
                return pos

    def lateral_vazio(tab):
        """Devolve a menor posicao de uma lateral, se esta estiver inocupada.

        Se uma posicao lateral (que nem a o centro, nem um canto) for livre
        entao jogar nesse lateral.

        :param tab: Um tuplo, representa o tabuleiro.
        :return: Um inteiro (2,4,6 ou 8), posicao do canto do tabuleiro.
        """
        for pos in (2, 4, 6, 8):
            if eh_posicao_livre(tab, pos):
                return pos

    def basico(tab):
        """Corresponde a estrategia que segue as seguintes acoes, com prioridade
        da esquerda para a direita:
        centro, canto vazio, lateral vazio.

        :param tab: Um tuplo, representa o tabuleiro.
        :return: Um inteiro (de 1 a 9), posicao escolhida face a estrategia.
        """
        if centro(tab) != None:
            return centro(tab)
        elif canto_vazio(tab) != None:
            return canto_vazio(tab)
        else:
            return lateral_vazio(tab)

    def normal(tab, jog):
        """Corresponde a estrategia que segue as seguintes acoes, com prioridade
        da esquerda para a direita:
        vitoria, bloqueio, centro, canto oposto, canto vazio, lateral vazio.

        :param tab: Um tuplo, representa o tabuleiro.
        :return: Um inteiro (de 1 a 9), posicao escolhida face a estrategia.
        """
        if vitoria(tab, jog) != None:
            return vitoria(tab, jog)
        elif bloqueio(tab, jog) != None:
            return bloqueio(tab, jog)
        elif centro(tab) != None:
            return centro(tab)
        elif canto_oposto(tab, jog) != None:
            return canto_oposto(tab, jog)
        elif canto_vazio(tab) != None:
            return canto_vazio(tab)
        else:
            return lateral_vazio(tab)

    def perfeito(tab, jog):
        """Corresponde a estrategia que segue as seguintes acoes, com prioridade
        da esquerda para a direita:
        vitoria, bloqueio, bifurcacao, bloqueio de bifurcacao, centro, canto oposto, canto vazio, lateral vazio.

        :param tab: Um tuplo, representa o tabuleiro.
        :return: Um inteiro (de 1 a 9), posicao escolhida face a estrategia.
        """
        if vitoria(tab, jog) != None:
            return vitoria(tab, jog)
        elif bloqueio(tab, jog) != None:
            return bloqueio(tab, jog)
        elif bifurcacao(tab, jog) != None:
            return bifurcacao(tab, jog)
        elif bloqueio_de_bifurcacao(tab, jog) != None:
            return bloqueio_de_bifurcacao(tab, jog)
        elif centro(tab) != None:
            return centro(tab)
        elif canto_oposto(tab, jog) != None:
            return canto_oposto(tab, jog)
        elif canto_vazio(tab) != None:
            return canto_vazio(tab)
        else:
            return lateral_vazio(tab)

    # Resultado de escolher_posicao_auto face a estrategia escolhida
    if estra == "basico":
        return basico(tab)
    elif estra == "normal":
        return normal(tab, jog)
    else:
        return perfeito(tab, jog)


def jogo_do_galo(simb_jog, estra):
    """Permite jogar um jogo completo de Jogo do Galo contra o computador.

    O jogo comeca sempre com o jogador "X" a marcar uma posicao livre e termina
    quando um dos jogadores vence ou, se nao existem posicoes livres no tabuleiro.

    :param simb_jog: Uma cadeia de caracteres, representa o simbolo do jogador humano.
    :param estra: Uma cadeia de caracteres, corresponde a estrategia utilizada pelo computador.
    :return: Uma cadeia de caracteres, simula o Jogo do Galo.
    """

    def eh_jogo_terminado(tab):
        """Verifica se o jogo terminou, dado um tabuleiro.

        Um jogo esta terminado se existe um jogador ganhador
        ou se todas as posicoes do tabuleiro ja foram marcadas.

        : param tab: tuplo, representa o tabuleiro
        : return: valor logico
        """
        if not eh_tabuleiro(tab):
            raise ValueError("eh_jogo_terminado: tabuleiro invalido")
        return jogador_ganhador(tab) != 0 or eh_tabuleiro_cheio(tab)

    # Verificar argumentos
    if simb_jog not in ("X", "O") or not eh_estrategia(estra):
        raise ValueError("jogo do galo: algum dos argumentos e invalido")

    # Atribuir numero de jogador ao jogador humano
    if simb_jog == "X":
        jog = 1
    elif simb_jog == "O":
        jog = -1

    # Tabuleiro inicial
    tab = ((0, 0, 0), (0, 0, 0), (0, 0, 0))

    # Boas-vindas
    print("Bem-vindo ao JOGO DO GALO.")
    print("O jogador joga com '", simb_jog, "'.", sep="")

    # Jogo
    # Se o jogador humano jogar com "X", comeca a jogar primeiro
    if simb_jog == "X":
        while True:
            # Turno do jogador
            tab = marcar_posicao(tab, jog, escolher_posicao_manual(tab))
            print(tabuleiro_str(tab))

            if eh_jogo_terminado(tab):
                break

            # Turno do computator
            print("Turno do computador (", estra, "):", sep="")
            # Tabuleiro com posicao marcada pelo computador
            tab = marcar_posicao(
                tab, -jog, escolher_posicao_auto(tab, -jog, estra))
            print(tabuleiro_str(tab))

            if eh_jogo_terminado(tab):
                break

    # Se o jogador humano jogar com "O", o computador comeca a jogar primeiro
    else:
        while True:
            # Turno do computator
            print("Turno do computador (", estra, "):", sep="")
            tab = marcar_posicao(
                tab, -jog, escolher_posicao_auto(tab, -jog, estra))
            print(tabuleiro_str(tab))

            if eh_jogo_terminado(tab):
                break

            # Turno do jogador
            tab = marcar_posicao(tab, jog, escolher_posicao_manual(tab))
            print(tabuleiro_str(tab))

            if eh_jogo_terminado(tab):
                break

    # Concluir o jogo
    if jogador_ganhador(tab) == 1:
        return "X"
    elif jogador_ganhador(tab) == -1:
        return "O"
    else:
        return "EMPATE"
