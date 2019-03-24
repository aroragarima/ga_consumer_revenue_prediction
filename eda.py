from dependencies import *

train_df = pd.read_csv("datafiles/train_sampled_v40perc.csv")

def target_variable_exploration(df):
	df["totals.transactionRevenue"] = df["totals.transactionRevenue"].astype('float')
	gdf = df.groupby("fullVisitorId")["totals.transactionRevenue"].sum().reset_index()

	#TODO: define a helper function for plotting graphs

	plt.figure(figsize=(8,6))
	plt.scatter(range(gdf.shape[0]), np.sort(np.log1p(gdf["totals.transactionRevenue"].values)))
	plt.xlabel('index', fontsize=12)
	plt.ylabel('TransactionRevenue', fontsize=12)
	plt.show()
	plt.savefig(("target_variable_exploration.png"))

def find_constant_cols(df):
	constant_cols = [c for c in df.columns if df[c].nunique(dropna=False)==1 ]
	return constant_cols

target_variable_exploration(train_df)

cols = find_constant_cols(train_df)

# imputing 0 for missing target values
train_df['totals.transactionRevenue'].fillna(0, inplace=True)

# Browser Category
cnt_srs = train_df.groupby('device.browser')['totals.transactionRevenue'].agg(['size', 'count', 'mean'])
cnt_srs.columns = ["count", "count of non-zero revenue", "mean"]
cnt_srs = cnt_srs.sort_values(by="count", ascending=False)
print(cnt_srs.head(10))

# Device Category
cnt_srs = train_df.groupby('device.deviceCategory')['totals.transactionRevenue'].agg(['size', 'count', 'mean'])
cnt_srs.columns = ["count", "count of non-zero revenue", "mean"]
cnt_srs = cnt_srs.sort_values(by="count", ascending=False)
print(cnt_srs.head(10))

# Operating system
cnt_srs = train_df.groupby('device.operatingSystem')['totals.transactionRevenue'].agg(['size', 'count', 'mean'])
cnt_srs.columns = ["count", "count of non-zero revenue", "mean"]
cnt_srs = cnt_srs.sort_values(by="count", ascending=False)
print(cnt_srs.head(10))
