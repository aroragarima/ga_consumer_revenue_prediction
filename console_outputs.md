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

#### Top 10s as per Browser category, Device, OS

                    count  count of non-zero revenue          mean
device.browser
Chrome             468400                     468400  1.816349e+06
Safari             125388                     125388  2.581296e+05
Firefox             25617                      25617  2.019140e+06
Internet Explorer   14090                      14090  4.126139e+05
Android Webview     13751                      13751  3.918988e+03
Edge                 8309                       8309  5.524419e+05
Samsung Internet     6282                       6282  2.601719e+04
Opera Mini           5974                       5974  0.000000e+00
Safari (in-app)      5776                       5776  1.833102e+04
Opera                3844                       3844  3.679761e+04

                        count  count of non-zero revenue          mean
device.deviceCategory
desktop                468106                     468106  1.941682e+06
mobile                 188679                     188679  1.648375e+05
tablet                  26360                      26360  2.171096e+05

                         count  count of non-zero revenue          mean
device.operatingSystem
Windows                 247359                     247359  9.601755e+05
Macintosh               175521                     175521  3.116047e+06
Android                 119498                     119498  1.713550e+05
iOS                      88386                      88386  1.797319e+05
Linux                    25566                      25566  1.021596e+06
Chrome OS                20435                      20435  4.834386e+06
(not set)                 4693                       4693  0.000000e+00
Windows Phone              662                        662  3.987915e+04
Samsung                    357                        357  0.000000e+00
Tizen                      288                        288  0.000000e+00
