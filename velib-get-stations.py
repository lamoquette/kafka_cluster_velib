import json
import time
import urllib.request

from kafka import KafkaProducer

API_KEY = "2a611fcdbbc9ef57345c913cbd2b0c80dc168832"
url = "https://api.jcdecaux.com/vls/v1/stations?apiKey={}".format(API_KEY)

producer = KafkaProducer(bootstrap_servers="localhost:9092")

while True:
    response = urllib.request.urlopen(url)
    stations = json.loads(response.read().decode())
    for station in stations:
        producer.send("velib-stations", json.dumps(station).encode())
    print("{} Produced {} station records".format(time.time(), len(stations)))
    time.sleep(1)