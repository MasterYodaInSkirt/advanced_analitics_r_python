import tabpy_client
import numpy as np

client = tabpy_client.Client('http://localhost:9004/')


def multiply(x, y):
    return np.sum(x, y).tolist()


client.deploy('multiply', multiply, 'Multiples two numbers x and y')
