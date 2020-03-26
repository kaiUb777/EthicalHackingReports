import requests
import hashlib
import re

url = "http://docker.hackthebox.eu:30943/" #change port if you need
session = requests.Session()
out = session.get(url)
str = re.search(r"<h3 align='center'>(\w*)</h3>", out.text)

result = hashlib.md5(str.group(1).encode('utf-8')).hexdigest()

print("Sending MD5:-{}".format(result))

data = {'hash': result}
out = session.post(url = url, data = data)

print(out.text)
