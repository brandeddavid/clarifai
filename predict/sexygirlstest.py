import urllib
from clarifai import rest
from clarifai.rest import ClarifaiApp


app = ClarifaiApp(api_key='a3c7aa75cc924ed6830a1feaaf8ab2f7')

model = app.models.get("general-v1.3")

url='https://scontent.fnbo2-1.fna.fbcdn.net/v/t1.0-9/21371389_168465910373464_2334320689568462400_n.jpg?oh=758a48019d03da65cd1a45545da75011&oe=5A1A5BEF' #Enter Url or code scrapper here

result = model.predict_by_url(url)

#print(result)

#print(type(result))

data = (result['outputs'][0]['data']['concepts'])

for item in data:

    print(item['name'], item['value'])
