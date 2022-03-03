import influxdb_client

token = "Replace token here"
org = "soumi_bt18@iiitkalyani.ac.in" #Replace your org here
bucket = "Demo"

client = influxdb_client.InfluxDBClient(url="https://us-east-1-1.aws.cloud2.influxdata.com", token=token, org=org)

query_api = client.query_api()

query1 = ' from(bucket:"Demo")\
|> range(start: -60y)\
|> filter(fn:(r) => r._field == "Temp" ) '

result = query_api.query(org=org, query=query1)

results = []
for table in result:
  for record in table.records:
    results.append([record.get_field(), record.get_value()])

for i in results:
  print(i[0], i[1])