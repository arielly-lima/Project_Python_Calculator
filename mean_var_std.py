import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # Transforma a lista em uma matriz
    matriz = np.array(list).reshape(3, 3)
    # medias
    media_linha = matriz.mean(axis=0).tolist()
    media_coluna = matriz.mean(axis=1).tolist()
    media_flat = matriz.mean().tolist()
    # Variâncias
    variancia_linha = matriz.var(axis=0).tolist()
    variancia_coluna = matriz.var(axis=1).tolist()
    variancia_flat = matriz.var().tolist()
    # Desvios padrões
    desvio_padrao_l = matriz.std(axis=0).tolist()
    desvio_padrao_c = matriz.std(axis=1).tolist()
    desvio_flat = matriz.std().tolist()

    #Máximo
    maximo_l = matriz.max(axis=0).tolist()
    maximo_c = matriz.max(axis=1).tolist()
    maximo = matriz.max().tolist()

    #Mínimo
    minimo_l = matriz.min(axis=0).tolist()
    minimo_c = matriz.min(axis=1).tolist()
    minimo = matriz.min().tolist()

    #Soma
    soma_l = matriz.sum(axis=0).tolist()
    soma_c = matriz.sum(axis=1).tolist()
    soma = matriz.sum().tolist()

    # Dicionário
    calculations = {
        #Média
        'mean': [media_linha, media_coluna, media_flat],
        #Variância 
        'variance': [variancia_linha, variancia_coluna, variancia_flat],
        # Desvio padrão
        'standard deviation': [desvio_padrao_l, desvio_padrao_c, desvio_flat],
        # Máximo
        'max': [maximo_l, maximo_c, maximo],
        # "Máximo'
        'min': [minimo_l, minimo_c, minimo],
        # Soma
        'sum': [soma_l, soma_c, soma]

    }
    return calculations
