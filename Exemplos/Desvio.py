import NewtonGravity as ng

#                                   NOME     COR    R  MASSA          POSIÇÃO      VELOCIDADE
Planeta_A  = ng.CorpoCeleste('Terra_A'  , 'Blue' , 1,  1,          [-2.0, -4.0], [0.0,   2.00])
Planeta_B  = ng.CorpoCeleste('Terra_B'  , 'Red'   , 5,  400E6,      [+0.0,  0.0], [0.0,  -0.00])

# Inicia o Universo
Universo = ng.Universo()

# Adiciona os Corpos no Universo
Universo.Add_Corpos([Planeta_A, Planeta_B])


# Inicia a Simulação
Universo.Start()

