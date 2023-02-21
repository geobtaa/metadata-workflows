# convert from xml to CSV
# requires pandas_read_xml module
## not really working


import csv
import json
import os
import pandas as pd
import pandas_read_xml as pdx
import numpy as np

xml_path = r"illinois"	# point to path
csv_name = "pandas-output.csv"	# name for csv

dataset = []	# empty list

# through all items, format and append to dataset list
for path, dir, files in os.walk(xml_path):
    for filename in files:
    	if filename.endswith(".xml"):
            file_path = os.path.join(path, filename)
            xml_file_open = open(file_path, 'rb')
            data = xml_file_open.read().decode('utf-8', errors='ignore')
            loaded = pdx.read_xml(data)
            dataset.append(loaded)


df = pd.DataFrame(np.concatenate(dataset))		# convert dataset into dataframe

df.to_csv("{}.csv".format(csv_name))