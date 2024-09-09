# cluster_standard_deviation

Proprietary technique designed for simple n-dimensional clustering

## To download:

```
pip install git+https://github.com/IanAguiar-ai/cluster_standard_deviation
```

## To use:

```
from cluster_deviation import Cluster_Deviation

help(Cluster_Deviation)
```

## Do funcionamento:

### Introduction/Introdução:

The *cluster_deviation* is an n-dimensional clustering method developed with the goal of being as simple as possible. It is an iterative and non-deterministic method, as the result depends on the order in which the data is processed. The algorithm operates using only the concepts of distance, standard deviation, attraction (pull), and repulsion (push).

O *cluster_deviation* é um método de clusterização n-dimensional desenvolvido com o objetivo de ser o mais simples possível. Trata-se de um método iterativo e não determinístico, pois o resultado depende da ordem em que os dados são processados. O algoritmo opera utilizando apenas os conceitos de distância, desvio padrão, aproximação (puxar) e afastamento (empurrar).

### Algorithm/Algorítimo:

When processing the observations (structured data), where all share the same dimensions, the method follows these steps:

1. Calculates the standard deviation;
2. Iterates over all Q observations, interacting with the other (Q-1) observations;
3. If the distance between two points, as shown in the (DISTANCE) formula, is less than the standard deviation, the points attract each other, as illustrated in the (ATTRACTION) formula; otherwise, the points repel, as demonstrated in the (REPULSION) formula;
4. At the end of this stage, the points will have their n-dimensional positions modified, and the clustering algorithm is initiated;
5. Any point is selected, and its modified distance is compared with the other points that do not yet belong to a group. If the distance between them is less than the sum of the standard deviation and a threshold, the point is included in the group. The threshold is a parameter adjustable by the user;
6. The threshold can range from a value equivalent to the standard deviation up to infinity. Thus, as long as no points are positioned exactly at the same coordinates, it is possible to form clusters with 2 to Q groups;
7. At the end of the clustering iterations, all points will be assigned to a group.


Ao processar as observações (dados estruturados), onde todas compartilham as mesmas dimensões, o método realiza os seguintes passos:

1. Calcula o desvio padrão;
2. Itera sobre todas as Q observações, interagindo com as outras (Q-1) observações;
3. Se a distância entre dois pontos, conforme demonstrado na fórmula (DISTÂNCIA), for menor que o desvio padrão, os pontos se atraem, como ilustrado na fórmula (ATRAÇÃO); caso contrário, os pontos se afastam, conforme demonstrado na fórmula (REPULSÃO);
4. Ao final dessa etapa, os pontos terão suas posições n-dimensionais modificadas, e o algoritmo de agrupamento é iniciado;
5. Um ponto qualquer é selecionado, e sua distância modificada é comparada com a dos demais pontos que ainda não pertencem a um grupo. Se a distância entre eles for menor que a soma do desvio padrão e de um threshold, o ponto é incluído no grupo. O threshold é um parâmetro ajustável pelo usuário;
6. O threshold pode variar de um valor equivalente ao desvio padrão até o infinito. Assim, desde que nenhum ponto esteja posicionado exatamente na mesma coordenada, é possível formar agrupamentos com 2 até Q grupos;
7. Ao final das iterações de agrupamento, todos os pontos estarão atribuídos a um grupo.

### Formulas/Fórmulas:

(DISTANCI/DISTANCIA)

Given two points **P** and **Q** in an n-dimensional space, where:

- **P** = (x₁, x₂, ..., xₙ)
- **Q** = (y₁, y₂, ..., yₙ)

The distance between **P** and **Q** is given by the following formula:

$$
d(P, Q) = \sqrt{(x₁ - y₁)^2 + (x₂ - y₂)^2 + \dots + (xₙ - yₙ)^2}
$$

This formula represents the Euclidean distance between the two points in n-dimensional space.

(ATTRACTION/ATRACAO)

Given two points **P**, where:

$$
P_1 = PUSH(P_1, P_2) = P_{1,i} + \lambda * (P_{2,i} − P_{1,i})
$$

(REPULSION/REPULSAO)

Given two points **P**, where:

$$
P_1 = PULL(P_1, P_2) = P_{1,i} - \lambda * (P_{2,i} − P_{1,i})
$$
