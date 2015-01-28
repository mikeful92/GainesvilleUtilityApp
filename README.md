# GainesvilleUtilityApp
Find the utility consumption of any house in gainesville.

Version 0.0.1

Link to the CSV file directly off the Gainesville Data portal: (It is ~300MB)
https://data.cityofgainesville.org/api/views/gk3k-9435/rows.csv?accessType=DOWNLOAD

Gainesville Open Data Portal:
https://data.cityofgainesville.org

Needed modules:
-csv
-prettytable

Both should be easy to download wiht the command:
pip install csv
pip install prettytable

Once you have the code, the csv file and the modules you should be good to go.

There is currently a bug in the code. If the address is missing any months, it can cause pretty tables to crash. I have made a quick workaround that inputs empty variables to get to 12 months. First thing in my to do list is to fix this. 

Let me know if you have any questions.
