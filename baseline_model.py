from dependencies import *
from eda import drop_constant_cols

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
        + list(test_df[col].values.astype("str"))
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
    test_df[col] = test_df[col].astype(float)
