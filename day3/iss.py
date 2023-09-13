import urllib.request

url = "http://api.open-notify.org/iss-now.json"

def iss_position():
    while True:
        with urllib.request.urlopen(url) as response:
            data = response.read()
            yield data.decode('utf8')

