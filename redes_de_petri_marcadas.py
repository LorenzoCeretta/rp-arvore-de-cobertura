# Ao implementar o algoritmo da Árvore de Cobertura, vale notar dois casos:
# (i) Redes Limitadas (sem a presença de w)
# (ii) Redes Ilimitadas (com a presença de w)

# -- Caso 1: Rede de Petri Limitada --

# Matriz Pre: A_in_1[lugar][transição] = tokens consumidos
A_in_1 = [
    #  t1  t2  t3
    [1, 0, 0],  # P1
    [0, 1, 0],  # P2
    [0, 0, 1],  # P3
]

# Matriz Post: A_out_1[lugar][transição] = tokens produzidos
A_out_1 = [
    #  t1  t2  t3
    [0, 0, 1],  # P1
    [1, 0, 0],  # P2
    [0, 1, 0],  # P3
]

# Marcação Inicial
x0_1 = [1, 0, 0]

# -- Caso 2: Rede de Petri Ilimitada --

# Matriz Pre: A_in_2[lugar][transição] = tokens consumidos
A_in_2 = [
    #  t1  t2
    [1, 0],  # P1
    [0, 1],  # P2
]

# Matriz Post: A_out_2[lugar][transição] = tokens produzidos
A_out_2 = [
    #  t1  t2
    [1, 1],  # P1
    [1, 0],  # P2
]

# Marcação Inicial
x0_2 = [1, 0]

# -- Caso 3: Rede com Bifurcação --
#
#        t1 --> P2 --t3--> P4
#   P1 --|
#        t2 --> P3 --t4--> P5
#
# Dois caminhos a partir de x0, cada um com mais um passo.

# Matriz Pre: A_in_3[lugar][transição] = tokens consumidos
A_in_3 = [
    #  t1  t2  t3  t4
    [1, 1, 0, 0],  # P1
    [0, 0, 1, 0],  # P2
    [0, 0, 0, 1],  # P3
    [0, 0, 0, 0],  # P4
    [0, 0, 0, 0],  # P5
]

# Matriz Post: A_out_3[lugar][transição] = tokens produzidos
A_out_3 = [
    #  t1  t2  t3  t4
    [0, 0, 0, 0],  # P1
    [1, 0, 0, 0],  # P2
    [0, 1, 0, 0],  # P3
    [0, 0, 1, 0],  # P4
    [0, 0, 0, 1],  # P5
]

# Marcação Inicial
x0_3 = [1, 0, 0, 0, 0]
