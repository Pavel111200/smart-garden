from http.server import HTTPServer, BaseHTTPRequestHandler
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
aht20 = DFRobot_AHT20()
air_quality = Air_quality()

data = {
    "moisture": 0,
    "temperature": 0,
    "humidity": 0,
    "light": 0,
    "air_quality": 0
}

class SmartGardenHTTPServer(BaseHTTPRequestHandler):
    @cached_property
    def post_data(self):
        content_length = int(self.headers.get("Content-Length", 0))
        return self.rfile.read(content_length)

    def do_GET(self):
        self.send_response(200)

        self.send_header("Content-type", "application/json")
        self.end_headers()

        data["moisture"] = moisture_sensor.get_sensor_value()
        data["light"] = light_sensor.get_sensor_value()
        if aht20.start_measurement_ready():
            (temperature, humidity) = aht20.get_sensor_value()
            data["temperature"] = temperature
            data["humidity"] = humidity
        data["air_quality"] = air_quality.get_sensor_value()

        self.wfile.write(bytes(json.dumps(data), "utf-8"))

    def do_POST(self):
        print(self.post_data.decode("utf-8"))
        self.send_response(200)

        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(bytes("", "utf-8"))

server = HTTPServer((HOST,PORT),SmartGardenHTTPServer)
print("Server started")
server.serve_forever()
server.server_close()
print("Server stoped")