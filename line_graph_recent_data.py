
import influxdb_client
import matplotlib.pyplot as plt

token = "Replace token here"
org = "soumi_bt18@iiitkalyani.ac.in" #Replace your org here
bucket = "Demo"

client = influxdb_client.InfluxDBClient(url="https://us-east-1-1.aws.cloud2.influxdata.com", token=token, org=org)

query_api = client.query_api()

query = ' from(bucket:"Demo")\
|> range(start: -30m)\
|> filter(fn:(r) => r._measurement == "my_measurement")\
|> filter(fn: (r) => r.location == "India")\
|> filter(fn:(r) => r._field == "temperature" ) '

result = query_api.query(org=org, query=query)

numbers = []

results = []
for table in result:
  for record in table.records:
    numbers.append(record.get_value())
    results.append([record.get_field(), record.get_value()])

plt.plot(numbers)
plt.ylabel('India temperatures recently')
plt.show()

