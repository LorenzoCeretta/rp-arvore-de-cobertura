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
