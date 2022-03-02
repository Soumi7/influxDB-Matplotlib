from flask import Flask, render_template, request
import matplotlib.pyplot as plt

import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS

token = "29ZCFBz82gAECt3S1NdXPouZX0j7To5V8FjaISYDpHODZ1blbnpPGI3PhIAOpX5MgdlL62SY8vvBNZX0gFKvhg=="
org = "soumi_bt18@iiitkalyani.ac.in"
bucket = "Demo"

client = influxdb_client.InfluxDBClient(url="https://us-east-1-1.aws.cloud2.influxdata.com", token=token, org=org)
query_api = client.query_api()

write_api = client.write_api(write_options=SYNCHRONOUS)

app = Flask(__name__)

@app.route('/plot')
def chartTest():

      query = ' from(bucket:"Demo")\
      |> range(start: -10m)\
      |> filter(fn:(r) => r._measurement == "my_measurement")\
      |> filter(fn: (r) => r.location == "India")\
      |> filter(fn:(r) => r._field == "temperature" ) '

      result = query_api.query(org=org, query=query)

      numbers = []

      results = []
      for table in result:
            for record in table.records:
                  numbers.append(float(record.get_value()))
                  results.append([record.get_field(), record.get_value()])

      print(numbers)
      plt.plot(numbers)
      plt.ylabel('India temperatures recently')  
      plt.savefig('./static/images/new_plot.png')
      return render_template('plot.html', name = 'new_plot', url ='./static/images/new_plot.png')

@app.route('/')
def student():
   return render_template('record.html')

@app.route('/addRecord',methods = ['POST', 'GET'])
def update():
      result = request.form
      print('result from updater',result)
      global data
      location=result['Location']
      temperature=float(result['Temperature'])
      print(location,temperature)
      print(type(location),type(temperature))

      p = influxdb_client.Point("my_measurement").tag("location", location).field("temperature", temperature)
      write_api.write(bucket=bucket, org=org, record=p)
      
      return render_template('record.html')

if __name__ == '__main__':
   app.run(debug = True)