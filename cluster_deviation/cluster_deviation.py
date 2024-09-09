"""
Clusterização pelo desvio padrão
"""
from copy import deepcopy

class Cluster_Deviation:
    """
    Classe que recebe:
    points:list = Lista de pontos
    factor_pull:float = Fator para puxar o ponto 2 em relação ao ponto 1
    factor_push:float = Fator para empurrar o ponto 2 em relação ao ponto 1
    """
    def __init__(self, points:list, factor_pull:float = 0.1, factor_push:float = 0.001) -> None:
        self.list = points
        self.old_list = deepcopy(points)
        self.factor_pull = factor_pull
        self.factor_push = factor_push
        self.first_deviation = self.deviation()
        self.temporary_groups = []

    def deviation(self) -> float:
        """
        Função que calcula o desvio padrão n-dimensional
        """
        number_points:int = len(self.list)
        dimentions:int = len(self.list[0])
        means:list[float] = [sum(point[i] for point in self.list)/number_points for i in range(dimentions)]
        variance_sum:float = sum(sum((point[i] - means[i]) ** 2 for i in range(dimentions)) for point in self.list)
        return (variance_sum/(number_points * dimentions)) ** 0.5

    def group(self, threshold:float = None, amount:int = None) -> bool:
        """
        Função que descobre os agrupamentos

        Pode receber como parâmetro:
        threshold:float = valor além do desvio padrão para que seja considerado um grupo
        amount:int = quantidade de grupos se for possível
        """
        if amount != None and type(amount) == int:
            self.group(threshold = 0)
            threshold_min:float = 0
            threshold_max:float = self.first_deviation * 10
            mid_threshold:float = (threshold_min + threshold_max)/2

            iterations:int = 0
            while len(self.temporary_groups) != amount:
                if iterations > 100:
                    print(f"Could not find {amount} groups")
                    return False
                    
                mid_threshold:float = (threshold_min + threshold_max)/2
                #print(f"{len(self.temporary_groups):2} | {threshold_min:8.04f} | {threshold_max:8.04f} | {mid_threshold:8.04f}")
                self.group(threshold = mid_threshold)

                if len(self.temporary_groups) > amount:
                    threshold_min:float = mid_threshold
                else:
                    threshold_max:float = mid_threshold

                if threshold_max == threshold_min:
                    threshold_max:float = mid_threshold * 2

                iterations += 1

            #print(f"groups({len(self.temporary_groups)}) = {mid_threshold} <----")
            return True

        if threshold == None:
            threshold:float = self.first_deviation

        self.temporary_groups = []
        self.groups = []

        temporary_list = deepcopy(self.list)
        temporary_list_old = deepcopy(self.old_list)

        while len(temporary_list) != 0:
            point_cluster:list = temporary_list[0]
            point_cluster_old:list = temporary_list_old[0]
            
            temporary_group:list = [point_cluster]
            temporary_group_old:list = [point_cluster_old]
            
            temporary_list.remove(point_cluster)
            temporary_list_old.remove(point_cluster_old)

            for point, point_old in zip(deepcopy(temporary_list), deepcopy(temporary_list_old)):
                if distance(point_cluster, point) <= threshold:
                    temporary_group.append(point)
                    temporary_group_old.append(point_old)
                    
                    temporary_list.remove(point)
                    temporary_list_old.remove(point_old)

            self.temporary_groups.append(temporary_group)
            self.groups.append(temporary_group_old)
        return True

    def cluster(self, iterations:int = 1, threshold:float = 0, amount:int = None) -> bool:
        """
        Faz a clusterização
        Se falhar retorna False, caso contrário, retorna True
        """
        len_self_list = sorted([len(point) for point in self.list])
        if len_self_list[0] != len_self_list[-1]:
            print("Error with dimensions, {len_self_list[0]} != {len_self_list[-1]}")
            return False
        
        for _ in range(iterations):
            for i in range(len(self.list)):
                for j in range(len(self.list)):
                    if i != j:
                        if distance(self.list[i], self.list[j]) < self.first_deviation:
                            self.list[j] = pull(point_1 = self.list[i], point_2 = self.list[j], factor = self.factor_pull)
                            #print(f"PULL {deviation} {distance(self.list[i], self.list[j])}")
                        else:
                            self.list[j] = push(point_1 = self.list[i], point_2 = self.list[j], factor = self.factor_push)
                            #print(f"PUSH {deviation} {distance(self.list[i], self.list[j])}")

        self.group(threshold, amount)
        return True

def distance(point_1:list, point_2:list) -> float:
    """
    Calcula a distancia entre dois pontos
    """
    return sum([(point_1[i] - point_2[i]) * (point_1[i] - point_2[i]) for i in range(len(point_1))])**0.5

def push(point_1:list, point_2:list, factor:float) -> list:
    """
    Empurra o ponto 2 em relação ao 1
    """
    return [coord2 + factor * (coord2 - coord1) for coord1, coord2 in zip(point_1, point_2)]

def pull(point_1:list, point_2:list, factor:float) -> list:
    """
    Puxa o ponto 2 em relação ao 1
    """
    return [coord2 - factor * (coord2 - coord1) for coord1, coord2 in zip(point_1, point_2)]  
