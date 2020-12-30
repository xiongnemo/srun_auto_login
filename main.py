import requests
import json
from urllib import parse
import base64

with open("./config.json") as config_json_str:
    config = json.loads(config_json_str.read())

TARGET_ENDPOINT = config["TARGET_ENDPOINT"]
USE_HTTPS = config["USE_HTTPS"]
USERNAME = config["USERNAME"]
PASSWORD = config["PASSWORD"]

USERNAME_URL_PARSED = parse.quote(USERNAME)
PASSWORD_BASE64 = base64.b64encode(PASSWORD.encode()).decode()
PASSWORD_BASE64_URL_PARSED = parse.quote(PASSWORD_BASE64)

HTTP_SCHEME = "https://" if USE_HTTPS else "http://"
BASE = HTTP_SCHEME + TARGET_ENDPOINT
RESOURCE = "/include/auth_action.php"


data = "action=login&username="\
    + USERNAME\
    + "&password={B}"\
    + PASSWORD_BASE64_URL_PARSED \
    + "&ac_id=1&user_ip=&nas_ip=&user_mac=&save_me=1&ajax=1"
srun_headers = {
    "Host": TARGET_ENDPOINT,
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
    "Accept": "*/*",
    "DNT": "1",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": BASE,
    "Referer": BASE + "/srun_portal_pc.php?ac_id=1&",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
}
r = requests.post(BASE + RESOURCE, data=data, headers=srun_headers)

print(r.status_code)
print(r.text)
