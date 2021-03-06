import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS

token = "Replace token here"
org = "soumi_bt18@iiitkalyani.ac.in" #Replace your org here
bucket = "Demo"

client = influxdb_client.InfluxDBClient(url="https://us-east-1-1.aws.cloud2.influxdata.com", token=token, org=org)

query_api = client.query_api()

query = ' from(bucket:"Demo")\
|> range(start: -10m)\
|> filter(fn:(r) => r._measurement == "my_measurement")\
|> filter(fn: (r) => r.location == "India")\
|> filter(fn:(r) => r._field == "temperature" ) '

result = query_api.query(org=org, query=query)

results = []
for table in result:
  for record in table.records:
    results.append([record.get_field(), record.get_value()])

for i in results:
    print(i[0],i[1])