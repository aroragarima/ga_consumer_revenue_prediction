from dependencies import *

def plot_horizontally(x, y, filename):
	plt.figure(figsize=(8,10))
	plt.title(filename)
	sns.barplot(x=x, y=y, orient = "h")
	plt.savefig(filename, dpi=200)
