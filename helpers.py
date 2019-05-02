from dependencies import *

def plot_horizontally(x, y, filename):
    plt.figure(figsize=(8, 5))
    plt.title(filename)
    sns.barplot(x=x, y=y, orient="h")
    plt.tight_layout()
    plt.savefig("graph_plots/" + filename, bbox_inches="tight", dpi=100)
