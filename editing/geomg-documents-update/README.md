# GEOMG Document Update
The `update.ipynb` is a script aims to modify fields' values on GEOMG via python. We used to **download CSV files -> modify values locally -> upload again** to modify a large number of datasets, or **open each dataset page -> modify values -> update and open next data page** to modify datasets one by one. However, this repository offers you a third method for GEOMG document updates.


## Getting Started
### Prerequisites
Store updated **values** with **field names** in a local CSV file under the same directory. **Field name** here refers to the name attribute of the input tag in HTML file. 
```html
<input class="..." type="text" name="document[title]" value="..." id="...">
```
*For example, the name attribute for the input tag above is `document[title]`, which is corresponding to the `Title` field. Check [lookup tables](##Lookup-Table) below to get the name for each field.*

First row should be **field names**, and the first column should be **IDs** for each document. Here's an example for a CSV:
![CSV Example](/image/sample.png)

### Installation
There are three Python modules/packages used in the script. Make sure you have them successfully installed.
```python
import time
import csv
import mechanize
```

 If any package is missing, try the following statement for installation, for example: 
```bash
pip install mechanize
```
### Execute the script
Before running the script, here are two manual changes for you to modify.


- **Change the directory of your CSV file.**
```python
csv_file = "<directory of your CSV file>"
```
- **Edit the `username` and `password` for your own ones**
```python
username = "<your_username>"
password = "<your_password>"
```

## Lookup Table
The following tables offer you a quick lookup for the `name attribute` of each `field`. 

#### Identification
|             | Field              | Name attr.                                  | Control Type | Format    |
| :---------- | :----------------- | :------------------------------------------ | :----------- | :-------- |
| Descriptive | Title              | document[title]                             |              |           |
|             | Alternative Title  | document[dct_alternative_sm_attributes][]   |              |           |
|             | Description        | document[dct_description_sm_attributes][]   |              |           |
|             | Language           | document[dct_language_sm_attributes][]      |              |           |
| Credits     | Creator            | document[dct_creator_sm_attributes][]       |              |           |
|             | Publisher          | document[dct_publisher_sm_attributes][]     |              |           |
|             | Provider           | document[schema_provider_s]                 |              |           |
| Categories  | Resource Class     | document[gbl_resourceClass_sm_attributes][] |              |           |
|             | Resource Type      | document[gbl_resourceType_sm_attributes][]  |              |           |
|             | Subject            | document[dct_subject_sm_attributes][]       |              |           |
|             | ISO Topic Category | document[dcat_theme_sm_attributes][]        |              |           |
|             | Keyword            | document[dcat_keyword_sm_attributes][]      |              |           |
| Temporal    | Temporal Coverage  | document[dct_temporal_sm_attributes][]      |              |           |
|             | Date Issued        | document[dct_issued_s]                      |              | YYYY      |
|             | Date range         | document[gbl_dateRange_drsim_attributes][]  |              | YYYY-YYYY |
| Spatial     | Spatial Coverage   | document[dct_spatial_sm_attributes][]       |              |           |
|             | Bounding Box       | document[locn_geometry]                     |              | W,S,E,N   |
|             | GeoNames           | document[b1g_geonames_sm_attributes][]      |              |           |
| Relations   | Relation           | document[dct_relation_sm_attributes][]      |              |           |
|             | Member Of          | document[pcdm_memberOf_sm_attributes][]     |              |           |
|             | Is Part Of         | document[dct_isPartOf_sm_attributes][]      |              |           |
|             | Source             | document[dct_source_sm_attributes][]        |              |           |
|             | Version            | document[dct_isVersionOf_sm_attributes][]   |              |           |
|             | Replaces           | document[dct_replaces_sm_attributes][]      |              |           |
|             | Is Replace By      | document[dct_isReplacedBy_sm_attributes][]  |              |           |

#### Distribution
|        | Field              | Name attr.                                             | Control Type | Format |
| :----- | :----------------- | :----------------------------------------------------- | :----------- | :----- |
| Object | Format             | document[dct_format_s]                                 |              |        |
|        | File Size          | document[gbl_fileSize_s]                               |              |        |
|        | WxS Identifier     | document[gbl_wxsIdentifier_s]                          |              |        |
|        | Georeferenced      | document[gbl_georeferenced_b]                          |              |        |
| Links  | Reference Category | document[dct_references_s_attributes][index][category] |              |        |
|        | Reference Value    | document[dct_references_s_attributes][index][value]    |              |        |
|        | B1G Image URL      | document[b1g_image_ss]                                 |              |        |

#### Administrative
|               | Field               | Name attr.                                    | Control Type | Format |
| :------------ | :------------------ | :-------------------------------------------- | :----------- | :----- |
| Codes         | ID                  | document[geomg_id_s]                          |              |        |
|               | Identifier          | document[dct_identifier_sm_attributes][]      |              |        |
|               | Code                | document[b1g_code_s]                          |              |        |
| Rights        | Access Rights       | document[dct_accessRights_s]                  |              |        |
|               | Right Holder        | document[dct_rightsHolder_sm_attributes][]    |              |        |
|               | License             | document[dct_license_sm_attributes][]         |              |        |
|               | Rights              | document[dct_rights_sm_attributes][]          |              |        |
| Life Cycle    | Accrual Method      | document[b1g_dct_accrualMethod_s]             |              |        |
|               | Accrual Periodicity | document[b1g_dct_accrualPeriodicity_s]        |              |        |
|               | Date Accessioned    | document[b1g_dateAccessioned_sm_attributes][] |              |        |
|               | Date Retired        | document[b1g_dateRetired_s]                   |              |        |
|               | Status              | document[b1g_status_s]                        |              |        |
|               | Publication State   | document[publication_state]                   |              |        |
| Accessibility | Gbl suppressed b    | document[gbl_suppressed_b]                    |              |        |
|               | Child Record        | document[b1g_child_record_b]                  |              |        |
|               | Mediator            | document[b1g_dct_mediator_sm_attributes][]    |              |        |
|               | Access              | document[b1g_access_s]                        |              |        |




## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Credit
Originally created by **Gene Cheng** [@Ziiiiing](https://github.com/Ziiiiing) on **Oct 3, 2021**