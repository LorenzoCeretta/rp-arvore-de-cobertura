from arvore_cobertura import (
    w,
    transicao_esta_habilitada,
    disparar,
    expandir_marcacao,
    tem_ancestral_menor,
    aplicar_w,
    arvore_de_cobertura,
)
from redes_de_petri_marcadas import A_in_1, A_out_1, x0_1, A_in_2, A_out_2, x0_2

# Rede 1: ciclo P1 --t1--> P2 --t2--> P3 --t3--> P1, x0 = [1, 0, 0]

# transicao_esta_habilitada: t1 habilitada, t2 bloqueada (P2=0)
print(transicao_esta_habilitada([1, 0, 0], 0, A_in_1))  # True
print(transicao_esta_habilitada([1, 0, 0], 1, A_in_1))  # False

# disparar: t1 em [1,0,0] consome P1 e produz P2
print(disparar([1, 0, 0], 0, A_in_1, A_out_1))  # [0, 1, 0]

# expandir_marcacao: em [1,0,0] só t1 está habilitada
print(expandir_marcacao([1, 0, 0], A_in_1, A_out_1))  # [(0, [0, 1, 0])]

# tem_ancestral_menor: [1,0] <= [1,1] (True), [1,2] <= [1,1] (False)
print(tem_ancestral_menor((1, 0), (1, 1)))  # True
print(tem_ancestral_menor((1, 2), (1, 1)))  # False

# aplicar_w: ancestral [1,0] domina nova [1,1] → P2 cresceu, vira w
print(aplicar_w([1, 1], [(1, 0)]))  # [1, w]

# arvore_de_cobertura — rede limitada: ciclo fecha, 3 arestas, sem w
arestas = arvore_de_cobertura(x0_1, A_in_1, A_out_1)
for origem, t, destino in arestas:
    print(f"  {list(origem)} --t{t+1}--> {list(destino)}")

# arvore_de_cobertura — rede ilimitada: P2 vira w no primeiro passo
arestas = arvore_de_cobertura(x0_2, A_in_2, A_out_2)
print(arestas[0])  # ((1, 0), 0, (1, w))
