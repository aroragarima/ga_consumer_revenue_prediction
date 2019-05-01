from dependencies import *
from eda import drop_constant_cols
from datetime import datetime
import warnings
warnings.filterwarnings("ignore")

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

### creating a new feature space with better and more robust training_features

# training_features['channelGrouping'] = train_df['channelGrouping']
# temp = []
# for i in train_df['date']:
# 	temp.append(i[4:])
# training_features['date'] = pd.Series(temp)

training_features = pd.DataFrame()
training_features['channelGrouping'] = train_df['channelGrouping']

date = []

for i in range(len(train_df)):
	element = train_df['date'][i]
	element = element.astype(str)
	date.append(element[4:])


def return_training_features(attribute):
	temp = []
	for i in range(len(train_df[attribute])):
		element = train_df[attribute][i]
		temp.append(element[4:])
	print(temp)
	return temp

training_features['date'] = date

timestamp = []
for i in range(len(train_df)):
	element = train_df['visitStartTime'][i]
	dt_object = datetime.fromtimestamp(element)
	timestamp.append(dt_object.hour)

training_features['fullVisitorId'] = train_df['fullVisitorId']
training_features['visitStartTime'] = timestamp
training_features['device.browser'] = train_df['device.browser']
training_features['device.deviceCategory'] = train_df['device.deviceCategory']
training_features['geoNetwork.networkDomain'] = train_df['geoNetwork.networkDomain']
training_features['totals.pageviews'] = train_df['totals.pageviews']
training_features['totals.timeOnSite'] = train_df['totals.timeOnSite']
training_features['totals.transactionRevenue'] = train_df['totals.transactionRevenue']
training_features['totals.transactions'] = train_df['totals.transactions']
training_features['trafficSource.adContent'] = train_df['trafficSource.adContent']
training_features['trafficSource.adwordsClickInfo.adNetworkType'] = train_df['trafficSource.adwordsClickInfo.adNetworkType']
training_features['trafficSource.campaign'] = train_df['trafficSource.campaign']
training_features['trafficSource.medium'] = train_df['trafficSource.medium']
training_features['trafficSource.source'] = train_df['trafficSource.source']
