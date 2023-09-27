import NewtonGravity as ng

#                        NOME     COR       R  MASSA         POSIÇÃO      VELOCIDADE
Terra = ng.CorpoCeleste('Terra', 'Green' ,  1, 1.6    ,   [1.0, 0.0], [0.0,  -0.05])
Sol   = ng.CorpoCeleste('Sol'  , 'Red'   ,  4, 800E3,     [0.0, 0.0], [0.0,  +0.00])

# Inicia o Universo
Universo = ng.Universo()

# Adiciona os Corpos ao Universo
Universo.Add_Corpos([Sol, Terra])


# Inicia a Simulação
Universo.Start()