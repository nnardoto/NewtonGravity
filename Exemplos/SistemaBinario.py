import NewtonGravity as ng

#                                   NOME     COR    R  MASSA          POSIÇÃO      VELOCIDADE
Planeta_A  = ng.CorpoCeleste('Terra_A'  , 'Green' , 5,  400E6,      [-1.0, 0.0], [0.0,   0.90])
Planeta_B  = ng.CorpoCeleste('Terra_B'  , 'Red'   , 5,  400E6,      [+1.0, 0.0], [0.0,  -0.90])

# Inicia o Universo
Universo = ng.Universo()

# Adiciona os Corpos no Universo
Universo.Add_Corpos([Planeta_A, Planeta_B])


# Inicia a Simulação
Universo.Start()

