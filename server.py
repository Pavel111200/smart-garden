from http.server import BaseHTTPRequestHandler
from functools import cached_property
from moisture import Moisture
from light import Light
from DFRobot_AHT20 import *
from air_quality import Air_quality
import json
import cgi


HOST = "192.168.2.236"
PORT = 9999

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
            (temperature_c,
              temperature_f,
                humidity) = self.server.aht20_sensor.get_sensor_value()

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
        data = json.loads(self.post_data)
        if data["moisture"] != 0:
            self.server.moisture_sensor.watering_value = data["moisture"]
        if data["light"] != 0:
            self.server.light_sensor.turn_on_value = data["light"]
        if data["temperature"] != 0:
            self.server.aht20_sensor.temp_turn_on_value = data["temperature"]
        if data["humidity"] != 0:
            self.server.aht20_sensor.humd_turn_on_value = data["humidity"]
        self.send_response(200)

        self.send_header("Content-type", "text/plain")
        self.end_headers()
    
        self.wfile.write(bytes("", "utf-8"))