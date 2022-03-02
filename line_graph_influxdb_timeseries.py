from datetime import datetime
import os

#from influxdb import InfluxDBClient

import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS


# You can generate an API token from the "API Tokens Tab" in the UI
token = "29ZCFBz82gAECt3S1NdXPouZX0j7To5V8FjaISYDpHODZ1blbnpPGI3PhIAOpX5MgdlL62SY8vvBNZX0gFKvhg=="
org = "soumi_bt18@iiitkalyani.ac.in"
bucket = "Demo"

client = influxdb_client.InfluxDBClient(url="https://us-east-1-1.aws.cloud2.influxdata.com", token=token, org=org)


write_api = client.write_api(write_options=SYNCHRONOUS)

p = influxdb_client.Point("my_measurement").tag("location", "Prague").field("temperature", 35.3)
write_api.write(bucket=bucket, org=org, record=p)

p1 = influxdb_client.Point("my_measurement").tag("location", "Prague").field("temperature", 45.3)
write_api.write(bucket=bucket, org=org, record=p1)

query_api = client.query_api()

numbers1 = []

query1 = ' from(bucket:"Demo")\
|> range(start: -200y)\
|> filter(fn:(r) => r._field == "Temp" ) '

result = query_api.query(org=org, query=query1)

results1 = []
for table in result:
  for record in table.records:
    numbers1.append(record.get_value())
    results1.append([record.get_field(), record.get_value()])


import matplotlib.pyplot as plt 

print(result)

print("results",results1)
print("numbers",numbers1)

plt.plot(numbers1)
plt.ylabel('Daily Temperatures in Melbourne, Australia')
plt.show()