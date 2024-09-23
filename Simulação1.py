import random

# Tempos médios de cada atividade
TEMPO_CONFERIR = 1
TEMPO_TEREO = 3
TEMPO_1O_ANDAR = 5
TEMPO_EMBALAR = 4
TEMPO_DESPACHAR = 1

# Função para simular o tempo de processamento de um pedido
def processar_pedido(prob_terreo):
    # Conferir pedido
    tempo_total = TEMPO_CONFERIR

    # Decidir se o produto está no térreo ou no 1º andar
    if random.random() < prob_terreo:
        tempo_total += TEMPO_TEREO
    else:
        tempo_total += TEMPO_1O_ANDAR

    # Decidir se o produto é para presente (20% de chance)
    if random.random() < 0.2:
        tempo_total += TEMPO_EMBALAR

    # Despachar o produto
    tempo_total += TEMPO_DESPACHAR

    return tempo_total

# Função para simular a loja por um período determinado (minutos_simulacao)
def simular_loja(prob_terreo, tempo_entre_pedidos, minutos_simulacao, seed):
    # Configurar a semente do random
    random.seed(seed)

    tempo_atual = 0
    fila_de_pedidos = []
    pedidos_processados = 0
    tempo_total_fila = 0
    proximo_tempo_disponivel = 0  # Tempo em que o funcionário estará disponível

    # Simulação por um tempo mais longo
    while tempo_atual < minutos_simulacao:
        # Chegada de novo pedido a cada tempo_entre_pedidos minutos
        if len(fila_de_pedidos) == 0 or tempo_atual >= fila_de_pedidos[-1] + tempo_entre_pedidos:
            fila_de_pedidos.append(tempo_atual)

        # Processamento do próximo pedido, se o funcionário estiver disponível
        if fila_de_pedidos and tempo_atual >= proximo_tempo_disponivel:
            chegada = fila_de_pedidos.pop(0)
            tempo_proximo_pedido = processar_pedido(prob_terreo)
            tempo_espera = max(0, tempo_atual - chegada)  # Tempo de espera na fila
            tempo_total_fila += tempo_espera  # Soma o tempo de espera
            proximo_tempo_disponivel = tempo_atual + tempo_proximo_pedido  # Atualiza o próximo tempo que o funcionário estará livre
            pedidos_processados += 1

        # Avançar o tempo
        tempo_atual += 1

    return pedidos_processados, tempo_total_fila / pedidos_processados if pedidos_processados > 0 else 0

# Parâmetros da simulação
MINUTOS_SIMULACAO = 60  # Tempo total de simulação
TEMPO_ENTRE_PEDIDOS_NORMAL = 7  # Tempo constante entre pedidos
NUM_SIMULACOES = 30  # Número de simulações para cada cenário

# Listas para armazenar os resultados
resultados = []

# Realizar 30 simulações para cada cenário
for i in range(NUM_SIMULACOES):
    # Gerar uma semente aleatória
    seed = random.randint(1, 100000)

    # Simulação com 70% de chance de estar no térreo
    pedidos_70, tempo_medio_espera_70 = simular_loja(0.7, TEMPO_ENTRE_PEDIDOS_NORMAL, MINUTOS_SIMULACAO, seed)

    # Simulação com 55% de chance de estar no térreo
    pedidos_55, tempo_medio_espera_55 = simular_loja(0.55, TEMPO_ENTRE_PEDIDOS_NORMAL, MINUTOS_SIMULACAO, seed)

    # Adicionar os resultados às listas (semente, tempo_70, tempo_55)
    resultados.append((seed, tempo_medio_espera_70, tempo_medio_espera_55))

# Exibir os resultados
print("Semente   | Tempo de Espera (70% Térreo) | Tempo de Espera (55% Térreo)")
print("---------------------------------------------------------------")
for seed, tempo_70, tempo_55 in resultados:
    print(f"{seed:<9} | {tempo_70:<24.2f} | {tempo_55:<26.2f}")
