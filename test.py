def neuron(x, w, b):
    """
    Compute the output of a single neuron given the input x, the weight w and the bias b.
    """
    return max(0, w*x+b)