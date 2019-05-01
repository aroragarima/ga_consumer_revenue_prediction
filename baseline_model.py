from dependencies import *
from eda import drop_constant_cols
from datetime import datetime

train_df = pd.read_csv("datafiles/train_sampled_v40perc.csv")

# imputing 0 for missing target values
train_df["totals.transactionRevenue"].fillna(0, inplace=True)
train_df = train_df.drop(["Unnamed: 0"], axis=1)  # serial number column
constant_cols, train_df = drop_constant_cols(train_df)

print(
    "Shape of Training dataframe after dropping constant columns: {}".format(
        train_df.shape
    )
)

train_y = train_df["totals.transactionRevenue"].values
train_id = train_df["fullVisitorId"].values
# label encode the categorical variables and convert the numerical variables to float
cat_cols = [
    "channelGrouping",
    "device.browser",
    "device.deviceCategory",
    "device.operatingSystem",
    "geoNetwork.city",
    "geoNetwork.continent",
    "geoNetwork.country",
    "geoNetwork.metro",
    "geoNetwork.networkDomain",
    "geoNetwork.region",
    "geoNetwork.subContinent",
    "trafficSource.adContent",
    "trafficSource.adwordsClickInfo.adNetworkType",
    "trafficSource.adwordsClickInfo.gclId",
    "trafficSource.adwordsClickInfo.page",
    "trafficSource.adwordsClickInfo.slot",
    "trafficSource.campaign",
    "trafficSource.keyword",
    "trafficSource.medium",
    "trafficSource.referralPath",
    "trafficSource.source",
    "trafficSource.adwordsClickInfo.isVideoAd",
    "trafficSource.isTrueDirect",
]

for col in cat_cols:
    print(col)
    lbl = preprocessing.LabelEncoder()
    lbl.fit(
        list(train_df[col].values.astype("str"))
    )
    train_df[col] = lbl.transform(list(train_df[col].values.astype("str")))
    num_cols = [
        "totals.hits",
        "totals.pageviews",
        "visitNumber",
        "visitStartTime",
        "totals.bounces",
        "totals.newVisits",
    ]
for col in num_cols:
    train_df[col] = train_df[col].astype(float)

### creating a new feature space with better and more robust features

# features['channelGrouping'] = train_df['channelGrouping']
# temp = []
# for i in train_df['date']:
# 	temp.append(i[4:])
# features['date'] = pd.Series(temp)

features = pd.DataFrame()
features['channelGrouping'] = train_df['channelGrouping']

date = []

for i in range(len(train_df)):
	element = train_df['date'][i]
	element = element.astype(str)
	date.append(element[4:])


def return_features(attribute):
	temp = []
	for i in range(len(train_df[attribute])):
		element = train_df[attribute][i]
		temp.append(element[4:])
	print(temp)
	return temp

features['date'] = date

timestamp = []
for i in range(len(train_df)):
	element = train_df['visitStartTime'][i]
	dt_object = datetime.fromtimestamp(element)
	timestamp.append(dt_object.hour)

features['fullVisitorId'] = train_df['fullVisitorId']
features['visitStartTime'] = timestamp
features['device.browser'] = train_df['device.browser']
features['device.deviceCategory'] = train_df['device.deviceCategory']
features['geoNetwork.networkDomain'] = train_df['geoNetwork.networkDomain']
features['totals.pageviews'] = train_df['totals.pageviews']
features['totals.timeOnSite'] = train_df['totals.timeOnSite']
features['totals.transactionRevenue'] = train_df['totals.transactionRevenue']
features['totals.transactions'] = train_df['totals.transactions']
features['trafficSource.adContent'] = train_df['trafficSource.adContent']
features['trafficSource.adwordsClickInfo.adNetworkType'] = train_df['trafficSource.adwordsClickInfo.adNetworkType']
features['trafficSource.campaign'] = train_df['trafficSource.campaign']
features['trafficSource.medium'] = train_df['trafficSource.medium']
features['trafficSource.source'] = train_df['trafficSource.source']
