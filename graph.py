from driver import *
from constructor import *
import matplotlib.pyplot as plt
import random

driver_data = [sublist[0] for sublist in get_drivers(connection)]
constructor_data = [sublist[0] for sublist in get_constructors(connection)]


def plot_graph(data):
    print(data)
    plt.figure()
    for li in data:
        plt.plot(li)
    plt.axis((0, 24, 0, 400))
    plt.show()

