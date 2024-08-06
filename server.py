from http.server import BaseHTTPRequestHandler
from functools import cached_property
from moisture import Moisture
from light import Light
from DFRobot_AHT20 import *
from air_quality import Air_quality
import json


HOST = "192.168.2.236"
PORT = 9999
moisture_sensor = Moisture()
light_sensor = Light()
aht20_sensor = DFRobot_AHT20()
air_quality_sensor = Air_quality()

class SmartGardenHTTPHandler(BaseHTTPRequestHandler):
    @cached_property
    def post_data(self):
        content_length = int(self.headers.get("Content-Length", 0))
        return self.rfile.read(content_length)

    def do_GET(self):
        self.send_response(200)

        self.send_header("Content-type", "application/json")
        self.end_headers()

        if self.server.aht20_sensor.start_measurement_ready():
            (temperature_c, temperature_f, humidity) = self.server.aht20_sensor.get_sensor_value()

        data = {
            "moisture": self.server.moisture_sensor.get_sensor_value(),
            "light": self.server.light_sensor.get_sensor_value(),
            "temperature_C": temperature_c,
            "temperature_F": temperature_f,
            "humidity": humidity,
            "air_quality": self.server.air_quality_sensor.get_sensor_value()
        }

        self.wfile.write(bytes(json.dumps(data), "utf-8"))

    def do_POST(self):
        print(self.post_data.decode("utf-8"))
        self.send_response(200)

        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(bytes("", "utf-8"))