from dependencies import *
from helpers import *

def extract_plots(df):

	list = ['channelGrouping','geoNetwork.city','geoNetwork.continent','geoNetwork.country','geoNetwork.metro','geoNetwork.networkDomain','geoNetwork.region','geoNetwork.subContinent','trafficSource.adContent','trafficSource.adwordsClickInfo.adNetworkType','trafficSource.campaign','trafficSource.isTrueDirect','trafficSource.keyword','trafficSource.medium','trafficSource.referralPath','trafficSource.source']

	for col in list:
		cnt_srs = df.groupby(col)['totals.transactionRevenue'].agg(['size', 'count', 'mean'])
		cnt_srs.columns = ["count", "count of non-zero revenue", "mean"]
		cnt_srs = cnt_srs.sort_values(by="count", ascending=False)[:10]
		print(cnt_srs.head(10))
		plot_horizontally(cnt_srs.iloc[:, 0], cnt_srs.index, '{} -count'.format(col))
		plot_horizontally(cnt_srs.iloc[:, 1], cnt_srs.index, '{} -Non Zero Revenue Count'.format(col))
		plot_horizontally(cnt_srs.iloc[:, 2], cnt_srs.index, '{} -Mean Revenue'.format(col))

	return True
