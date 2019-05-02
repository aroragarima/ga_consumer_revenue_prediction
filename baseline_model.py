from dependencies import *
from eda import drop_constant_cols
from datetime import datetime
import warnings
warnings.filterwarnings("ignore")
from sklearn import metrics

# train_df = pd.read_csv("datafiles/train_sampled_v40perc.csv")
train_df = pd.read_csv("train_all.csv")
test_df = pd.read_csv("datafiles/test_v2.csv")
# test_df = pd.read_csv("datafiles/test_flat.csv")

# imputing 0 for missing target values
train_df["totals.transactionRevenue"].fillna(0, inplace=True)
train_df = train_df.drop(["Unnamed: 0"], axis=1)  # serial number column
constant_cols, train_df = drop_constant_cols(train_df)
# train_df = train_df.drop(['sessionId'], axis=1) # attribute absent in test set

constant_cols, test_df = drop_constant_cols(test_df)

print(
    "Shape of Training dataframe after dropping constant columns: {}".format(
        train_df.shape
    )
)

train_y = train_df["totals.transactionRevenue"].values
train_id = train_df["fullVisitorId"].values
test_id = test_df["fullVisitorId"].values
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
    lbl.fit(list(train_df[col].values.astype('str')) + list(test_df[col].values.astype('str')))
    train_df[col] = lbl.transform(list(train_df[col].values.astype('str')))
    test_df[col] = lbl.transform(list(test_df[col].values.astype('str')))

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
    test_df[col] = test_df[col].astype(float)

### creating a new feature space with better and more robust training_features

# training_features['channelGrouping'] = train_df['channelGrouping']
# temp = []
# for i in train_df['date']:
# 	temp.append(i[4:])
# training_features['date'] = pd.Series(temp)

training_features = pd.DataFrame()
training_features['channelGrouping'] = train_df['channelGrouping']

# date = []

#for i in range(len(train_df)):
#	element = train_df['date'][i]
#	element = element.astype(str)
#	date.append(element[4:])


def return_training_features(attribute):
	temp = []
	for i in range(len(train_df[attribute])):
		element = train_df[attribute][i]
		temp.append(element[4:])
	print(temp)
	return temp

#training_features['date'] = date
training_features['date'] = train_df['date']
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
training_features['geoNetwork.continent'] = train_df['geoNetwork.continent']
training_features['geoNetwork.country'] = train_df['geoNetwork.country']
training_features['totals.pageviews'] = train_df['totals.pageviews']
training_features['totals.timeOnSite'] = train_df['totals.timeOnSite']
training_features['totals.transactionRevenue'] = train_df['totals.transactionRevenue']
training_features['totals.transactions'] = train_df['totals.transactions']
training_features['trafficSource.adContent'] = train_df['trafficSource.adContent']
training_features['trafficSource.adwordsClickInfo.adNetworkType'] = train_df['trafficSource.adwordsClickInfo.adNetworkType']
training_features['trafficSource.campaign'] = train_df['trafficSource.campaign']
training_features['trafficSource.medium'] = train_df['trafficSource.medium']
training_features['trafficSource.source'] = train_df['trafficSource.source']

feature_list = [x for x in training_features.columns]

# Model data fitting
# Split the train dataset into development and validation sets based on time
dev_df = training_features[training_features['date']<=datetime.date(2017,5,31)]
val_df = training_features[training_features['date']>datetime.date(2017,5,31)]
dev_y = np.log1p(dev_df["totals.transactionRevenue"].values)
val_y = np.log1p(v["totals.transactionRevenue"].values)

dev_X = dev_df[feature_list]
val_X = val_df[feature_list]
test_X = test_df[feature_list]

# custom function to run light gbm model
def run_lgb(train_X, train_y, val_X, val_y, test_X):
    params = {
        "objective" : "regression",
        "metric" : "rmse",
        "num_leaves" : 30,
        "min_child_samples" : 100,
        "learning_rate" : 0.1,
        "bagging_fraction" : 0.7,
        "feature_fraction" : 0.5,
        "bagging_frequency" : 5,
        "bagging_seed" : 2018,
        "verbosity" : -1
    }

    lgtrain = lgb.Dataset(train_X, label=train_y)
    lgval = lgb.Dataset(val_X, label=val_y)
    model = lgb.train(params, lgtrain, 1000, valid_sets=[lgval], early_stopping_rounds=100, verbose_eval=100)

    pred_test_y = model.predict(test_X, num_iteration=model.best_iteration)
    pred_val_y = model.predict(val_X, num_iteration=model.best_iteration)
    return pred_test_y, model, pred_val_y

# Training the model #
pred_test, model, pred_val = run_lgb(dev_X, dev_y, val_X, val_y, test_X)

pred_val[pred_val<0] = 0
val_pred_df = pd.DataFrame({"fullVisitorId":val_df["fullVisitorId"].values})
val_pred_df["transactionRevenue"] = val_df["totals.transactionRevenue"].values

val_pred_df["PredictedRevenue"] = np.expm1(pred_val)
#print(np.sqrt(metrics.mean_squared_error(np.log1p(val_pred_df["transactionRevenue"].values), np.log1p(val_pred_df["PredictedRevenue"].values))))
val_pred_df = val_pred_df.groupby("fullVisitorId")["transactionRevenue", "PredictedRevenue"].sum().reset_index()
print(np.sqrt(metrics.mean_squared_error(np.log1p(val_pred_df["transactionRevenue"].values), np.log1p(val_pred_df["PredictedRevenue"].values))))

sub_df = pd.DataFrame({"fullVisitorId":test_id})
pred_test[pred_test<0] = 0
sub_df["PredictedLogRevenue"] = np.expm1(pred_test)
sub_df = sub_df.groupby("fullVisitorId")["PredictedLogRevenue"].sum().reset_index()
sub_df.columns = ["fullVisitorId", "PredictedLogRevenue"]
sub_df["PredictedLogRevenue"] = np.log1p(sub_df["PredictedLogRevenue"])
sub_df.to_csv("baseline_lgb.csv", index=False)
