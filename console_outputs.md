# Feature Discription:

##### channelGrouping
The channel via which the user came to the Store.
##### date
The date on which the user visited the Store.
##### device 
The specifications for the device used to access the Store.
##### geoNetwork 
This section contains information about the geography of the user.
##### socialEngagementType 
Engagement type, either "Socially Engaged" or "Not Socially Engaged".
##### totals 
This section contains aggregate values across the session.
##### trafficSource 
This section contains information about the Traffic Source from which the session originated.
##### visitId 
An identifier for this session. This is part of the value usually stored as the _utmb cookie. This is only unique to the user. For a completely unique ID, you should use a combination of fullVisitorId and visitId.
##### visitNumber 
The session number for this user. If this is the first session, then this is set to 1.
##### visitStartTime 
The timestamp (expressed as POSIX time).
##### hits 
This row and nested fields are populated for any and all types of hits. Provides a record of all page visits.
##### customDimensions 
This section contains any user-level or session-level custom dimensions that are set for a session. This is a repeated field and has an entry for each dimension that is set.
##### totals 
This set of columns mostly includes high-level aggregate data.

# Results

Number of unique customers with non-zero revenue :  7204 and the ratio is :  0.011865819390501416

Shape of input datafile: (683145, 60) sampled from 1708337x13 records file

#### Normalising JSON column 'geoNetwork' 
| 0 | {"continent": "Europe", "subContinent": "Western Europe", "country": "Germany", "region": "not available in demo dataset", "metro": "not available in demo dataset", "city": "not available in demo dataset", "cityId": "not available in demo dataset", "networkDomain": "(not set)", "latitude": "not available in demo dataset", "longitude": "not available in demo dataset", "networkLocation": "not available in demo dataset"}                     |
|---|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1 | {"continent": "Americas", "subContinent": "Northern America", "country": "United States", "region": "California", "metro": "San Francisco-Oakland-San Jose CA", "city": "Cupertino", "cityId": "not available in demo dataset", "networkDomain": "(not set)", "latitude": "not available in demo dataset", "longitude": "not available in demo dataset", "networkLocation": "not available in demo dataset"}                                              |
| 2 | {"continent": "Americas", "subContinent": "Northern America", "country": "United States", "region": "not available in demo dataset", "metro": "not available in demo dataset", "city": "not available in demo dataset", "cityId": "not available in demo dataset", "networkDomain": "windjammercable.net", "latitude": "not available in demo dataset", "longitude": "not available in demo dataset", "networkLocation": "not available in demo dataset"} |
| 3 | {"continent": "Asia", "subContinent": "Western Asia", "country": "Turkey", "region": "not available in demo dataset", "metro": "not available in demo dataset", "city": "not available in demo dataset", "cityId": "not available in demo dataset", "networkDomain": "unknown.unknown", "latitude": "not available in demo dataset", "longitude": "not available in demo dataset", "networkLocation": "not available in demo dataset"}                    |

|   | geoNetwork.city               | geoNetwork.cityId             | geoNetwork.continent | geoNetwork.country | geoNetwork.latitude           | geoNetwork.longitude          | geoNetwork.metro                  | geoNetwork.networkDomain | geoNetwork.networkLocation    | geoNetwork.region             | geoNetwork.subContinent |
|---|-------------------------------|-------------------------------|----------------------|--------------------|-------------------------------|-------------------------------|-----------------------------------|--------------------------|-------------------------------|-------------------------------|-------------------------|
| 0 | Cupertino                     | not available in demo dataset | Americas             | United States      | not available in demo dataset | not available in demo dataset | San Francisco-Oakland-San Jose CA | (not set)                | not available in demo dataset | California                    | Northern America        |
| 1 | London                        | not available in demo dataset | Europe               | United Kingdom     | not available in demo dataset | not available in demo dataset | London                            | (not set)                | not available in demo dataset | England                       | Northern Europe         |
| 2 | not available in demo dataset | not available in demo dataset | Europe               | Denmark            | not available in demo dataset | not available in demo dataset | not available in demo dataset     | fullrate.ninja           | not available in demo dataset | not available in demo dataset | Northern Europe         |
| 3 | Mexico City                   | not available in demo dataset | Americas             | Mexico             | not available in demo dataset | not available in demo dataset | (not set)                         | uninet-ide.com.mx        | not available in demo dataset | Mexico City                   | Central America         |
| 4 | not available in demo dataset | not available in demo dataset | Europe               | Netherlands        | not available in demo dataset | not available in demo dataset | not available in demo dataset     | (not set)                | not available in demo dataset | not available in demo dataset | Western Europe          |
| 5 | not available in demo dataset | not available in demo dataset | Europe               | United Kingdom     | not available in demo dataset | not available in demo dataset | not available in demo dataset     | unknown.unknown          | not available in demo dataset | not available in demo dataset | Northern Europe         |
| 6 | not available in demo dataset | not available in demo dataset | Europe               | Sweden             | not available in demo dataset | not available in demo dataset | not available in demo dataset     | gavlenet.com             | not available in demo dataset | not available in demo dataset | Northern Europe         |
| 7 | not available in demo dataset | not available in demo dataset | Europe               | United Kingdom     | not available in demo dataset | not available in demo dataset | not available in demo dataset     | virginm.net              | not available in demo dataset | not available in demo dataset | Northern Europe         |
| 8 | not available in demo dataset | not available in demo dataset | Asia                 | India              | not available in demo dataset | not available in demo dataset | not available in demo dataset     | (not set)                | not available in demo dataset | not available in demo dataset | Southern Asia           |
| 9 | not available in demo dataset | not available in demo dataset | Europe               | United Kingdom     | not available in demo dataset | not available in demo dataset | not available in demo dataset     | virginm.net              | not available in demo dataset | not available in demo dataset | Northern Europe         |

	geoNetwork after flattening split into 11 attributes

#### Top 10s as per Browser category, Device, OS

| device.browser    | count  | count of non-zero revenue | mean               |
|-------------------|--------|---------------------------|--------------------|
| Chrome            | 468400 | 468400                    | 1816349.3381725021 |
| Safari            | 125388 | 125388                    | 258129.6455801193  |
| Firefox           | 25617  | 25617                     | 2019140.024202678  |
| Internet Explorer | 14090  | 14090                     | 412613.9105748758  |
| Android Webview   | 13751  | 13751                     | 3918.9877099847286 |
| Edge              | 8309   | 8309                      | 552441.9304368757  |
| Samsung Internet  | 6282   | 6282                      | 26017.191977077364 |
| Opera Mini        | 5974   | 5974                      | 0.0                |
| Safari (in-app)   | 5776   | 5776                      | 18331.02493074792  |
| Opera             | 3844   | 3844                      | 36797.60665972945  |

| device.deviceCategory | count  | count of non-zero revenue | mean               |
|-----------------------|--------|---------------------------|--------------------|
| desktop               | 468106 | 468106                    | 1941681.8840177224 |
| mobile                | 188679 | 188679                    | 164837.52828878677 |
| tablet                | 26360  | 26360                     | 217109.6358118361  |

| device.operatingSystem | count  | count of non-zero revenue | mean               |
|------------------------|--------|---------------------------|--------------------|
| Windows                | 247359 | 247359                    | 960175.5343448187  |
| Macintosh              | 175521 | 175521                    | 3116047.082685263  |
| Android                | 119498 | 119498                    | 171355.0017573516  |
| iOS                    | 88386  | 88386                     | 179731.85798655896 |
| Linux                  | 25566  | 25566                     | 1021596.2606586873 |
| Chrome OS              | 20435  | 20435                     | 4834386.1022755075 |
| (not set)              | 4693   | 4693                      | 0.0                |
| Windows Phone          | 662    | 662                       | 39879.15407854985  |
| Samsung                | 357    | 357                       | 0.0                |
| Tizen                  | 288    | 288                       | 0.0                |

#### List of constant columns
* socialEngagementType
* device.browserSize 
* device.browserVersion 
* device.flashVersion 
* device.language 
* device.mobileDeviceBranding 
* device.mobileDeviceInfo 
* device.mobileDeviceMarketingName 
* device.mobileDeviceModel 
* device.mobileInputSelector 
* device.operatingSystemVersion 
* device.screenColors 
* device.screenResolution 
* geoNetwork.cityId 
* geoNetwork.latitude 
* geoNetwork.longitude 
* geoNetwork.networkLocation 
* totals.visits 
* trafficSource.adwordsClickInfo.criteriaParameters

Resultant df has now got 41 columns
Shape of Training dataframe after dropping constant columns: (683145, 41)
