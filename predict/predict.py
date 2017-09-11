import urllib
from clarifai import rest
from clarifai.rest import ClarifaiApp


app = ClarifaiApp(api_key='a3c7aa75cc924ed6830a1feaaf8ab2f7')

model = app.models.get("general-v1.3")

url='https://scontent.fnbo2-1.fna.fbcdn.net/v/t1.0-9/20915626_163083024245086_5811988536670428723_n.jpg?oh=8bc06b811ebf9ec653730d3168619096&oe=5A5989B1'

result = model.predict_by_url(url)

#print(result)

#print(type(result))

data = (result['outputs'][0]['data']['concepts'])

for item in data:
   

    print(item['name'], item['value'])

