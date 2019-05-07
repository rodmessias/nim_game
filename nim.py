def computador_escolhe_jogada(n, m):
    computador_remove_peca = 1
    while computador_remove_peca != m:
        if (n - computador_remove_peca) % (m + 1) == 0:
            return computador_remove_peca
        computador_remove_peca += 1
    return computador_remove_peca

def usuario_escolhe_jogada(n, m):
    usuario_jogada_valida = False
    while not usuario_jogada_valida:
        usuario_jogada = int(input('Quantas peças você vai tirar? '))
        if usuario_jogada > m or usuario_jogada < 1:
            print('\nOops! Jogada inválida! Tente de novo.\n')
        else:
            usuario_jogada_valida = True
    return usuario_jogada

def partida():
    n = int(input('\nQuantas peças? '))
    m = int(input('Limite de peças por jogada? '))
    computador_joga = False
    if n % (m + 1) == 0:
        print('\nVocê começa!\n')
    else:
        print('\nComputador começa!\n')
        computador_joga = True
    while n > 0:
        if computador_joga:
            computador_remove_peca = computador_escolhe_jogada(n, m)
            n -= computador_remove_peca
            if computador_remove_peca == 1:
                print('\nO computador tirou uma peça')
            else:
                print('O computador tirou', computador_remove_peca, 'peças')
            computador_joga = False
        else:
            usuario_remove_peca = usuario_escolhe_jogada(n, m)
            n -= usuario_remove_peca
            if usuario_remove_peca == 1:
                print('\nVocê tirou uma peça')
            else:
                print('\nVocê tirou', usuario_remove_peca, 'peças')
            computador_joga = True
        if n == 1:
            print('Agora resta apenas uma peça no tabuleiro.\n')
        else:
            if n != 0:
                print('Agora restam,', n, 'peças no tabuleiro.\n')
    print('Fim do jogo! O computador ganhou!')

def campeonato():
    rodada = 0
    while rodada < 3:
        print('\n**** Rodada', (rodada + 1), '****\n')
        partida()
        rodada += 1
    print('Placar: Você 0 X 3 Computador')
    
def inicio_partida():
    tipo_partida = int(input('Bem-vindo ao jogo do NIM! Escolha:\n\n1 - para jogar uma partida isolada\n2 - para jogar um campeonato\n'))
    while tipo_partida > 2 or tipo_partida < 1:
        tipo_partida = int(input('Por Favor escolha entre as opções:\n\n1 - para jogar uma partida isolada\n2 - para jogar um campeonato\n'))
    if tipo_partida == 1:
        partida()
    else:
        campeonato()
        
inicio_partida()
