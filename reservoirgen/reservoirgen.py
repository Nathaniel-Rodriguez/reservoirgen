import numpy as np
from functools import partial


class Distribution(np.random.RandomState):
    """
    A sub-class around random state that is specialized to a specific
    distribution. The user can pick from the distribution methods available
    to RandomState and provide arguments to it while leaving out any they
    wish to specify at call time.

    When called, the Distribution object will generate random values as a numpy
    array.
    """

    def __init__(self, distribution, distribution_args, *args, **kwargs):
        """
        :param distribution: string of one of the methods available to RandomState
        :param distribution_args: dictionary of argument/value pairs
        :param args: any other RandomState initialization arguments
        :param kwargs: any other RandomState keyword arguments
        """
        super().__init__(*args, **kwargs)
        self.partial_distribution = partial(getattr(self, distribution),
                                            **distribution_args)

    def __call__(self, *args, **kwargs):
        """
        :param kwargs: Any positional or keyword arguments NOT provided at
            initialization.
        :return: numpy array of random values generated from the distribution.
        """
        return self.partial_distribution(*args, **kwargs)


def generate_reservoir_from_edge_list(graph, distribution, sparse=False):
    """
    Generates a weighted reservoir from an unweighted network. The network
    can be expressed as an edge list
    :param graph: a Ex2 numpy edge list
    :param distribution: a distribution that can be called with a shape parameter
        e.g.: random_values = distribution(shape)
    :return:
    """



def generate_reservoir_from_matrix(graph, distribution, sparse=False):


def generate_reservoir_from_nx_graph(graph, distribution, sparse=False):


if __name__ == "__main__":
    pass
