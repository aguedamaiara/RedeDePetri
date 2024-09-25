import random

# Tempos médios de cada atividade
TEMPO_CONFERIR = 1  # Conferir pedido
TEMPO_TEREO = 3     # Caminhar até a prateleira no térreo (ida e volta)
TEMPO_1O_ANDAR = 5  # Caminhar até a prateleira no 1º andar (ida e volta)
TEMPO_EMBALAR = 4   # Embalar produto para presente
TEMPO_DESPACHAR = 1  # Despachar produto

# Função para simular o tempo de processamento de um pedido
def processar_pedido(prob_terreo):
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
def simular_loja(prob_terreo, tempo_entre_pedidos, minutos_simulacao):
    tempo_atual = 0
    fila_de_pedidos = []
    pedidos_processados = 0
    tempo_total_fila = 0
    proximo_tempo_disponivel = 0  # Tempo em que o funcionário estará disponível

    # Simulação por um tempo mais longo
    while tempo_atual < minutos_simulacao:
        # Chegada de novo pedid a cada tempo_entre_pedidos minutos
        if len(fila_de_pedidos) == 0 or tempo_atual >= fila_de_pedidos[-1] + tempo_entre_pedidos:
            fila_de_pedidos.append(tempo_atual)

        # Processamento do próx pedido, se o funcionario estiver disponível
        if fila_de_pedidos and tempo_atual >= proximo_tempo_disponivel:
            chegada = fila_de_pedidos.pop(0)
            tempo_proximo_pedido = processar_pedido(prob_terreo)
            tempo_espera = max(0, tempo_atual - chegada)  # Tempo de espera na fila
            tempo_total_fila += tempo_espera  # Soma o tempo de espera
            proximo_tempo_disponivel = tempo_atual + tempo_proximo_pedido  # Atualiza o próximo tempo que o funcionário estará livre
            pedidos_processados += 1

        # Avançar o tempo
        tempo_atual += 1

    # Retornar total de pedidos processados e tempo médio de espera
    return pedidos_processados, tempo_total_fila / pedidos_processados if pedidos_processados > 0 else 0

# Parâmetros da simulação
MINUTOS_SIMULACAO = 600  # 10 horas de expediente
TEMPO_ENTRE_PEDIDOS_NORMAL = 7  # Tempo entre pedidos normal
TEMPO_ENTRE_PEDIDOS_ESPECIAL = 3  # Tempo entre pedidos em dias especiais

# Simulação normal (70% no térreo)
pedidos_normal, tempo_medio_espera_normal = simular_loja(0.7, TEMPO_ENTRE_PEDIDOS_NORMAL, MINUTOS_SIMULACAO)

# Simulação em dias especiais (70% no térreo)
pedidos_especial, tempo_medio_espera_especial = simular_loja(0.7, TEMPO_ENTRE_PEDIDOS_ESPECIAL, MINUTOS_SIMULACAO)

# Exibir resultados
print(f"Resultados da simulação normal (70% no térreo):")
print(f"Pedidos processados: {pedidos_normal}, Tempo médio de espera: {tempo_medio_espera_normal:.2f} minutos")

print(f"\nResultados da simulação em dias especiais (70% no térreo):")
print(f"Pedidos processados: {pedidos_especial}, Tempo médio de espera: {tempo_medio_espera_especial:.2f} minutos")

# Análise da necessidade de um funcionário temporário
diferenca_absoluta = tempo_medio_espera_especial - tempo_medio_espera_normal
diferenca_percentual = (diferenca_absoluta / tempo_medio_espera_normal) * 100 if tempo_medio_espera_normal > 0 else float('inf')

# Definir um limite de diferença que considere a necessidade de um funcionário
limite_diferenca = 50  # Exemplo de 50 minutos como um limite

if diferenca_absoluta > limite_diferenca or diferenca_percentual > 50:  # Exemplo de 50% como um limite
    print("\nA diminuição do tempo entre chegadas de pedidos interfere significativamente na fila de pedidos em espera.")
    print("A contratação de um funcionário temporário é justificada devido ao aumento no fluxo de pedidos.")
else:
    print("\nA diminuição do tempo entre chegadas de pedidos não interfere significativamente na fila de pedidos em espera.")
    print("A contratação de um funcionário temporário pode não ser justificada.")
import random

# Tempos médios de cada atividade
TEMPO_CONFERIR = 1  # Conferir pedido
TEMPO_TEREO = 3  # Caminhar até a prateleira no térreo (ida e volta)
TEMPO_1O_ANDAR = 5  # Caminhar até a prateleira no 1º andar (ida e volta)
TEMPO_EMBALAR = 4  # Embalar produto para presente
TEMPO_DESPACHAR = 1  # Despachar produto


# Função para simular o tempo de processamento de um pedido
def processar_pedido(prob_terreo):
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
def simular_loja(prob_terreo, tempo_entre_pedidos, minutos_simulacao):
    tempo_atual = 0
    fila_de_pedidos = []
    pedidos_processados = 0
    tempo_total_fila = 0
    proximo_tempo_disponivel = 0  # Tempo em que o funcionário estará disponível

    # Simulação por um tempo mais longo
    while tempo_atual < minutos_simulacao:
        # Chegada de novo pedido a cada tempo_entre_pedidos minutos
        if len(
                fila_de_pedidos
        ) == 0 or tempo_atual >= fila_de_pedidos[-1] + tempo_entre_pedidos:
            fila_de_pedidos.append(tempo_atual)

        # Processamento do próximo pedido, se o funcionário estiver disponível
        if fila_de_pedidos and tempo_atual >= proximo_tempo_disponivel:
            chegada = fila_de_pedidos.pop(0)
            tempo_proximo_pedido = processar_pedido(prob_terreo)
            tempo_espera = max(0, tempo_atual -
                               chegada)  # Tempo de espera na fila
            tempo_total_fila += tempo_espera  # Soma o tempo de espera
            proximo_tempo_disponivel = tempo_atual + tempo_proximo_pedido  # Atualiza o próximo tempo que o funcionário estará livre
            pedidos_processados += 1

        # Exibir informações sobre o estado da fila
        print(
            f"Minuto {tempo_atual}, Tamanho da fila: {len(fila_de_pedidos)}, Próximo tempo disponível: {proximo_tempo_disponivel}"
        )

        # Avançar o tempo
        tempo_atual += 1

    # Retornar total de pedidos processados e tempo médio de espera
    return pedidos_processados, tempo_total_fila / pedidos_processados if pedidos_processados > 0 else 0


# Parâmetros da simulação
MINUTOS_SIMULACAO = 600  # 10 horas de expediente
TEMPO_ENTRE_PEDIDOS_NORMAL = 7  # Tempo entre pedidos normal
TEMPO_ENTRE_PEDIDOS_ESPECIAL = 3  # Tempo entre pedidos em dias especiais

# Simulação normal (70% no térreo)
pedidos_normal, tempo_medio_espera_normal = simular_loja(
    0.7, TEMPO_ENTRE_PEDIDOS_NORMAL, MINUTOS_SIMULACAO)

# Simulação em dias especiais (70% no térreo)
pedidos_especial, tempo_medio_espera_especial = simular_loja(
    0.7, TEMPO_ENTRE_PEDIDOS_ESPECIAL, MINUTOS_SIMULACAO)

# Exibir resultados
print(f"Resultados da simulação normal (70% no térreo):")
print(
    f"Pedidos processados: {pedidos_normal}, Tempo médio de espera: {tempo_medio_espera_normal:.2f} minutos"
)

print(f"\nResultados da simulação em dias especiais (70% no térreo):")
print(
    f"Pedidos processados: {pedidos_especial}, Tempo médio de espera: {tempo_medio_espera_especial:.2f} minutos"
)

# Análise da necessidade de um funcionário temporário
diferenca_absoluta = tempo_medio_espera_especial - tempo_medio_espera_normal
diferenca_percentual = (diferenca_absoluta / tempo_medio_espera_normal
                        ) * 100 if tempo_medio_espera_normal > 0 else float(
                            'inf')

# Definir um limite de diferença que considere a necessidade de um funcionário
limite_diferenca = 50  # Exemplo de 50 minutos como um limite

if diferenca_absoluta > limite_diferenca or diferenca_percentual > 50:  # Exemplo de 50% como um limite
    print(
        "\nA diminuição do tempo entre chegadas de pedidos interfere significativamente na fila de pedidos em espera."
    )
    print(
        "A contratação de um funcionário temporário é justificada devido ao aumento no fluxo de pedidos."
    )
else:
    print(
        "\nA diminuição do tempo entre chegadas de pedidos não interfere significativamente na fila de pedidos em espera."
    )
    print(
        "A contratação de um funcionário temporário pode não ser justificada.")
