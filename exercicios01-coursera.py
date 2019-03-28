
# coding: utf-8

# In[1]:


ladoquadrado = input("Digite o valor correspondente ao lado de um quadrado:")

perimetro = 4 * int(ladoquadrado)
area = int(ladoquadrado) ** 2

print("perímetro: {0} - área: {1}".format(perimetro, area))


# In[2]:


n1 = int(input("Digite a primeira nota:"))
n2 = int(input("Digite a segunda nota:"))
n3 = int(input("Digite a terceira nota:"))
n4 = int(input("Digite a quarta nota:"))

media = ((n1 + n2 + n3 + n4) / 4)

print("A média aritmética é {0}".format(media))


# In[3]:


num = int(input("Digite um numero:"))

if (num%2 == 0):
    print("Número par!!")
else:
    print("Número impar!!")


# In[5]:


def fizz(n):
    if(n%3 == 0):
        return True
    else:
        return False
    
n = int(input("Informe o numero:"))

if(fizz(n)):
    print("Fizz")
else:
    print(n)


# In[ ]:


def buzz(x):
    if(x%5 == 0):
        return True
    else:
        return False
    
x = int(input("Informe o numero:"))

if (buzz(x)):
    print("Buzz")
else:
    print(x)


# In[ ]:


def FizzBuzz(y):
    if(y%3 == 0 & y%5 == 0):
        return True
    else:
        return False
    
y = int(input("Informe o numero:"))

if(FizzBuzz(y)):
    print("FizzBuzz")
else:
    print(y)


# In[ ]:


n1 = int(input("Insira o primeiro numero:"))
n2 = int(input("Insira o segundo numero:"))
n3 = int(input("Insira o terceiro numero:"))

if(n1 <= n2 & n2 <= n3):
    print("Crescente")
else:
    print("Não está em ordem crescente")


# In[ ]:


n = int(input("Digite o valor de n: "))
fatorial = 1
 
while n > 0:
    fatorial = fatorial * n
    n -= 1
 
print(fatorial)


# In[ ]:


n = int(input("Digite o valor de n: "))

for i in range(1, n+n, 2):
   print(i)


# In[ ]:


n = input("Digite um número inteiro: ")

print(sum(int(i) for i in n))


# In[ ]:


def maximo(x, y):
    if x > y:
        return x
    else:
        return y


# In[ ]:


def maior_primo(n):
    for num in reversed(range(1, n+1)):
        if all(num % i != 0 for i in range(2,num)):
            return num


# In[10]:


tipo_jogo = 0


def computador_escolhe_jogada(n, m):   
    # Pode retirar todas as peças?
    if n <= m:
        # Retira todas as peças e ganha o jogo:
        return n
    else:
        # Verifica se é possível deixar uma quantia múltipla de m+1:
        quantia = n % (m+1)
        if quantia > 0:
            return quantia
        # Não é, então tire m peças:
        return m


def usuario_escolhe_jogada(n, m):
    # Define o número de peças do usuário:
    jogada = 0
    # Enquanto o número não for válido
    while jogada == 0:
        # Solicita ao usuário quantas peças irá tirar:
        jogada = int(input("Quantas peças irá tirar? "))
        # Condições: jogada < n, jogada < m, jogada > 0
        if jogada > n or jogada < 1 or jogada > m:
            # Valor inválido, continue solicitando ao usuário:
            print("\nOops! Jogada inválida! Tente de novo.\n")
            jogada = 0
    # Número de peças válido, então retorne-o:
    return jogada


def partida_loop():    
    print(" ")
    # Solicita ao usuário os valores de n e m:
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    # Define uma variável para controlar a vez do computador:
    is_computer_turn = True
    # Decide quem iniciará o jogo:
    if n % (m+1) == 0:
        is_computer_turn = False
        print("\nVoce começa!\n")
    else:
        print("\nComputador começa!\n")
    # Execute enquanto houver peças no jogo:
    while n > 0:
        if is_computer_turn:
            jogada = computador_escolhe_jogada(n, m)
            is_computer_turn = False
            print("Computador retirou {} peça(s).".format(jogada))
        else:
            jogada = usuario_escolhe_jogada(n, m)
            is_computer_turn = True
            print("Você retirou {} peça(s).".format(jogada))   
        # Retira as peças do jogo:
        n = n - jogada
        # Mostra o estado atual do jogo:
        print("Agora resta(m) {} peça(s) em jogo.\n".format(n))
    # Fim de jogo, verifica quem ganhou:
    if is_computer_turn:
        print("Você ganhou!")
        return 1
    else:
        print("Fim do jogo! O computador ganhou!")
        return 0


def campeonato():
    # Pontuações:
    usuario = 0
    computador = 0
    # Executa 3 vezes:
    for _ in range(3):
        print()
        print("**** Rodada {} ****".format(_+1))

        # Executa a partida:
        vencedor = partida_loop()
        # Verifica o resultado, somando a pontuação:
        if vencedor == 1:
            # Usuário venceu:
            usuario = usuario + 1
        else:
            # Computador venceu:
            computador = computador + 1  
    # Exibe o placar final:
    print("Placar final: Você  {} x {}  Computador".format(usuario, computador))


def partida():
    # Menu de opções:
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print(" ")
    print("1 - Para jogar uma partida isolada")
    # Solicita a opção ao usuário:
    tipo_jogo = int(input("2 - Para jogar um campeonato "))
    print(" ")

    # Decide o tipo de jogo:
    if tipo_jogo == 1:
        print("Voce escolheu partida isolada!")
        partida_loop()
    if tipo_jogo == 2:
        print("Voce escolheu um campeonato!")
        campeonato()
    else:
        print("Numero inválido, escolha uma opção de partida")


partida()


# In[11]:


largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))
while altura > 0:
    print("#" * largura)
    altura -= 1


# In[12]:


largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))
    
linha = 1

while linha <= altura:
    print("#", end="")
    coluna = 2
    while coluna < largura: 
        if linha == 1 or linha == altura:
            print("#", end="")
        else:
            print(end=" ")
        coluna += 1
    print("#")
    linha += 1


# In[15]:


def remove_repetidos(lista):
    n_lista = []
    for i in lista:
        if i not in n_lista:
            n_lista.append(i)
    n_lista.sort()
    return n_lista


lista_antiga = [1, 1, 2, 1, 3, 4, 3, 6, 7, 6, 7, 8, 10, 9]

lista_nova = remove_repetidos(lista_antiga)
print(lista_nova)


# In[18]:


def soma_elementos(lista):
    soma = 0
    for i in lista:
        soma += i
    return soma


lista_int = [1, 2, 3]
print(soma_elementos(lista_int))


# In[20]:


import re


def le_assinatura():
    """
    Função que lê os valores dos traços linguísticos do modelo e devolve uma assinatura
    a ser comparada com os textos fornecidos.
    """
    print("Bem-vindo ao detector automático de COH-PIAH.\n\n")

    wal = float(input("Entre o tamanho medio de palavra: "))
    ttr = float(input("Entre a relação Type-Token: "))
    hlr = float(input("Entre a Razão Hapax Legomana: "))
    sal = float(input("Entre o tamanho médio de sentença: "))
    sac = float(input("Entre a complexidade média da sentença: "))
    pal = float(input("Entre o tamanho medio de frase: "))
    
    return [wal, ttr, hlr, sal, sac, pal]  # retorno a lista das assinaturas


def le_textos():
    """
    Função que carrega uma lista com os textos digitados até o não informar mais o texto
    apertando ENTER com texto em branco.
    """
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) + " (aperte enter para sair): ")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) + " (aperte enter para sair): ")

    return textos  # retorno a lista de textos


def separa_sentencas(texto):
    """Função que recebe um texto e devolve uma lista das sentenças dentro do texto."""
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
        
    return sentencas  # retorna senteças


def separa_frases(sentenca):
    """Função que recebe uma sentença e devolve uma lista das frases dentro da sentença."""
    return re.split(r'[,:;]+', sentenca)


def separa_palavras(frase):
    """Função que recebe uma frase e devolve uma lista das palavras dentro da frase."""
    return frase.split()


def n_palavras_unicas(lista_palavras):
    """Função que recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez."""
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas


def n_palavras_diferentes(lista_palavras):
    """Função que recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas."""
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)


def compara_assinatura(as_a, as_b):
    """Função que recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas."""
    grau_similaridade = 0
    
    for i in range(0,6):
        valor = as_a[i] - as_b[i]
        
        if valor < 0:
            valor *= -1
            
        grau_similaridade += valor
    
    return grau_similaridade / 6  # retorno grau de similaridade divido por 6 conforme formula


def calcula_assinatura(texto):
    """Função que executa os cálculos e devolve uma lista dos resultados."""
    sentencas = separa_sentencas(texto)
    frases = extrai_frases(sentencas)
    palavras = extrai_palavras(frases)
    
    # Cálculo dos membros das assinaturas
    wal = calcula_tamanho_medio_palavra(palavras)
    ttr = calcula_typen_token(palavras)
    hlr = calcula_Hapax_Legomana(palavras)
    
    sal = calcula_tamanho_medio_sentencas(sentencas)
    sac = calcula_complexidade_sentenca(frases, len(sentencas))
    pal = calcula_tamanho_medio_frase(frases)
   
    return [wal, ttr, hlr, sal, sac, pal]
    

def avalia_textos(textos, ass_cp):
    assinaturas = []
    for te in textos:
        assinaturas.append(calcula_assinatura(te))

    grau_similaridade = 1000.0
    num_tex = -1
    
    for i in range( 0, len(assinaturas)):
        similaridade = compara_assinatura(ass_cp, assinaturas[i])
                
        if (similaridade < grau_similaridade):
            grau_similaridade = similaridade
            num_tex = i + 1

    return num_tex


def extrai_frases(sentencas):
    """Função que retorna a frase de uma sentença."""
    frases = []
    for sentenca in sentencas:  
        frases += separa_frases(sentenca)
        
    return frases
    
    
def extrai_palavras(sentencas):
    """Função que retira palavras de um texto."""
    palavras = []
    frases = extrai_frases(sentencas)
    for frase in frases:
        palavras += separa_palavras(frase)
        
    return palavras
    

def calcula_tamanho_medio_palavra(palavras):
    """Função que calcula a media dos caracteres por palavra."""
    tamanho = 0
    for pal in palavras:
        tamanho += len(pal)
        
    return tamanho / len(palavras)


def calcula_typen_token(palavras):
    """Função que calcula o numero de palavras diferentes pelo total de palavras."""
    numPalavrasDif = n_palavras_diferentes(palavras)
    return numPalavrasDif / len(palavras)


def calcula_Hapax_Legomana(palavras):
    """Função que calcula numero de palavras ja dividido pelo total de palavras."""
    numPalavasUnicas = n_palavras_unicas(palavras)
    return numPalavasUnicas / len(palavras)


def calcula_tamanho_medio_sentencas(sentencas):
    """Função que retorna media do numero de caracteres por sentenca."""
    tamanho = 0
    for sentenca in sentencas:
        s = re.sub(r'[.!?]+', "", sentenca)
        tamanho += len(s)
    return tamanho / len(sentencas)


def calcula_complexidade_sentenca(frases, sentencas):
    """Função que retorna pelo numero de sentencas."""
    n_frases = len(frases)
    return n_frases / sentencas


def calcula_tamanho_medio_frase(frases):
    """Função que retorna media da frase."""
    tamanho = 0
    for frase in frases:
        f =  re.sub(r'[,:;]+', "", frase)
        tamanho += len(f)

    return tamanho / len(frases)


assinatura = le_assinatura()  # dados da assinatura
textos = le_textos()  # texto para analise

infectados = avalia_textos(textos, assinatura)

print("\n\nO autor do texto {} esta infectado com COH-PIAH".format(infectados))

