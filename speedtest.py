import os
import re
import subprocess
from time import strftime, time

SPEED_LOG = TEMP_LOG = os.path.abspath(
  os.path.join(os.path.dirname(__file__), "logs", "speed_log.csv"))

def test_speed():
    print("Testing speed...")
    ret = {}
    response = subprocess.Popen("speedtest-cli --simple", shell=True, stdout=subprocess.PIPE).stdout
    response = response.read().decode('utf-8')
    ret["ping"] = re.findall("Ping:\s(.*?)\s", response, re.MULTILINE)[0]
    ret["down"] = re.findall("Download:\s(.*?)\s", response, re.MULTILINE)[0]
    ret["up"] = re.findall("Upload:\s(.*?)\s", response, re.MULTILINE)[0]
    return ret

def check_header(log_file = SPEED_LOG):
    if not os.path.isfile(log_file) or os.stat(log_file).st_size == 0:
        with open(log_file, "a") as log:
            head = "{0},{1},{2},{3}\n".format("time", "ping (ms)", "download (Mbit/s)", "upload (Mbit/s)")
            log.write(head)

def write_speed(result, log_file = SPEED_LOG):
    print("result: ", result)
    with open(log_file, "a") as log:
        time = strftime("%Y-%m-%d %H:%M:%S")
        ping = str(result["ping"])
        download = str(result["down"])
        upload = str(result["up"])
        log.write("{0},{1},{2},{3}\n".format(time, ping, download, upload))

if __name__ == "__main__":
    result = test_speed()
    check_header()
    write_speed(result)
    print("Speed test complete")
