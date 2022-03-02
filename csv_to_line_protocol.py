import pandas as pd
import time

df = pd.read_csv("daily-min-temperatures.csv")
time_col = []
for d in range(len(df)):
    timestamp = time.mktime(time.strptime(str(df["Date"][d]), '%Y-%m-%d')) - time.timezone
    time_col.append(int(timestamp))
df["Timestamp"] = time_col


lines = ["price"
         + ",type=BTC"
         + " "
         + "Temp=" + str(df["Temp"][d]) 
         + " " + str(df["Timestamp"][d]) for d in range(len(df))]
thefile = open('text_file.txt', 'w')
for item in lines:
    thefile.write("%s\n" % item)