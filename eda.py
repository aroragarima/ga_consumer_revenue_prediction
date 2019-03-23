from dependencies import *

train_df = pd.read_csv("datafiles/train_sampled_v40perc.csv")

def target_variable_exploration(df):
	df["totals.transactionRevenue"] = df["totals.transactionRevenue"].astype('float')
	gdf = df.groupby("fullVisitorId")["totals.transactionRevenue"].sum().reset_index()

	#TODO: define a helper function for plotting graphs

	plt.figure(figsize=(8,6))
	plt.scatter(range(gdf.shape[0]), np.sort(gdf["totals.transactionRevenue"].values))
	plt.xlabel('index', fontsize=12)
	plt.ylabel('TransactionRevenue', fontsize=12)
	plt.show()
	plt.savefig(("target_variable_exploration_sans_log.png"))

target_variable_exploration(train_df)
