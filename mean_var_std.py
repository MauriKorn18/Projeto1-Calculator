import numpy as np  # biblioteca NumPy (atalho 'np')

def calculate(numbers):  # função principal
    if len(numbers) != 9:  # precisa ter exatamente 9 números
        raise ValueError("List must contain nine numbers.")  # lança erro se não tiver 9

    arr = np.array(numbers).reshape(3, 3)  # transforma a lista em um array 3x3

# mapeamento dos eixos: colunas (axis=0), linhas (axis=1), total (flatten)

    results = {
    'mean': [
        arr.mean(axis=0).tolist(),  # médias por coluna (lista)
        arr.mean(axis=1).tolist(),  # médias por linha (lista)
        float(arr.mean().item())    # média total (float)
    ],
    'variance': [
        arr.var(axis=0).tolist(),   # variâncias por coluna
        arr.var(axis=1).tolist(),   # variâncias por linha
        float(arr.var().item())     # variância total
    ],
    'standard deviation': [
        arr.std(axis=0).tolist(),   # desvios-padrão por coluna
        arr.std(axis=1).tolist(),   # desvios-padrão por linha
        float(arr.std().item())     # desvio-padrão total
    ],
    'max': [
        arr.max(axis=0).tolist(),   # máximos por coluna
        arr.max(axis=1).tolist(),   # máximos por linha
        int(arr.max().item())       # máximo total
    ],
    'min': [
        arr.min(axis=0).tolist(),   # mínimos por coluna
        arr.min(axis=1).tolist(),   # mínimos por linha
        int(arr.min().item())       # mínimo total
    ],
    'sum': [
        arr.sum(axis=0).tolist(),   # somas por coluna
        arr.sum(axis=1).tolist(),   # somas por linha
        int(arr.sum().item())       # soma total
    ]
}

return results  # retorna o dicionário final