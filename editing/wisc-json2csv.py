# convert from JSON to CSV

import csv
import json
import os
import pandas as pd

json_path = r"wisc"	# point to path
csv_name = "output.csv"	# name for csv

dataset = []	# empty list

# through all items, format and append to dataset list
for path, dir, files in os.walk(json_path):
    for filename in files:
    	if filename.endswith(".json"):
            file_path = os.path.join(path, filename)
            json_file_open = open(file_path, 'rb')
            data = json_file_open.read().decode('utf-8', errors='ignore')
            loaded = json.loads(data)
            dataset.append(loaded)
            


df = pd.DataFrame(dataset)		# convert dataset into dataframe

# return the first value of a multivalued cell;this removes the []
df['dc_creator_sm']=df['dc_creator_sm'].str[0]
df['dc_subject_sm']=df['dc_subject_sm'].str[0]

# remove brackets from Temporal which is a mix of single values and lists; this might fail in other cases
df['dct_temporal_sm']=df['dct_temporal_sm'].str.join('')

# Split solr_geom coordinates and reorder from WENS to WSEN
df[['w', 'e','n','s']] = df['solr_geom'].str.strip('ENVELOPE()').str.split(',', expand=True)
df['Bounding Box'] = df[['w', 's','e','n']].agg(', '.join, axis=1) 

#Convert Geometry Type to Resource Type value
df['Resource Type'] = df['layer_geom_type_s'].astype(str) + ' data'

# Create Date Range field
df['Date Range'] = df['dct_temporal_sm'].astype(str) +'-' + df['dct_temporal_sm'].astype(str) 




# df['dct_references_s'] = df['dct_references_s'].str.split(',', expand=True)

# Remove unnecessary columns
df = df.drop(columns=['geoblacklight_version','layer_modified_dt', 'thumbnail_path_ss','w','e','n','s', 'layer_id_s','solr_year_i','layer_geom_type_s','solr_geom'])


df = df.rename(columns={
'dc_title_s': 'Title', 
'dc_description_s': 'Description',
'dc_creator_sm': 'Creator',
'dct_issued_s': 'Date Issued',
'dc_rights_s' : 'Access Rights',
'dc_format_s': 'Format',
'layer_slug_s' : 'ID',
'dc_identifier_s' : 'Identifier',
'dc_language_s' : 'Language',
'dct_provenance_s' : 'Provider',
'dc_publisher_s' : 'Publisher',
'dc_publisher_sm' : 'Publisher',
'dc_source_sm' : 'Source',
'dct_spatial_sm' : 'Spatial Coverage',
'dc_subject_sm' : 'Subject',
'dct_temporal_sm' : 'Temporal Coverage',
})

df['Creator']=df['Creator'].str.strip('[]')

df.to_csv("{}.csv".format(csv_name))