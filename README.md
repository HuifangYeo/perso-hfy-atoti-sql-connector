# perso-hfy-atoti-sql-connector

Connecting to SQL data source with real-time data polling

This is a simple demonstration of how we can use atoti to analyse sales of medical devices.  
The notebook also shows two different authentication mechanisms that we can integrate with the [Atoti+ plugin](https://docs.atoti.io/latest/lib/atoti-plus/atoti_plus.html#module-atoti_plus).  
Contact [support@atoti.io](mailto:support@atoti.io) if you need more information on Atoti+.  
Alternative, you can comment off the security related codes to run the notebook with Atoti+ plugin.

## Data source

This example uses mock data. Depending on whether you are using the CSV version or SQL connector version of the use case, the data source used is different.

**For CSV example:**
Refer to the data files under the data directory:

- [medical_devices_db.csv](data/medical_devices_db.csv)
- [medical_sales_db.csv](data/medical_sales_db.csv)

**For MS SQL example:**
Use [00_data_generation.ipynb](00_data_generation.ipynb) to generate and upload data into MS-SQL database. Update the database JDBC URL according to your own database setting.

The data is generated using the below data templates:

- [devices_details.csv](data/devices_details.csv)
- [hospital_details.csv](data/hospital_details.csv)
- [medical_device_price_listing.csv](data/medical_device_price_listing.csv)

## Notebooks

Use [01_main_csv.ipynb](01_main_csv.ipynb) to run analysis by consuming CSV data files.

Use [02_main_mssql_realtime.ipynb](02_main_mssql_realtime.ipynb) to run analysis by loading data from MS SQL database into the atoti data cube. This notebooks includes demonstration of:

- Security implementation with basic authentication
- atoti connectivity to SQL database
- real-time dashboarding, polling delta data from the database
- what-if simulation (replace [mockML.py](data/mockML.py) with your own machine learning algorithm to forecast the sales in the next quarter.
- Cumulative trends and YTD/YTM computation

[03_main_LDAP_authentication.ipynb](03_main_LDAP_authentication.ipynb) shows how to connect to an LDAP authentication provider. 