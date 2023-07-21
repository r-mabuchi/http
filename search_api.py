import requests
import pandas as pd

def zipinfo(zipcode):
    url = "https://zip-cloud.appspot.com/api/search?zipcode=" + str(zipcode)
    x = requests.get(url)
    x = x.json()
    x = x['results']
    y = pd.DataFrame(x)
    print(y)

zipinfo(1000001)