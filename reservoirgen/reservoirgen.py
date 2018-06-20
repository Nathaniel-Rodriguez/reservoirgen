import numpy as np


def generate_reservoir_from_edge_list(graph, distribution, dtype=np.float32):
    """
    Generates a weighted reservoir from an unweighted network. The network
    can be expressed as an edge list
    :param graph: a Ex2 numpy edge list. Indices are assumed to correspond to
        neuron ids. Assumed edge list represents i->j connections given (i,j)
        values. e.g. (graph[x][i], graph[x][j])
    :param distribution: a distribution that can be called with a shape parameter
        e.g.: random_values = distribution(shape)
    :return: numpy square matrix of size NxN, where N = # of identified neurons
        rows are predecessors of ith neuron, e.g. ith row is all of the neurons
        connecting TO i. So the sum of values in the ith row is the in-strength
        of i. This orientation is chosen so that the dot product: M * x can be
        done to give the sum of incoming excitations if x is the state vector Nx1.
    """




def generate_reservoir_from_adj_matrix(graph, distribution, dtype=np.float32):
    """
    Generates a weighted reservoir from an unweighted network. The network
    can be expressed as an numpy matrix
    :param graph: a matrix with head as first axis, tails as second axis.
        e.g. graph[i,j] gives link from j->i
    :param distribution:
    :return:
    """

def generate_reservoir_from_nx_graph(graph, distribution, dtype=np.float32):


if __name__ == "__main__":
    pass
