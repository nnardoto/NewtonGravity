import NewtonGravity as ng

#                        NOME     COR       R  MASSA          POSIÇÃO      VELOCIDADE
Terra  = ng.CorpoCeleste('Terra', 'Green' , 1, 1      ,      [1.0, 0.0], [0.0,  0.07])
Terra2 = ng.CorpoCeleste('Terra', 'Blue'  , 1, 1      ,      [1.6, 0.0], [0.0,  0.07])
Sol    = ng.CorpoCeleste('Sol'  , 'Red'   , 10, 333.0E3,     [0.0, 0.0], [0.0,  0.00])

# Inicia o Universo
Universo = ng.Universo()

# Adiciona os Corpos ao Universo
Universo.Add_Corpos([Sol, Terra, Terra2])


# Inicia a Simulação
Universo.Start()

