#!/usr/bin/env python

from flask import Flask
from flask.ext.responses import json_response
import psutil
import sarge
import re

app = Flask(__name__)

@app.route("/space")
def space():
    result = {"space": (100-psutil.disk_usage("/").percent)}
    return json_response(result, status_code=200)

@app.route("/battery")
def battery():
    result = {"battery_perc": -1, "remaining_seconds": -1, "temperature_c": -1, "adapter_on": None}
    p = sarge.run("acpi --everything", stdout=sarge.Capture())
    output = p.stdout.text

    first_line = output.splitlines()[0].strip()
    print(first_line)
    batt_perc_raw = re.findall("(\d\d)%", first_line)
    print(batt_perc_raw)
    result["battery_perc"] = int(batt_perc_raw[0])

    batt_remain_time = re.findall("(\d\d):(\d\d):(\d\d)", first_line)
    result["remaining_seconds"] = (lambda x: x[0]*3600+x[1]*60+x[2])(list(map(int, batt_remain_time[0])))

    temperature_raw = re.findall("Thermal .+(\d\d\.\d) degrees C", output)
    print("temp", temperature_raw)
    result["temperature_c"] = float(temperature_raw[0])

    adapter_on_raw = re.findall("Adapter \d: (on-line|off-line)", output)[0]
    print(adapter_on_raw)
    result["adapter_on"] = (adapter_on_raw == "on-line") and True or False

    return json_response(result, status_code=200)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
