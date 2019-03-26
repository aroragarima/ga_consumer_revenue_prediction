from dependencies import *
from helpers import *

train_df = pd.read_csv("datafiles/train_sampled_v40perc.csv")
print("Shape of input datafile: {}".format(train_df.shape))

def target_variable_exploration(df):
	df["totals.transactionRevenue"] = df["totals.transactionRevenue"].astype('float')
	gdf = df.groupby("fullVisitorId")["totals.transactionRevenue"].sum().reset_index()

	#TODO: define a helper function for plotting graphs

	plt.figure(figsize=(8,6))
	plt.scatter(range(gdf.shape[0]), np.sort(np.log1p(gdf["totals.transactionRevenue"].values)))
	plt.xlabel('index', fontsize=12)
	plt.ylabel('TransactionRevenue', fontsize=12)
	plt.savefig("target_variable_exploration.png")

def drop_constant_cols(df):
	constant_cols = [c for c in df.columns if df[c].nunique(dropna=False)==1 ]
	df = df.drop(constant_cols, axis = 1)
	return constant_cols, df

target_variable_exploration(train_df)
cols, train_df = drop_constant_cols(train_df)

# imputing 0 for missing target values
# train_df['totals.transactionRevenue'].fillna(0, inplace=True)

print("Shape of Training dataframe after dropping constant columns: {}".format(train_df.shape))

# Browser Category
# cnt_srs = train_df.groupby('device.browser')['totals.transactionRevenue'].agg(['size', 'count', 'mean'])
# cnt_srs.columns = ["count", "count of non-zero revenue", "mean"]
# cnt_srs = cnt_srs.sort_values(by="count", ascending=False)[:10]
# print(cnt_srs.head(10))
# plot_horizontally(cnt_srs.iloc[:, 0], cnt_srs.index, 'Browser Category -count')
# plot_horizontally(cnt_srs.iloc[:, 1], cnt_srs.index, 'Browser Category -Non Zero Revenue Count')
# plot_horizontally(cnt_srs.iloc[:, 2], cnt_srs.index, 'Browser Category -Mean Revenue')

l = ['device.browser', 'device.deviceCategory', 'device.operatingSystem', 'channelGrouping',
	'geoNetwork.city','geoNetwork.continent','geoNetwork.country','geoNetwork.metro','geoNetwork.networkDomain',
	'geoNetwork.region','geoNetwork.subContinent','trafficSource.adContent',
	'trafficSource.adwordsClickInfo.adNetworkType','trafficSource.campaign','trafficSource.isTrueDirect',
	'trafficSource.keyword','trafficSource.medium','trafficSource.referralPath','trafficSource.source']

graphing = ['device.browser', 'device.operatingSystem', 'geoNetwork.continent', 'geoNetwork.networkDomain', 
		'trafficSource.source']

def extract_plots(df, top, l):

	for col in l:
		name = col.replace(".", " ")
		print(name)
		cnt_srs = df.groupby(col)['totals.transactionRevenue'].agg(['size', 'count', 'mean'])
		cnt_srs.columns = ["count", "count of non-zero revenue", "mean"]
		cnt_srs = cnt_srs.sort_values(by="count", ascending=False)[:top]
		print(cnt_srs.head(top))
		plot_horizontally(cnt_srs.iloc[:, 0], cnt_srs.index, '{} -count'.format(name))
		plot_horizontally(cnt_srs.iloc[:, 1], cnt_srs.index, '{} -Non Zero Revenue Count'.format(name))
		plot_horizontally(cnt_srs.iloc[:, 2], cnt_srs.index, '{} -Mean Revenue'.format(name))

	return True

extract_plots(train_df, 10, graphing)

extract_plots(train_df, 60, ['totals.hits', 'totals.pageviews'])
