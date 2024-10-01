"""
Exemplo simples
"""
from copy import deepcopy
from cluster_deviation import Cluster_Deviation
from cluster_min import Cluster_Min

def plot_2d(list_:list):
    """
    Função que plota pontos em 2 dimensões usando matplotlib.
    """
    import matplotlib.pyplot as plt
    
    x_coords = [point[0] for point in list_]
    y_coords = [point[1] for point in list_]
    
    plt.figure(figsize=(8, 6))
    plt.scatter(x_coords, y_coords, c='blue', marker='o')
    
    plt.title('2D Points Plot')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    
    plt.grid(True)
    plt.show()

def plots_2d(list_1:list, list_2:list):
    """
    Função que plota pontos em 2 dimensões usando matplotlib.
    """
    import matplotlib.pyplot as plt
    
    x_coords_1 = [point[0] for point in list_1]
    y_coords_1 = [point[1] for point in list_1]
    x_coords_2 = [point[0] for point in list_2]
    y_coords_2 = [point[1] for point in list_2]
    
    plt.figure(figsize=(8, 6))
    plt.scatter(x_coords_1, y_coords_1, c='blue', marker='o')
    plt.scatter(x_coords_2, y_coords_2, c='orange', marker='o')
    
    plt.title('2D Points Plot')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    
    plt.grid(True)
    plt.show()

def multiple_plot_2d(groups:list[list[list[float]]]):
    """
    Função que plota pontos em 2 dimensões usando matplotlib.
    Cada sub-lista dentro de `groups` representa um grupo, e cada grupo é plotado com uma cor diferente.
    """
    import itertools
    import matplotlib.pyplot as plt
    
    colors = itertools.cycle(['blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan'])
    
    plt.figure(figsize=(8, 6))
    
    for group in groups:
        color = next(colors)
        x_coords = [point[0] for point in group]
        y_coords = [point[1] for point in group]
        plt.scatter(x_coords, y_coords, c=color, marker='o', label=f'Group {groups.index(group) + 1}')
    
    plt.title('2D Points Plot by Groups')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    from random import random, seed
    from copy import deepcopy

##    # Método cluster deviation    
##    metodo = Cluster_Deviation([[random()*20, random()*20] for _ in range(200)])
##    
##    antes = deepcopy(metodo.list)
##    
##    plot_2d(metodo.list)
##    metodo.cluster(iterations = 10)
##    for i in range(2, 5):
##        metodo.group(amount = i)
##
##    metodo.group()
##    multiple_plot_2d(metodo.groups)


    # Método cluster min
    dados = [[x, 8 + (x/4)**2*1.6] for x in range(10)]
    dados.extend([[x, (x/4)**2*1.6] for x in range(10)])

    metodo = Cluster_Min(dados)
    metodo.cluster([[0, -2], [0, 10]])
    print(metodo.groups)

    multiple_plot_2d(list(metodo.groups.values()))

