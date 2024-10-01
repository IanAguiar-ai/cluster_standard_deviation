"""
Clusterização por menor caminho, ele pega o ponto menos distante de um grupo...

Algoritimo:
    Com pontos iniciais para começar o grupo, pega um ponto aleatório;
    Se o ponto aleatório tiver seu vizinho mais próximo como um ponto de outro grupo agora ele pertence a outro ponto;
    Isso acontece até que todos os pontos tenham grupos
"""
from copy import deepcopy
from cluster_deviation import distance
from random import random

class Cluster_Min:
    """
    Classe que recebe:
    points:list = Lista de pontos
    """
    def __init__(self, points:list) -> None:
        self.list = points
        self.groups = []

    def cluster(self, groups_index:list) -> None:
        """
        Faz a clusterização
        """
        # Inicia os grupos
        self.list.extend(groups_index)
        self.list = sorted(self.list, key = lambda x: random())
        groups:dict = {}
        dones:list = []
        not_dones:list = deepcopy(self.list)

        for i in range(len(groups_index)):
            groups[i] = [groups_index[i]]
            dones.append(groups_index[i])
            not_dones.remove(groups_index[i])

        # Começa a separar os grupos
        while not_dones != []:
            # Seleciona um ponto de not_dones
            point = not_dones[0]
            min_dist = float('inf')
            closest_group = None
            
            # Encontra o grupo com o ponto mais próximo
            for group_idx, group_points in groups.items():
                for group_point in group_points:
                    dist = distance(point, group_point)
                    if dist < min_dist:
                        min_dist = dist
                        closest_group = group_idx

            # Adiciona o ponto ao grupo mais próximo
            groups[closest_group].append(point)
            dones.append(point)
            not_dones.remove(point)

        self.groups = groups
