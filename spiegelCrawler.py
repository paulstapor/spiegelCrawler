import pycurl
import certifi
from io import BytesIO


def performGetRequest() -> BytesIO:
    buffer = BytesIO()
    c = pycurl.Curl()
    c.setopt(c.URL,
             'https://www.spiegel.de/kultur/literatur/bestseller-jugendbuecher-a-d3134d41-f5ce-40c2-880e-6fc98752ed85')
    c.setopt(c.WRITEDATA, buffer)
    c.setopt(c.CAINFO, certifi.where())
    c.perform()
    c.close()
    return buffer


def isLupus(buffer) -> bool:
    body = buffer.getvalue()
    body = body.decode('utf-8')
    return body.find('Lupus Noctis') > 0


lupusFound = isLupus(performGetRequest())
if lupusFound:
    print("Lupus Noctis ist in der Spiegel-Bestseller-Liste!!!")
else:
    print("Leider hat es Lupus Noctis noch nicht in die Spiegel-Bestseller-Liste geschafft...")
