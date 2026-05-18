# rp-arvore-de-cobertura

# Algoritmo da Árvore de Cobertura para Redes de Petri

Este projeto implementa o algoritmo de busca em largura (BFS) para construir a **Árvore de Cobertura** de uma Rede de Petri, tratando tanto sistemas limitados quanto ilimitados através da introdução do símbolo de infinito ($\omega$, representado no código como w).

## Estrutura

- **`arvore_cobertura.py`**: Lógica das funções necessárias para a execução do algoritmo.
- **`redes_de_petri_marcadas.py`**: Arquivo de configuração onde são definidas as matrizes de entrada (A_in), saída (A_out) e a marcação inicial (x0) das redes de teste.
- **`main.py`**: Executa os casos de teste e exibe os resultados formatados no terminal.
- **`testes.py`**: Script contendo testes unitários simples para validar o comportamento isolado de cada função.

## Como o Algoritmo Funciona

O algoritmo processa a árvore passo a passo utilizando uma fila:

1. **`transicao_esta_habilitada`**: Varre os lugares da rede para garantir que o estado atual possui fichas suficientes para disparar uma transição específica. Se um lugar contiver `w`, a checagem é ignorada (quantidade de fichas consideradas infinitas).
2. **`disparar`**: Calcula a próxima marcação aplicando a equação de estado ($X' = X - A_{in} + A_{out}$). Valores em w permanecem inalterados após a operação.
3. **`expandir_marcacao`**: Faz a varredura de todas as transições da rede para mapear quais ramos podem brotar a partir do nó atual.
4. **`tem_ancestral_menor`**: Compara o nó recém-gerado com o histórico de seus nós pais na árvore para verificar se a rede manteve estabilidade ou se está crescendo sem limite.
5. **`aplicar_w`**: Se for detectado um crescimento em relação a algum ancestral, localiza o lugar exato onde o número de fichas aumentou e crava o símbolo w (float("inf")).
6. **`arvore_de_cobertura`**: Gerencia o laço principal. Marcações inéditas continuam expandindo a árvore; marcações repetidas interrompem o ramo (nós terminais), garantindo que o algoritmo finalize mesmo em redes infinitas.

## Como Executar

Certifique-se de ter o Python instalado e rode o arquivo principal no terminal:

```bash
python3 main.py
```
