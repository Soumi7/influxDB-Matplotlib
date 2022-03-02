import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS

token = "29ZCFBz82gAECt3S1NdXPouZX0j7To5V8FjaISYDpHODZ1blbnpPGI3PhIAOpX5MgdlL62SY8vvBNZX0gFKvhg=="
org = "soumi_bt18@iiitkalyani.ac.in"
bucket = "Demo"

client = influxdb_client.InfluxDBClient(url="https://us-east-1-1.aws.cloud2.influxdata.com", token=token, org=org)

write_api = client.write_api(write_options=SYNCHRONOUS)

p = influxdb_client.Point("my_measurement").tag("location", "India").field("temperature", 35.3)
write_api.write(bucket=bucket, org=org, record=p)

p1 = influxdb_client.Point("my_measurement").tag("location", "India").field("temperature", 45.3)
write_api.write(bucket=bucket, org=org, record=p1)

p2 = influxdb_client.Point("my_measurement").tag("location", "India").field("temperature", 15.3)
write_api.write(bucket=bucket, org=org, record=p2)

