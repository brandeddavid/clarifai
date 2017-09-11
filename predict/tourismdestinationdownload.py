import urllib
from clarifai import rest
from clarifai.rest import ClarifaiApp


app = ClarifaiApp(api_key='a3c7aa75cc924ed6830a1feaaf8ab2f7')

model = app.models.get("general-v1.3")

url='' #Enter Url or code scrapper here

result = model.predict_by_url(url)

#print(result)

#print(type(result))

data = (result['outputs'][0]['data']['concepts'])

for item in data:

    if item['name'] == 'tourism' and item['value'] >= 0.5:

        urllib.request.urlretrieve(url, "image1.jpg")

