from driver import *
from constructor import *
import matplotlib.pyplot as plt
import io
import base64

driver_data = [sublist[0] for sublist in get_drivers(connection)]
constructor_data = [sublist[0] for sublist in get_constructors(connection)]


def plot_graph(data):
    plt.figure()
    for li in data:
        plt.plot(li)
    plt.axis((0, 24, 0, 400))

    # save the plot to a buffer
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()
    buffer.seek(0)

    # convert to a base64 string
    image = buffer.getvalue()
    buffer.close()
    image_base64 = base64.b64encode(image).decode('utf-8')

    # return the image of the plot
    return image_base64


