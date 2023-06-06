import matplotlib.pyplot as plt

def plot_histogram(data, bins=10, title='', xmin=None, xmax=None, xlabel = None):
    plt.hist(data, bins=bins, edgecolor='black')
    plt.title(title)
    if xlabel is not None: 
        plt.xlabel(xlabel)
    else: 
        plt.xlabel("Values")
    plt.ylabel('Frequency')
    if xmin is not None and xmax is not None:
        plt.xlim(xmin, xmax)
    plt.ticklabel_format(style="plain")
    plt.show()
