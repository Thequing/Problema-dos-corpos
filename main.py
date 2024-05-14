import numpy as np

#Começamos "setando" a constante gravitacional, sempre será a mesma:

G = 6.67430e-11

#Serão passadas as massas dos respectivos corpos (em kg):

massa_terra = 5.972e24 

massa_lua = 7.348e22 

#Coloca-se a distância inicial entre sí (em metros):

r = 3.844e8 

#Velocidade inicial da Lua (em m/s)(não se coloca a da terra pois ela se considera em repouso em comparação a Lua):

v = 1.022e3  

#Iniciando suas posições no sistema:

posicao_terra = np.array([0, 0], dtype=float)

posicao_lua = np.array([r, 0], dtype=float)

velocidade_terra = np.array([0, 0], dtype=float)

velocidade_lua = np.array([0, v], dtype=float)

#Passo de tempo (time step) (dado em segundos), se o passo de tempo é de 1000 segundos, isso significa que estamos avançando a simulação em 1000 segundos a cada etapa.

dt = 1000

#Número de passos de tempo, numero total de vezes que avançamos a simulação pelo passo de tempo, se o número de passos de tempo é 10000, isso significa que avançamos a simulação 10000 vezes, cada vez avançando 1000 segundos.

num_pass = 10000

#Loop sobre o passo de tempo:

for passo in range(num_pass):

    #Vetor de posição relativa entre dois corpos.

    r_vec = posicao_lua - posicao_terra

   #Comprimento (ou magnitude) do vetor de posição relativa. É calculado usando a função np.hypot, que retorna a norma euclidiana, sqrt(xx + yy). Isso dá a distância entre os dois corpos.

    r_mag = np.hypot(*r_vec)

    #Calculando a força pela fórmula da física de atração de corpos:

    forca = G * massa_terra * massa_lua * r_vec / r_mag**3

    #Atualizando as velocidades:

    velocidade_terra += forca *dt / massa_terra

    velocidade_lua -= forca *dt / massa_lua

    #Atualizando as posições:

    posicao_terra += velocidade_terra * dt

    posicao_lua += velocidade_lua * dt

#Por fim, imprimir as posições finais:

print("Posição final da Terra:", posicao_terra)

print("Posição final da Lua:", posicao_lua)

