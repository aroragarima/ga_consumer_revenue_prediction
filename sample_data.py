# from dependencies import *

import pandas as pd
import json
from pandas.io.json import json_normalize

# required for increasing the field size
import os
import csv
import random

# csv.field_size_limit(sys.maxsize)

columns = ["device", "geoNetwork", "totals", "trafficSource"]  # json columns

dir_path = "datafiles/"
# p = 0.25
p = 1

def json_read(df):

    data_frame = dir_path + df

    df = pd.read_csv(
        data_frame,
        converters={column: json.loads for column in columns},
        dtype={"fullVisitorId": "str"},
        skiprows=lambda i: i > 0 and random.random() > p,
    )

    for column in columns:
        column_as_df = json_normalize(df[column])
        column_as_df.columns = [
            f"{column}.{subcolumn}" for subcolumn in column_as_df.columns
        ]
        df = df.drop(column, axis=1).merge(
            column_as_df, right_index=True, left_index=True
        )

    print(f"Loaded {os.path.basename(data_frame)}. Shape: {df.shape}")
    return df


if __name__ == '__main__':
	sampled_data = json_read("test_v2.csv")
	sampled_data.to_csv(r"test_sampled.csv")
