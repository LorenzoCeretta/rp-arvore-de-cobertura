from redes_de_petri_marcadas import A_in_1, A_out_1, x0_1, A_in_2, A_out_2, x0_2
from arvore_cobertura import arvore_de_cobertura, imprimir_arvore

print("-- Caso 1: Rede Limitada --")
arestas = arvore_de_cobertura(x0_1, A_in_1, A_out_1)
imprimir_arvore(arestas)

print("\n-- Caso 2: Rede Ilimitada --")
arestas = arvore_de_cobertura(x0_2, A_in_2, A_out_2)
imprimir_arvore(arestas)
