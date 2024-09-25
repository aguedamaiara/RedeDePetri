# Projeto de Simulação de uma Rede de Petri
## Descrição da Atividade
Este projeto foi desenvolvido para a disciplina de Modelagem de Processos de Negócio (MPN) e visa simular o fluxo de pedidos em uma loja de departamento chamada ShopeeCareta. A loja recebe pedidos em um ritmo definido, e o objetivo é analisar o impacto de diferentes fatores, como a localização dos produtos (térreo ou primeiro andar) e o tempo entre os pedidos, no tempo de espera dos clientes. O projeto também explora a necessidade de contratação de um funcionário temporário em dias de alta demanda.

### Cenário
Na ShopeeCareta, os pedidos chegam a cada 7 minutos. O funcionário confere cada pedido e se desloca até a prateleira para pegar o produto, que pode estar no térreo ou no primeiro andar. Caso o produto seja para presente, ele também precisa ser embalado antes de ser despachado. A probabilidade de um produto estar no térreo é de 70% e a chance de ser para presente é de 20%.

## Resumo dos Códigos
O projeto contém dois códigos principais que simulam o fluxo de pedidos:

1. **Simulação1.py: Simulação do Tempo de Espera**
   - Simula o tempo total de processamento de um pedido, considerando o tempo para conferir, deslocar, embalar (se necessário) e despachar.
   - Realiza simulações para dois cenários: com 70% de probabilidade de produtos no térreo e com 55%.
   - Coleta dados sobre o tempo médio de espera dos pedidos processados.

2. **Simulação2.py: Análise de Impacto em Dias Especiais**
   - Compara o tempo médio de espera em condições normais (7 minutos entre pedidos) e em dias especiais (3 minutos entre pedidos).
   - Avalia a necessidade de um funcionário temporário com base na diferença de tempo médio de espera.

## Instruções para Rodar o Projeto

1. **Pré-requisitos:**
   - Certifique-se de que o Python está instalado em sua máquina. O código foi testado em Python 3.11.

2. **Clone o Repositório:**
   ```bash
   git clone https://github.com/aguedamaiara/RedeDePetri.git
   cd RedeDePetri
