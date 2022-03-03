from datetime import datetime
import os

#from influxdb import InfluxDBClient

import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS


# You can generate an API token from the "API Tokens Tab" in the UI
token = "Replace token here"
org = "soumi_bt18@iiitkalyani.ac.in" #Replace your org here
bucket = "Demo"

client = influxdb_client.InfluxDBClient(url="https://us-east-1-1.aws.cloud2.influxdata.com", token=token, org=org)


write_api = client.write_api(write_options=SYNCHRONOUS)

p = influxdb_client.Point("my_measurement").tag("location", "Prague").field("temperature", 35.3)
write_api.write(bucket=bucket, org=org, record=p)

p1 = influxdb_client.Point("my_measurement").tag("location", "Prague").field("temperature", 45.3)
write_api.write(bucket=bucket, org=org, record=p1)

query_api = client.query_api()

result = query_api.query(org=org, query=query)

results = []
for table in result:
  for record in table.records:
    results.append([record.get_field(), record.get_value()])

print(results)

query1 = ' from(bucket:"Demo")\
|> range(start: -62y)\
|> filter(fn:(r) => r._field == "Temp" ) '

result = query_api.query(org=org, query=query1)

results = []
for table in result:
  for record in table.records:
    results.append([record.get_field(), record.get_value()])

print(results)