def plot_horizontally(x, y, filename):
	plt.figure(8,10)
	sns.barplot(x=x, y=y, orient = "h")
	plt.savefig("{}.png".format(filename), dpi=200)
	
