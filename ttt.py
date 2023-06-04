import sys
import os
import platform
import time



def divideCampoFileiras(campo) -> list:
    """
        O *desenho* do jogo da velha é separado em linhas, colunas e diagonais, para verificar se alguém ganhou.
        Facilitando sua vida...

        | [0][0] | [0][1] | [0][2] |
        | [1][0] | [1][1] | [1][2] |
        | [2][0] | [2][1] | [2][2] |
    """

    ln = campo[:]
    cl = [
        [campo[0][0], campo[1][0], campo[2][0]],
        [campo[0][1], campo[1][1], campo[2][1]],
        [campo[0][2], campo[1][2], campo[2][2]]
        ]
    diag = [
        [campo[0][0], campo[1][1], campo[2][2]],
        [campo[0][2], campo[1][1], campo[2][0]]
        ]

    return ln, cl, diag


def verificaAlguemVenceu(jogo_velha) -> bool:
    """
    Objetivo da função é verificar se 'xxx' ou 'ooo' ocorre na 'linhas', 'colunas', ou 'diagonal', se sim
    então alguém venceu o jogo, portanto, True para condição de saída.
    """
    sair = bool()
    linhas, colunas, diagonal = divideCampoFileiras(jogo_velha)
    dict_jogo_velha = {   
        "linhas" : ("".join(linhas[0]), "".join(linhas[1]), "".join(linhas[2])),
        "colunas" : ("".join(colunas[0]), "".join(colunas[1]), "".join(colunas[2])),
        "diagonal" : ("".join(diagonal[0]), "".join(diagonal[1]))
    }

    for chave in dict_jogo_velha.keys():       
        if ("XXX" in dict_jogo_velha[chave]) or ("OOO" in dict_jogo_velha):  
            print("~ Jogador 1 venceu!") if ("XXX" in dict_jogo_velha[chave]) else print("~ Jogador 2 venceu!")           
            sair = True
            break    
        
    return sair


def efetivaJogada(c, ln, col, simbolo):
    """
        campo(c) na linha 'ln', coluna 'col', recebe 'simbolo' ('X' ou 'O')
        Exemplo.:
        posicao: 5
        ln(linha) ~> | 4 | 5 | 6 |
        ln(linha) ~> | 4 | X/O | 6 |
    """
    c[ln][col] = simbolo

    return c 


def verificaJogada(campo, rodada, lance, simbolo):
    """
    A posição inserida pelo jogador não pode estar preenchida com um símbolo('X' / 'O').
    A procura por um valor correspondente ao lance por meio do método .index() pode gerar
    uma exceção do ValueError caso o valor procurado não exista(por já ter um 'X' ou 'O')...
    """

    try: 
        if (lance <= "3"):
            if (lance == campo[2][campo[2].index(lance)]):
                campo = efetivaJogada(campo, 2, campo[2].index(lance), simbolo)
            
        elif (lance <= "6"):
            if (lance == campo[1][campo[1].index(lance)]):
                campo = efetivaJogada(campo, 1, campo[1].index(lance), simbolo)

        elif (lance <= "9"):
            if (lance == campo[0][campo[0].index(lance)]):
                campo = efetivaJogada(campo, 0, campo[0].index(lance), simbolo)

    except ValueError:
        print("~ Posição {} já foi marcada.".format(lance))

    else:
        print("~ Posição {} foi marcada com sucesso!".format(lance))
        rodada += 1
    
    return campo, rodada


def validaEntrada(p) -> bool():
    return True if ((p.isdigit()) and (p in "123456789") and (len(p) == 1)) else False


def entrada(jogador, mensagem) -> str:
    while True:
        posicao = input("[*] Jogador {} | Símbolo {} {}".format(jogador[0], jogador[1], mensagem)).replace(" ", "")
        
        if validaEntrada(posicao):
            break
        else:
            print("~ Valor Inválido. Digite um número na faixa de 1 a 9.\n")

    return posicao


def verificaVezJogador(rodada) -> tuple:
    """
        A convenção que decidi usar aqui é que:
        -- Jogador 1 jogará nas rodadas ímpares(5 vezes)
        -- Jogador 2 jogará nas rodadas pares(4 vezes)
    """
    return (1, "X") if (rodada % 2 == 1) else (2, "O") 


def exibeJogoVelha(campo_velha, titulo="\n*** JOGO DA VELHA  X / O ***\n", char="-"):
    print(titulo)
    # ln - linha
    for ln in campo_velha:
            print(char * 13)
            print("| {0} | {1} | {2} |".format("".join(ln[0]), "".join(ln[1]), "".join(ln[2])))
    
    print(char * 13)

    return


def congelaPrograma(t=0.5):
    time.sleep(t)

    return


def limpaTela(so):
    if so == "Windows":
        os.system("cls")
    elif so == "Linux":
        os.system("clear")

    return


def verificaTipoSistema() -> str:
    """
        Função usada para evitar conflito posteriomente
        quando o for limpar o console/terminal do usuário.
    """
    return platform.system()


def exibeMensagemApresentacao():
    print('''\n
    -
    -
    Nome do programa: Jogo da velha
    Autor: Matias
    Data: 
    -   jogo_da_velha 1.0V: 05 / 06 / 22   
    -   jogo_da_velha 1.1V: 08 / 07 / 22
    -   
    -
    Atenção ao jogar:
    -
    Em um jogo da velha, cada "quadradinho" corresponde a um campo,
    que será identificado nesse programa por NÚMEROS, de 1 a 9.
    Portanto, se são 9 quadradinhos, teremos 9 rodadas. Cada usuário
    deverá jogar apenas UMA VEZ POR RODADA.
    -
    Se uma opção inválida for inserida incorretamente, a rodada não
    será contabilizada.
    -
    -
    Jogador 1: X
    Jogador 2: 0
    -
    Bom jogo!
    \n
    ''')

    return


def main():
    sistema_em_uso = verificaTipoSistema()   

    limpaTela(sistema_em_uso)
    exibeMensagemApresentacao()
    congelaPrograma(5)

    # criando os campos do jogo da velha
    jogo_da_velha = [list("789"), list("456"), list("123")]
    rodada = 1    
        
    while rodada <= 9:
        exibeJogoVelha(jogo_da_velha)
        print("\n<<< RODADA {} >>>\n".format(rodada))

        jogador = verificaVezJogador(rodada)
        posicao = entrada(jogador, "| Insira a posição do campo a marcar(de 1 a 9) ~> ")
        jogo_da_velha, rodada = verificaJogada(jogo_da_velha, rodada, posicao, jogador[1])

        congelaPrograma(1) 

        if verificaAlguemVenceu(jogo_da_velha):

            exibeJogoVelha(jogo_da_velha, "\n*** Final ***\n")
            congelaPrograma(5)
            sys.exit()
            
    exibeJogoVelha(jogo_da_velha, "\n*** Deu Velha! ***\n")

    return 


if __name__ == "__main__":
    main()

