import numpy as np


def reservoir_as_edge_list(reservoir, dtype1=np.int, dtype2=np.float32):
    """
    Converts a reservoir to an edge list Ex2 with (i,j) where i->j.
    :param reservoir: reservoir as adjacency matrix
    :param dtype1: type of returned edge list
    :param dtype2: type of returned weight array
    :return: Ex2 numpy array, E numpy array of weights
    """
    pass  # TODO implement


def generate_weights_for_edge_list(graph, distribution, dtype=np.float32):
    """
    Generates weights for edges in edge list
    :param graph: Ex2 numpy array
    :param distribution: a distribution that can be called with a shape parameter
        e.g.: random_values = distribution(shape)
    :param dtype: type of weight array
    :return: an E numpy array of type dtype
    """

    return distribution(size=len(graph)).astype(dtype)


def generate_adj_reservoir_from_edge_list(graph, distribution, dtype=np.float32,
                                          N=None):
    """
    Generates a weighted reservoir from an unweighted network. The network
    can be expressed as an edge list
    :param graph: a Ex2 numpy edge list. Indices are assumed to correspond to
        neuron ids. Assumed edge list represents i->j connections given (i,j)
        values. e.g. (graph[x][i], graph[x][j])
    :param distribution: a distribution that can be called with a shape parameter
        e.g.: random_values = distribution(shape)
    :param dtype: numpy type of output reservoir
    :param N: if the graph is disconnected, then latter nodes maybe lost. So N
        would need to be specified
    :return: numpy square matrix of size NxN, where N = # of identified neurons
        rows are predecessors of ith neuron, e.g. ith row is all of the neurons
        connecting TO i. So the sum of values in the ith row is the in-strength
        of i. This orientation is chosen so that the dot product: M * x can be
        done to give the sum of incoming excitations if x is the state vector Nx1.
    """

    if N is None:
        N = graph.max()

    reservoir = np.zeros((N, N), dtype=dtype)
    flat_indices = np.ravel_multi_index(graph.transpose(), (N, N))
    reservoir.flat[flat_indices] = distribution(size=len(flat_indices))

    return reservoir


def generate_adj_reservoir_from_adj_matrix(graph, distribution, dtype=np.float32):
    """
    Generates a weighted reservoir from an unweighted network. The network
    can be expressed as an numpy matrix
    :param graph: a matrix with head as first axis, tails as second axis.
        e.g. graph[i,j] gives link from j->i
    :param distribution: a distribution that can be called with a shape parameter
        e.g.: random_values = distribution(shape)
    :return: numpy square matrix of size NxN, where N = # of identified neurons
        rows are predecessors of ith neuron, e.g. ith row is all of the neurons
        connecting TO i. So the sum of values in the ith row is the in-strength
        of i. This orientation is chosen so that the dot product: M * x can be
        done to give the sum of incoming excitations if x is the state vector Nx1.
    """

    reservoir = np.zeros(graph.shape, dtype=dtype)
    nonzero_indices = np.nonzero(graph)
    flat_indices = np.ravel_multi_index(nonzero_indices, reservoir.shape)
    reservoir.flat[flat_indices] = distribution(size=len(flat_indices))

    return reservoir


def generate_adj_reservoir_from_nx_graph(graph, distribution, dtype=np.float32):
    """
    Generates a weighted reservoir from an unweighted network. The network
    can be expressed as an numpy matrix
    :param graph: a matrix with head as first axis, tails as second axis.
        e.g. graph[i,j] gives link from j->i
    :param distribution: a distribution that can be called with a shape parameter
        e.g.: random_values = distribution(shape)
    :return: numpy square matrix of size NxN, where N = # of identified neurons
        rows are predecessors of ith neuron, e.g. ith row is all of the neurons
        connecting TO i. So the sum of values in the ith row is the in-strength
        of i. This orientation is chosen so that the dot product: M * x can be
        done to give the sum of incoming excitations if x is the state vector Nx1.
    """
    pass  # TODO implement


if __name__ == "__main__":
    pass
