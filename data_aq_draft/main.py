import os
from dotenv import load_dotenv
from qingping.client import QingPing
from datetime import datetime
from pymongo import MongoClient

load_dotenv()
app_key = os.environ["APP_KEY"]
app_secret = os.environ["APP_SECRET"]

client = QingPing(app_key, app_secret)

devices = client.devices.list()

# balkon
sensor_data = devices["devices"][0]["data"]

temperature = sensor_data["temperature"]["value"]
humidity = sensor_data["humidity"]["value"]
co2 = sensor_data["co2"]["value"]
pm25 = sensor_data["pm25"]["value"]
pm10 = sensor_data["pm10"]["value"]

data_dict = {
    "timestamp": datetime.now().isoformat(),
    "temperature": temperature,
    "humidity": humidity,
    "co2": co2,
    "pm25": pm25,
    "pm10": pm10,
}

# print(data_dict)

client = MongoClient()
db = client["qingping"]
collection = db["balkon"]

collection.insert_one(data_dict)
print(data_dict)

